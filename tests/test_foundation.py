import unittest
from datetime import datetime, timedelta, timezone
from decimal import Decimal

from apex_foundation.core import (
    MarketState, Observation, RiskConfig, gate_entry, estimate_carry_usd,
)


class TestApexFoundation(unittest.TestCase):
    def setUp(self):
        self.now = datetime(2026, 11, 27, 19, 0, tzinfo=timezone.utc)
        self.good = Observation(
            source="fixture", instrument="MSTR_PERP_TEST", timestamp=self.now,
            received=self.now, bid=Decimal("81.90"), ask=Decimal("81.91"),
            quote_currency="USDC", product_type="perpetual",
        )

    def test_never_authorizes_live_trade(self):
        decision = gate_entry(self.good, MarketState.HEALTHY, Decimal("1"), RiskConfig(), self.now)
        self.assertFalse(decision.may_enter)
        self.assertEqual(decision.reason, "paper_only_no_live_authorization")

    def test_stale_market_data_fails_closed(self):
        o = Observation("fixture", "MSTR", self.now - timedelta(minutes=10), self.now,
                        Decimal("80"), Decimal("81"), "USD", "equity")
        self.assertEqual(gate_entry(o, MarketState.HEALTHY, Decimal("1"), RiskConfig(), self.now).reason,
                         "stale_market_data")

    def test_liquidating_fails_closed(self):
        self.assertEqual(gate_entry(self.good, MarketState.LIQUIDATING, Decimal("1"), RiskConfig(), self.now).reason,
                         "market_state_liquidating")

    def test_spread_limit(self):
        o = Observation("fixture", "MSTR", self.now, self.now, Decimal("80"),
                        Decimal("81"), "USD", "equity")
        self.assertEqual(gate_entry(o, MarketState.HEALTHY, Decimal("1"), RiskConfig(), self.now).reason,
                         "spread_limit")

    def test_btc_borrow_appreciation_destoys_spread(self):
        # Borrow 1 BTC at $100, convert $100 to USD, receive $12; BTC rises 30%.
        value = estimate_carry_usd(Decimal(1), Decimal(100), Decimal(130),
                                  Decimal("0.0137"), Decimal(1), Decimal(12), Decimal(0))
        self.assertLess(value, 0)

    def test_stablecoin_borrow_small_spread_not_free(self):
        value = estimate_carry_usd(Decimal(100), Decimal(1), Decimal(1),
                                  Decimal("0.1114"), Decimal(1), Decimal(12), Decimal(2))
        self.assertLess(value, 0)


if __name__ == "__main__":
    unittest.main()
