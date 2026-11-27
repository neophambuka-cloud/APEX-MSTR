# Codex task: APEX foundation F0 -> F1 (branch codex/apex-foundation-2026-11)

Start by reading AGENTS.md, docs/ARCHITECTURE.md, docs/HYPOTHESES.md and docs/STRC_CARRY_RESEARCH.md.
Inspect and preserve any existing project files. The new apex_foundation package is an intentionally small, standard-library-only scaffold with tests, not a live bot.

Task 1: Verify VALR API endpoints, accessible MSTR perp instrument identifier, market availability and fee schedule against https://docs.valr.com/ and VALR terms. Record evidence URLs + timestamps; never invent a symbol or a JSON schema.
Task 2: Implement read-only public-market client with explicit timeouts, retry/backoff, request metrics and mockable transport; unit tests use fixtures only.
Task 3: Implement append-only event ledger, UTC schema validator, deduplication and delayed/replayed feed tests. Record source instrument and underlying separately.
Task 4: Add historical data importer for MSTR NASDAQ session, BTC USD and MSTR perps, including market-hours calendars, DST and funding cashflows. If entitlement or data access cannot be verified, mark blocked rather than synthesise live-looking data.
Task 5: Add paper-only risk engine, simulator and hypothesis backtests. No live trading methods. No API secret required for tests.
Task 6: Add a non-blocking STRC token-carry research fixture: measure quantity credits/rebases, sellable token amount, token price, exit liquidity, ZAR conversion, financing repayments and both rising/falling BTC liability scenarios. Mark any unknown as a measurable input, not a blanket blocker to F1.
Task 7: Produce a verification report identifying data gaps and the one minimum next step. Create a PR; do not merge without review.

Rules: No real account reads requiring secrets without user consent; no borrowing, deposits, withdrawals, or trading. No profit claims before out-of-sample and realistic friction testing.
Run: python -m unittest discover -s tests -v
