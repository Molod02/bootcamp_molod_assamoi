# Quantitative Dynamic Volatility & Risk Monitoring Pipeline
**Stage:** Problem Framing & Scoping (Stage 01)

## Problem Statement
Quantitative risk systems often react too slowly during sudden market crashes because they rely on lagging historical averages. This exposes equity portfolios to severe financial loss. The Chief Risk Officer needs a proactive risk system to maintain fund safety limits, while the Portfolio Manager needs daily risk signals before market open (8:30 AM EST) to rebalance assets.

We are building a predictive Python data pipeline that forecasts 5-day forward volatility for core ETF holdings. The deliverable is an automated daily risk report notebook. Success will be measured using forecast accuracy (RMSE) and overall portfolio drawdown reduction.

## Stakeholder & User
* **Primary Stakeholder:** Chief Risk Officer (CRO) — Responsible for fund drawdown limits.
* **End User:** Portfolio Manager (PM) — Executes trading adjustments before 8:30 AM EST.

## Useful Answer & Decision
* **Answer Type:** Predictive (5-day forward volatility forecast).
* **Primary Metric:** Out-of-Sample RMSE & Sharpe Ratio improvement.
* **Deliverable Artifact:** Automated Python data pipeline and daily risk alert notebook.

## Assumptions & Constraints
* Free daily market price data (OHLCV) via public financial APIs.
* Pipeline execution completes in under 5 minutes daily.

## Known Unknowns / Risks
* Extreme macro regime shifts exceeding historical training parameters.
* Monitored via backtesting across stress periods (2008 Crisis, 2020 COVID crash).

## Lifecycle Mapping
| Goal | Stage | Deliverable |
| :--- | :--- | :--- |
| Define problem & stakeholder needs | Stage 01: Problem Framing | `README.md` & Stakeholder Memo |

## Repo Plan
`data/`, `src/`, `notebooks/`, `docs/`
