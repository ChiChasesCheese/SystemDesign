You are triaging a codebase into a study system. For each artefact below decide
what it should become, and answer with one JSON object (no prose).

## Codebase
quant-stroller at c0cc39c68d33, cached read-only at .trellis/codebases/quant-stroller

## Lenses and their leaves
### markets
- `foundations.premia` — Return Foundations: Risk premium vs alpha vs beta, expected return as a discount rate, "bad returns in bad times", and Ilmanen's four building blocks — asset class premia, illiquidity, style premia, alpha.
- `foundations.asset-class-premia` — Return Foundations: The equity risk premium and its puzzle, the bond, credit and commodity premia, and the illiquidity premium charged by private and thinly traded assets.
- `foundations.efficiency` — Return Foundations: The three forms of EMH, the joint-hypothesis problem, behavioural biases, and why limits to arbitrage let mispricings survive contact with smart money.
- `foundations.capm` — Return Foundations: CAPM and the security market line with beta as the first factor, plus the volatility/Sharpe/drawdown/skew vocabulary every premium gets quoted in.
- `equities.instruments` — Equities & Equity Structure: Common vs preferred, share classes and free float, dividends, splits, spin-offs and ADRs — and why every backtest needs adjusted prices.
- `equities.structure` — Equities & Equity Structure: Reg NMS and the NBBO, fragmentation across lit and dark venues, maker-taker and payment for order flow, and the opening and closing auctions.
- `equities.short-selling` — Equities & Equity Structure: Locates and borrow fees, hard-to-borrow names and recalls, short squeezes, and borrow cost as the price of the constraint that lets overpricing persist.
- `equities.indices` — Equities & Equity Structure: Index construction and cap vs equal weighting, ETF creation/redemption arbitrage, and the flow effects of index inclusion and rebalancing.
- `futures.mechanics` — Futures & Forwards: Contract specs, initial vs variation margin, central clearing and daily marking, delivery vs cash settlement, and where a future stops being a forward.
- `futures.term-structure` — Futures & Forwards: Cost of carry and convergence, contango vs backwardation, roll yield, calendar spreads, and how continuous series get stitched.
- `futures.sectors` — Futures & Forwards: What actually differs across equity index, bond, STIR, FX, energy, metals and agricultural contracts — specs, seasonality, and curve shape.
- `options.payoffs` — Options & Volatility Instruments: Calls and puts as payoff diagrams, put-call parity as a no-arbitrage identity, moneyness, and the standard spread and combination structures.
- `options.pricing` — Options & Volatility Instruments: Risk-neutral valuation, Black-Scholes-Merton and binomial trees, and the real-world failure mode hiding behind each assumption.
- `options.greeks` — Options & Volatility Instruments: Delta, gamma, vega, theta and rho as a hedging vocabulary, and the gamma-theta trade every option position either pays or collects.
- `options.surface` — Options & Volatility Instruments: Implied volatility as a quoting convention, equity skew and FX smile, term structure, and sticky-strike vs sticky-delta dynamics.
- `options.vol-products` — Options & Volatility Instruments: VIX and its futures curve, variance and volatility swaps, vol ETPs and their roll drag, and the exotics (barriers, autocallables) worth recognising.
- `fixed-income.curve` — Rates & Credit: Spot, par and forward curves and their bootstrapping; level/slope/curvature as the three PCs; the expectations hypothesis, its rejection, and the countercyclical term premium that replaces it.
- `fixed-income.risk` — Rates & Credit: Duration, DV01, convexity and key-rate exposures — the units a rates desk speaks in and the hedges they imply.
- `fixed-income.instruments` — Rates & Credit: Bills, notes and bonds; futures with conversion factors and the cheapest-to-deliver option; the cash-futures basis trade; swaps, OIS discounting and the LIBOR-to-SOFR transition.
- `fixed-income.funding` — Rates & Credit: Repo and reverse repo, collateral and haircuts, money-market rates, and funding spreads as the market's stress gauge.
- `fixed-income.credit` — Rates & Credit: Corporate bonds and spread measures (G-spread, Z-spread, OAS), ratings and seniority, CDS mechanics and indices, and the CDS-bond basis.
- `fixed-income.credit-premium` — Rates & Credit: The credit spread puzzle — decomposing a spread into expected default, illiquidity, and genuine risk compensation, and credit's equity-like factor exposure.
- `fx.mechanics` — Foreign Exchange: Quoting and settlement conventions, outright forwards and FX swaps, NDFs, and the dealer/ECN structure of a 24-hour OTC market.
- `fx.parity` — Foreign Exchange: Covered interest parity as arbitrage, uncovered parity as a failed prediction, the forward premium puzzle, and the post-2008 cross-currency basis.
- `fx.drivers` — Foreign Exchange: PPP and real exchange rates, terms of trade, pegs and intervention, EM vs G10 behaviour, and the dollar as a global risk factor.
- `crypto.instruments` — Crypto Markets: Spot venues, perpetual swaps and the funding-rate mechanism, dated futures and their basis, and the options market's shape.
- `crypto.structure` — Crypto Markets: Centralised vs decentralised venues, AMMs and impermanent loss, MEV and the public mempool, liquidation cascades, exchange credit risk, and what on-chain data exposes that TradFi hides.
- `crypto.premia` — Crypto Markets: Funding and basis carry, cross-sectional and time-series momentum, and the open question of which equity-style factors survive in a market this reflexive.
- `microstructure.participants` — Market Microstructure: Harris's taxonomy — informed, value, news and utilitarian traders, dealers, front-runners and bluffers — and why each one is at the table.
- `microstructure.order-book` — Market Microstructure: Order types, price-time priority and matching, continuous trading vs call auctions, and quote-driven vs order-driven market designs.
- `microstructure.spread` — Market Microstructure: The three components of the bid-ask spread, Glosten-Milgrom adverse selection and Kyle's lambda, and why a resting quote is a free option written to the informed.
- `microstructure.liquidity` — Market Microstructure: Liquidity as tightness, depth, immediacy and resiliency; the square-root impact law; temporary vs permanent impact and order-flow imbalance as a price signal.
- `microstructure.market-making` — Market Microstructure: The economics of supplying liquidity — inventory risk, queue position, rebates — the HFT strategy families, and what flash events reveal about them.
- `factors.models` — Factor Foundations: A factor as a long-short portfolio, characteristics vs covariances, and the lineage CAPM to Fama-French 3, Carhart 4, FF5, the q-factor model and mispricing factors.
- `factors.rationale` — Factor Foundations: The three defences of any premium — risk compensation, behavioural bias, limits to arbitrage — plus the question that disciplines all three — who is on the other side of this trade, and why do they keep paying?
- `factors.zoo` — Factor Foundations: Harvey-Liu-Zhu's multiple-testing hurdle, Hou-Xue-Zhang's replication failures, McLean-Pontiff's post-publication decay, and open-source asset pricing as the reality check.
- `factors.cycles` — Factor Foundations: Factor drawdowns and cyclicality, crowding and capacity limits, and the timing debate between valuation spreads and "factor timing is hard".
- `momentum.cross-sectional` — Momentum & Trend: 12-1 relative strength, industry and residual momentum, the under-reaction story, and the momentum crashes that follow bear-market rebounds.
- `momentum.trend` — Momentum & Trend: TSMOM and managed futures across asset classes, the lookback-straddle payoff behind the crisis-alpha claim, and the awkward fact that time-series trend is largely cross-sectional momentum plus a net long.
- `momentum.fundamental` — Momentum & Trend: Post-earnings-announcement drift, analyst revisions and earnings momentum — price momentum's slower-moving fundamental cousin.
- `value.equity` — Value & Mean Reversion: Book-to-market and HML, alternative multiples, the intangibles critique, the value spread, and the 2018-2020 drawdown that reopened the argument.
- `value.cross-asset` — Value & Mean Reversion: Value everywhere — real yields in bonds, PPP in currencies, five-year reversal in commodities, and index-level equity value.
- `value.reversal` — Value & Mean Reversion: Short-horizon reversal as paid liquidity provision, long-horizon reversal, and cointegration-based pairs trading and stat arb.
- `carry.concept` — Carry: Carry defined as expected return under an unchanged price, its split from roll-down and spot drift, and the cross-asset unification of Koijen et al.
- `carry.rates-fx` — Carry: FX carry and the forward premium puzzle, curve carry and rolldown in rates, credit carry — and the crash risk that funds all three.
- `carry.commodities` — Carry: The theory of storage and convenience yield, Keynesian hedging pressure and normal backwardation, and roll return as the bulk of long-run commodity futures returns.
- `defensive.low-risk` — Defensive, Quality & Size: The low-volatility anomaly and BAB, the four competing stories (leverage constraints, benchmarking, lottery demand, and "it is just profitability and size"), and the beta-neutral construction the trade demands.
- `defensive.quality` — Defensive, Quality & Size: Quality Minus Junk and its profitability/growth/safety legs, gross profitability and asset growth, accruals, and the distress puzzle where the riskiest firms earn the least.
- `defensive.size-liquidity` — Defensive, Quality & Size: The size premium and its shrinking evidence, size as a conditioner on other factors, and the illiquidity premium of Amihud and Pastor-Stambaugh.
- `volatility.vrp` — Volatility as a Premium: Why implied volatility persistently exceeds realised, who is paying for it, why the premium lives at the front of the curve, and the negatively skewed payoff of harvesting it.
- `volatility.correlation` — Volatility as a Premium: Implied correlation, index vs single-name volatility, dispersion trading, and correlation as the thing that spikes exactly when you need it not to.
- `volatility.tail` — Volatility as a Premium: The skew premium, long-volatility and tail-hedge strategies, and the bleed of carrying protection that pays once a decade.
- `events.merger-arb` — Event-Driven Premia: Deal spreads as compensation for break risk, cash vs stock deal hedging, and merger arb's short-put payoff profile.
- `events.corporate` — Event-Driven Premia: Net share issuance and buybacks, IPO and SEO underperformance, spin-offs and index-driven forced trades.
- `events.calendar` — Event-Driven Premia: The scheduled-announcement premium around FOMC and macro releases, index rebalance flows and the vanishing index effect, month and quarter-end cash demand, and same-calendar-month return seasonality.
- `macro.growth-inflation` — Macro & Cross-Asset: The growth/inflation quadrant framework, real yields and breakevens, and which assets win in each cell.
- `macro.policy` — Macro & Cross-Asset: The central bank reaction function, QE and QT, fiscal shocks, and reading the priced policy path off the front of the curve.
- `macro.cross-asset` — Macro & Cross-Asset: The stock-bond correlation, why inflation volatility flips its sign, and what a positive correlation does to 60/40 and to levered risk parity.
- `regimes.volatility` — Regimes, Crowding & Crises: Volatility clustering and the leverage effect, calm vs stressed states, asymmetric downside correlation and tail dependence — diversification thinning exactly when it is needed.
- `regimes.crowding` — Regimes, Crowding & Crises: Crowded trades and forced-unwind spirals, funding vs market liquidity (Brunnermeier-Pedersen), and the August 2007 quant quake as the template.
- `regimes.crises` — Regimes, Crowding & Crises: LTCM, 2008, Volmageddon, the March 2020 dash for cash and the 2022 LDI spiral — each a lesson about which premium was really being harvested.
- `alt-data.families` — Alternative Data & ML Signals: Satellite, card transaction, web-scrape, app-usage and shipping data — what each proxies, its lag and coverage, and its capacity and decay profile.
- `alt-data.text` — Alternative Data & ML Signals: News sentiment, filings and earnings-call language as signals, and what text adds beyond the numbers already in the filing.
- `alt-data.positioning` — Alternative Data & ML Signals: CFTC commitments of traders, short interest, dealer gamma and the gamma flip, and fund flows — reading positioning as a level to fade against flow as a rate to follow.
- `alt-data.ml` — Alternative Data & ML Signals: What ML adds to a linear factor model — nonlinearity, interactions and wide predictor sets (Gu-Kelly-Xiu) — and the signal it cannot manufacture.
### quant-infra
- `foundations.pipeline` — Research Foundations: Splitting research into data curation, feature analysis, strategy, backtesting and deployment stations instead of letting one researcher run a strategy end to end.
- `foundations.hypothesis` — Research Foundations: Demanding an economic mechanism and a written prediction before the backtest, and logging every trial so the search cost stays countable.
- `foundations.fundamental-law` — Research Foundations: Information ratio as IC times root breadth times transfer coefficient — what each term buys and how implementation friction caps the product.
- `foundations.return-statistics` — Research Foundations: Fat tails, serial correlation, regime dependence, and an effective sample size far smaller than the row count implies.
- `data.point-in-time.as-of` — Data Correctness › Point-in-Time Discipline: Bitemporal tables separating effective date from knowledge date, as-reported versus restated fundamentals, filing and announcement lags, and vendor vintages.
- `data.point-in-time.universe` — Data Correctness › Point-in-Time Discipline: Rebuilding the tradable universe as of each date — delistings, bankruptcies, point-in-time index membership, and the backfill bias in vendor histories.
- `data.security-master` — Data Correctness: Identifier mapping across ticker reuse, mergers and CUSIP/ISIN/FIGI churn, plus split, dividend and spinoff adjustment factors and total- versus price-return series.
- `data.market-data.bars` — Data Correctness › Market Data: Trade conditions and busted prints, consolidated versus direct feeds, and why volume, dollar and imbalance bars sample information more evenly than clock time.
- `data.market-data.book` — Data Correctness › Market Data: L1/L2/L3 depth, snapshot-plus-delta reconstruction, sequence numbers, and what one dropped packet does to every downstream feature.
- `data.market-data.time` — Data Correctness › Market Data: Exchange versus capture versus ingest timestamps, session and holiday calendars, timezone and DST handling, and clock sync as a correctness requirement.
- `data.quality` — Data Correctness: Automated checks for stale prices, missing bars, unit changes and outliers; cross-vendor reconciliation, quarantine, and corrections that replay deterministically.
- `features.construction` — Features & Labels: Stationarity versus memory via fractional differentiation, cross-sectional ranking and winsorizing, and neutralizing a feature against exposures you are not paid to hold.
- `features.labeling.targets` — Features & Labels › Labeling: Fixed-horizon returns versus profit-taking, stop-loss and time barriers, and why path-dependent labels match how a position is actually held.
- `features.labeling.weights` — Features & Labels › Labeling: Overlapping outcomes break the IID assumption — concurrency-based uniqueness, sequential bootstrap, time decay and return-attribution weights.
- `features.labeling.meta` — Features & Labels › Labeling: A secondary model that sizes or vetoes a primary model's calls, converting a recall-heavy signal into a precision-managed bet.
- `features.leakage` — Features & Labels: Target leakage, features computed with future data, full-sample normalization and cross-ticker group leakage — and the test that catches each one.
- `features.selection` — Features & Labels: MDI versus MDA versus single-feature importance, substitution effects among correlated features, and why in-sample importance is a multiple-testing artifact.
- `features.store` — Features & Labels: Feature definitions as versioned code with lineage and backfills, serving identical point-in-time semantics to research and to live.
- `backtest.engines` — Backtesting: Vectorized versus event-driven simulation, the state an event loop must own — orders, positions, cash — and which classes of error vectorization hides.
- `backtest.mechanics.timing` — Backtesting › Simulation Mechanics: Signal timestamp versus order timestamp versus fill timestamp, bar-close-to-next-open conventions, and budgeting the decision latency live will really have.
- `backtest.mechanics.fills` — Backtesting › Simulation Mechanics: Marketable versus resting orders, participation caps against printed volume, partial fills, and the queue-position assumption hiding inside every limit fill.
- `backtest.mechanics.costs` — Backtesting › Simulation Mechanics: Commissions, fees, spread crossing, borrow and financing, taxes — stated as an explicit cost model you will later calibrate against real fills.
- `backtest.mechanics.events` — Backtesting › Simulation Mechanics: Simulating trading halts, limit up/down bands, hard-to-borrow names, delisting proceeds and dividends received while a position is open.
- `backtest.metrics` — Backtesting: Sharpe annualization under autocorrelation, drawdown and time under water, turnover and holding period, and how much each one moves on a single parameter nudge.
- `backtest.validation.walk-forward` — Backtesting › Validation Protocols: Why shuffled cross-validation is invalid on overlapping labels, and how purging plus an embargo restores a defensible train/test boundary.
- `backtest.validation.cpcv` — Backtesting › Validation Protocols: Generating many backtest paths from held-out group combinations to obtain a distribution of Sharpe instead of one lucky number.
- `backtest.validation.synthetic` — Backtesting › Validation Protocols: Block bootstrap, Monte Carlo and generated price paths as a second opinion on the single historical path — and what they cannot tell you.
- `backtest.overfitting.multiple-testing` — Backtesting › Overfitting Control: Counting trials honestly, family-wise error versus false discovery control, and the expected maximum Sharpe a pure-noise search will hand you.
- `backtest.overfitting.deflated-sharpe` — Backtesting › Overfitting Control: Adjusting Sharpe for skew, kurtosis, track length and trial count, and using minimum track record length to answer how long until you believe it.
- `backtest.overfitting.pbo` — Backtesting › Overfitting Control: Combinatorially symmetric cross-validation — how often the in-sample best configuration lands below median out of sample, and reading the degradation plot.
- `portfolio.risk-models.structure` — Risk Models & Portfolio Construction › Factor Risk Models: Fundamental versus statistical versus macro models — exposures, factor covariance, specific risk, and what each form assumes about stability.
- `portfolio.risk-models.covariance` — Risk Models & Portfolio Construction › Factor Risk Models: Sample covariance noise when history is short relative to breadth, shrinkage, random-matrix denoising, and EWMA half-life as a responsiveness dial.
- `portfolio.risk-models.attribution` — Risk Models & Portfolio Construction › Factor Risk Models: Splitting portfolio variance into factor and specific components, marginal contribution to risk, and surfacing the unintended bets nobody sized.
- `portfolio.optimization.mvo` — Risk Models & Portfolio Construction › Optimization: Why unconstrained mean-variance maximizes estimation error, and what Black-Litterman, resampling, risk parity and hierarchical risk parity do about it.
- `portfolio.optimization.constraints` — Risk Models & Portfolio Construction › Optimization: Position, sector and beta limits and tracking-error budgets as implicit views; turnover penalties, no-trade bands and cost-aware objectives.
- `portfolio.combination` — Risk Models & Portfolio Construction: Blending correlated alphas across horizons — orthogonalization, IC-weighted and covariance-aware combination, and matching forecast horizon to holding period.
- `portfolio.sizing` — Risk Models & Portfolio Construction: Kelly and why practitioners run a fraction of it, volatility targeting, mapping signal strength to size, and gross and net leverage limits.
- `execution.microstructure.book` — Microstructure & Execution › Market Mechanics: Order types and time-in-force, price-time versus pro-rata matching, queue position as an asset, and what a cancel/replace costs you in the queue.
- `execution.microstructure.sessions` — Microstructure & Execution › Market Mechanics: Opening and closing auctions, halts and reopenings, tick and lot size regimes, and why so much volume prints in the last minutes of the day.
- `execution.microstructure.fragmentation` — Microstructure & Execution › Market Mechanics: Multiple lit venues and dark pools, consolidated tape versus direct feeds, order protection rules, and the adverse selection a slow router pays.
- `execution.spread` — Microstructure & Execution: The bid-ask spread as compensation for inventory risk and informed flow, with quoted, effective and realized spread as the diagnostic trio.
- `execution.impact` — Microstructure & Execution: Temporary versus permanent impact, the square-root law in participation rate, Almgren-Chriss and I-Star style models, impact decay, and the capacity ceiling they imply.
- `execution.algos` — Microstructure & Execution: VWAP, TWAP and POV versus arrival-price schedules, the impact-against-timing-risk trade-off, and passive or aggressive child order placement.
- `execution.tca` — Microstructure & Execution: Decomposing implementation shortfall into delay, impact, timing and opportunity cost against a chosen benchmark, then feeding realized costs back into the backtest cost model.
- `platform.parity` — Research Platform Engineering: One code path for features, signals and accounting across sim and live, with config-driven venues and automated sim-versus-live divergence tests.
- `platform.experiments` — Research Platform Engineering: Run manifests pinning code commit, config, dataset snapshot and seeds so any past number can be regenerated and every trial stays auditable.
- `platform.pipelines` — Research Platform Engineering: Research DAGs with idempotent tasks, incremental versus full recompute, backfill semantics, and caching keyed on data version rather than wall clock.
- `platform.testing` — Research Platform Engineering: Golden-file P&L regressions, property tests on accounting invariants, synthetic data with known answers, deterministic replay, and an explicit float tolerance policy.
- `platform.promotion` — Research Platform Engineering: Paper and shadow trading, canary sizing, written promotion criteria and rollback triggers — a release process rather than a launch decision.
- `trading.oms-ems` — Trading Systems: Who owns the parent order, allocations and compliance state versus who slices and routes children, and the FIX session that carries both.
- `trading.order-lifecycle` — Trading Systems: The order state machine, client order ids, cancel/replace races, ack timeouts, and duplicate protection when the gateway's answer never arrives.
- `trading.accounting` — Trading Systems: Real-time versus official positions, mark-to-market with realized and unrealized split, multi-currency cash, and applying corporate actions to a live book.
- `trading.connectivity` — Trading Systems: Session lifecycle and sequence-number recovery, resend requests, drop copies as an independent record, and start-of-day and end-of-day procedures.
- `trading.latency` — Trading Systems: A tick-to-trade budget across feed handler, strategy and gateway, why jitter and tail latency dominate the mean, and recognizing when latency is not the constraint.
- `controls.pre-trade` — Live Risk & Controls: Fat-finger size and notional caps, price collars, restricted and hard-to-borrow lists and duplicate-order detection, enforced in the order path rather than in the strategy.
- `controls.limits` — Live Risk & Controls: Position, exposure, loss and message-rate limits with defined breach actions — throttle, block, flatten — and a named human allowed to override them.
- `controls.monitoring` — Live Risk & Controls: Alerting on stale data, signal health, position drift against target and fill quality, with thresholds tight enough to matter and few enough to be read.
- `controls.reconciliation` — Live Risk & Controls: Daily reconciliation of the internal book against broker, custodian and drop copy, break classification, and settlement and corporate-action mismatches.
- `controls.incidents` — Live Risk & Controls: Runbooks for a runaway algo, the flatten-versus-hold decision under uncertainty, deployment failures of the Knight Capital family, and blameless postmortems.
- `lifecycle.divergence` — Live Strategy Lifecycle: Attributing the gap between simulated and realized P&L to costs, capacity, timing, data differences or plain bugs before blaming the market.
- `lifecycle.attribution` — Live Strategy Lifecycle: Decomposing realized P&L by factor exposure, by signal, by execution and by residual, so the unexplained part stays small and named.
- `lifecycle.decay` — Live Strategy Lifecycle: Measuring signal half-life and crowding, separating a drawdown consistent with the backtest from a structural break, and pre-committing retirement criteria.
- `lifecycle.retraining` — Live Strategy Lifecycle: Refit cadence and drift triggers, champion-challenger comparison, versioned model artifacts, and treating every unscheduled refit as another trial to count.
- `governance.compliance` — Compliance & Governance: Short-sale locates and rules, restricted lists and information barriers, self-trade prevention, market-abuse patterns, and best-execution obligations.
- `governance.audit` — Compliance & Governance: Immutable order and decision logs reconstructable to the millisecond, provenance linking a live model to the research run that produced it, and retention rules.
- `governance.model-risk` — Compliance & Governance: Independent validation of a strategy's assumptions, documented limitations and monitoring plan, and sign-off before capital — model risk management in the SR 11-7 shape.

## Artefacts
- `subject:architecture-and-data-flow` (subject, suggested lens quant-infra) — docs/concepts/architecture-and-data-flow.md
- `subject:citadel-multi-pod-platform` (subject, suggested lens quant-infra) — docs/concepts/citadel-multi-pod-platform.md
- `subject:crisis-convexity-vs-short-premium` (subject, suggested lens quant-infra) — docs/concepts/crisis-convexity-vs-short-premium.md
- `subject:domain-model` (subject, suggested lens quant-infra) — docs/concepts/domain-model.md
- `subject:long-short-and-neutral` (subject, suggested lens quant-infra) — docs/concepts/long-short-and-neutral.md
- `subject:macro-regime-and-sizing` (subject, suggested lens quant-infra) — docs/concepts/macro-regime-and-sizing.md
- `subject:market-sentiment-factors` (subject, suggested lens quant-infra) — docs/concepts/market-sentiment-factors.md
- `subject:multiple-testing` (subject, suggested lens quant-infra) — docs/concepts/multiple-testing.md
- `subject:quant-dev-multifactor-and-infra` (subject, suggested lens quant-infra) — docs/concepts/quant-dev-multifactor-and-infra.md
- `subject:risk-parity-and-all-weather` (subject, suggested lens quant-infra) — docs/concepts/risk-parity-and-all-weather.md
- `subject:trading-101` (subject, suggested lens quant-infra) — docs/concepts/trading-101.md
- `subject:video-scout-pipeline` (subject, suggested lens quant-infra) — docs/concepts/video-scout-pipeline.md
- `subject:why-backtests-lie` (subject, suggested lens quant-infra) — docs/concepts/why-backtests-lie.md
- `subject:costs-and-prices` (subject, suggested lens quant-infra) — docs/deep/costs-and-prices.md
- `subject:data-governance` (subject, suggested lens quant-infra) — docs/deep/data-governance.md
- `subject:data-layer-and-automation` (subject, suggested lens quant-infra) — docs/deep/data-layer-and-automation.md
- `subject:data-pipeline` (subject, suggested lens quant-infra) — docs/deep/data-pipeline.md
- `subject:data-warehouse` (subject, suggested lens quant-infra) — docs/deep/data-warehouse.md
- `subject:factor-catalog` (subject, suggested lens quant-infra) — docs/deep/factor-catalog.md
- `subject:factor-risk-and-idiosyncratic-alpha` (subject, suggested lens quant-infra) — docs/deep/factor-risk-and-idiosyncratic-alpha.md
- `subject:forex-model-audit` (subject, suggested lens quant-infra) — docs/deep/forex-model-audit.md
- `subject:high-dim-factor-timing` (subject, suggested lens quant-infra) — docs/deep/high-dim-factor-timing.md
- `subject:index` (subject, suggested lens quant-infra) — docs/deep/index.md
- `subject:openbb-integration` (subject, suggested lens quant-infra) — docs/deep/openbb-integration.md
- `subject:parameters-and-hyperopt` (subject, suggested lens quant-infra) — docs/deep/parameters-and-hyperopt.md
- `subject:qlib-alpha-lab` (subject, suggested lens quant-infra) — docs/deep/qlib-alpha-lab.md
- `subject:signal-engineering` (subject, suggested lens quant-infra) — docs/deep/signal-engineering.md
- `subject:slow-fast-layering` (subject, suggested lens quant-infra) — docs/deep/slow-fast-layering.md
- `subject:strategy-styles` (subject, suggested lens quant-infra) — docs/deep/strategy-styles.md
- `subject:where-alpha-comes-from` (subject, suggested lens quant-infra) — docs/deep/where-alpha-comes-from.md
- `subject:advanced` (subject, suggested lens quant-infra) — docs/architecture/advanced.md
- `subject:borrowing-from-freqtrade` (subject, suggested lens quant-infra) — docs/architecture/borrowing-from-freqtrade.md
- `subject:citadel-framework-prd` (subject, suggested lens quant-infra) — docs/architecture/citadel-framework-prd.md
- `subject:citadel-pod-book` (subject, suggested lens quant-infra) — docs/architecture/citadel-pod-book.md
- `subject:citadel-research-and-sizing` (subject, suggested lens quant-infra) — docs/architecture/citadel-research-and-sizing.md
- `subject:data-flow` (subject, suggested lens quant-infra) — docs/architecture/data-flow.md
- `subject:freqtrade-full-comparison` (subject, suggested lens quant-infra) — docs/architecture/freqtrade-full-comparison.md
- `subject:hf-ai-gap-plan` (subject, suggested lens quant-infra) — docs/architecture/hf-ai-gap-plan.md
- `subject:index` (subject, suggested lens quant-infra) — docs/architecture/index.md
- `subject:live-and-event-driven` (subject, suggested lens quant-infra) — docs/architecture/live-and-event-driven.md
- `subject:module-graph` (subject, suggested lens quant-infra) — docs/architecture/module-graph.md
- `subject:module-map` (subject, suggested lens quant-infra) — docs/architecture/module-map.md
- `subject:risk-layer` (subject, suggested lens quant-infra) — docs/architecture/risk-layer.md
- `subject:seams` (subject, suggested lens quant-infra) — docs/architecture/seams.md
- `subject:vectorbt-nautilus-and-our-engines` (subject, suggested lens quant-infra) — docs/architecture/vectorbt-nautilus-and-our-engines.md
- `subject:vs-mainstream` (subject, suggested lens quant-infra) — docs/architecture/vs-mainstream.md
- `subject:01-momentum-trend` (subject, suggested lens markets) — docs/catalog/01-momentum-trend.md
- `subject:02-value-reversion` (subject, suggested lens markets) — docs/catalog/02-value-reversion.md
- `subject:03-carry` (subject, suggested lens markets) — docs/catalog/03-carry.md
- `subject:04-lowrisk-quality` (subject, suggested lens markets) — docs/catalog/04-lowrisk-quality.md
- `subject:05-size-liquidity` (subject, suggested lens markets) — docs/catalog/05-size-liquidity.md
- `subject:06-volatility-options` (subject, suggested lens markets) — docs/catalog/06-volatility-options.md
- `subject:07-event-fundamental` (subject, suggested lens markets) — docs/catalog/07-event-fundamental.md
- `subject:08-microstructure-intraday` (subject, suggested lens markets) — docs/catalog/08-microstructure-intraday.md
- `subject:09-macro-crossasset` (subject, suggested lens markets) — docs/catalog/09-macro-crossasset.md
- `subject:10-altdata-ml` (subject, suggested lens markets) — docs/catalog/10-altdata-ml.md
- `subject:11-portfolio-risk` (subject, suggested lens markets) — docs/catalog/11-portfolio-risk.md
- `subject:12-crypto-defi` (subject, suggested lens markets) — docs/catalog/12-crypto-defi.md
- `subject:index` (subject, suggested lens markets) — docs/catalog/index.md

## Verdicts
- `case` — the artefact records a DECISION that is an instance of something a
  leaf already teaches. Rewrite it in that lens's vocabulary: what problem it
  solves, what it forbids, what it costs. Never restate it as "we chose X";
  a reader who does not know this codebase must still learn something.
- `reading` — the artefact is SUBJECT MATTER for a leaf: it teaches a topic
  rather than recording a choice.
- `gap` — the artefact clearly belongs to one of these lenses but no leaf fits.
  Propose the leaf that is missing. This is a wanted outcome, not a failure.
- `skip` — housekeeping, duplication, or specific to this codebase in a way
  that teaches nothing transferable.

## Rules
- `nodes` must be leaf ids of the lens you chose, copied exactly from above.
- `slug` must be unique, lowercase-hyphenated, and start with `qs`.
- `body` is markdown, 100-250 words, written for someone who has never seen
  this repository. State the mechanism and the trade-off, not the conclusion.
- Be strict. An artefact that teaches nothing transferable is a `skip`, and
  skipping is cheaper than diluting the deck.

## Answer format
{"codebase": "quant-stroller", "ref": "c0cc39c68d33", "items": [
  {"artefact": "decisions:0004-...", "verdict": "case", "lens": "system-design",
   "nodes": ["async.log"], "slug": "qs-...", "title": "...",
   "body": "...", "confidence": "high"},
  {"artefact": "subject:...", "verdict": "gap", "lens": "quant-infra",
   "proposed_leaf": "data.point-in-time", "why": "..."},
  {"artefact": "subject:...", "verdict": "skip", "why": "..."}
]}
