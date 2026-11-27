"""Small, dependency-free invariants for APEX observation and risk evaluation."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from decimal import Decimal
from enum import Enum
from typing import Optional


class MarketState(str, Enum):
    HEALTHY = "healthy"
    WARNING = "warning"
    CRITICAL = "critical"
    LIQUIDATING = "liquidating"
    AUTO_CLOSED = "auto_closed"
    UNKNOWN = "unknown"


@dataclass(frozen=True)
class Observation:
    source: str
    instrument: str
    timestamp: datetime
    received: datetime
    bid: Decimal
    ask: Decimal
    quote_currency: str
    product_type: str

    def validate(self, max_age_seconds: int, now: Optional[datetime] = None) -> tuple[bool, str]:
        now = now or datetime.now(timezone.utc)
        if self.timestamp.tzinfo is None or self.received.tzinfo is None or now.tzinfo is None:
            return False, "timestamp_without_timezone"
        if self.timestamp > now or self.received > now:
            return False, "future_timestamp"
        if (now - self.timestamp).total_seconds() > max_age_seconds:
            return False, "stale_market_data"
        if not self.source or not self.instrument or not self.quote_currency or not self.product_type:
            return False, "missing_identifiers"
        if self.bid <= 0 or self.ask <= 0 or self.ask < self.bid:
            return False, "invalid_market_prices"
        return True, "ok"


@dataclass(frozen=True)
class RiskDecision:
    may_enter: bool
    reason: str


@dataclass(frozen=True)
class RiskConfig:
    max_age_seconds: int = 15
    max_spread_bps: Decimal = Decimal("30")
    max_leverage: Decimal = Decimal("1")
    allow_live_execution: bool = False  # intentionally not configurable by strategy


def gate_entry(
    observation: Observation,
    state: MarketState,
    leverage: Decimal,
    config: RiskConfig,
    now: Optional[datetime] = None,
) -> RiskDecision:
    valid, reason = observation.validate(config.max_age_seconds, now)
    if not valid:
        return RiskDecision(False, reason)
    if state is not MarketState.HEALTHY:
        return RiskDecision(False, f"market_state_{state.value}")
    if leverage <= 0 or leverage > config.max_leverage:
        return RiskDecision(False, "leverage_limit")
    spread_bps = (observation.ask - observation.bid) / observation.ask * Decimal("10000")
    if spread_bps > config.max_spread_bps:
        return RiskDecision(False, "spread_limit")
    return RiskDecision(False, "paper_only_no_live_authorization")

