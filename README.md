<div align="center">

# 📈 Market Signal Engine

**A transparent, rule-based engine that scans price data and explains every signal it produces.**

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)
![Dependencies](https://img.shields.io/badge/Dependencies-zero-success?style=flat-square)
![Explainable](https://img.shields.io/badge/Signals-100%25%20explainable-00D9FF?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

</div>

---

## ✨ Why

Most trading bots are black boxes. This engine does the opposite: **every signal comes with the exact reason behind it**, so a human can always understand — and challenge — the decision.

## 🧠 What it computes

| Indicator | What it tells you |
|---|---|
| **SMA 20 / SMA 50** | Short-term vs long-term trend — a crossover hints at a trend change |
| **RSI 14** | Momentum — above 70 is "overbought", below 30 is "oversold" |
| **Combined signal** | `BULLISH`, `BEARISH` or `NEUTRAL`, with a plain-language explanation |

## 🚀 Quick start

```bash
git clone https://github.com/toureabdoul2050-alt/market-signal-engine.git
cd market-signal-engine
python signals.py prices.csv
```

`prices.csv` needs two columns, oldest row first:

```csv
date,close
2026-01-02,101.25
2026-01-03,102.10
```

Works with any asset that has a daily close: stocks, ETFs, crypto, currencies.

## 🧾 Example output

```
Signal: BULLISH
- SMA20 (108.4) is above SMA50 (104.9): short-term trend is up.
- RSI14 is 61.2: momentum is positive but not overbought.
```

## 🗺 Roadmap

- [x] SMA + RSI signals with explanations
- [ ] Multi-asset watchlist scan
- [ ] Backtesting module
- [ ] Optional LLM summary of the day's signals

## ⚠️ Disclaimer

This project is for **education and research only**. It is **not financial advice**. Markets are risky; never trade money you cannot afford to lose.

---

<div align="center">Built by <a href="https://github.com/toureabdoul2050-alt">Ladji Touré</a> · MIT License</div>
