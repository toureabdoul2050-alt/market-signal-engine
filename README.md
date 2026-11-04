# market-signal-engine

Reads a CSV of daily closing prices and prints a BULLISH, BEARISH or NEUTRAL signal, along with the reasons behind it. I wanted something where every output can be checked by hand, so there is no machine learning here, only two classic indicators:

- **SMA 20 vs SMA 50** for the trend
- **RSI 14** for momentum (above 70 overbought, below 30 oversold)

No dependencies, standard library only.

## Usage

```bash
python signals.py prices.csv
```

The CSV needs at least 51 rows, oldest first:

```csv
date,close
2026-01-02,101.25
2026-01-03,102.10
```

Example output:

```
Signal: BULLISH
- SMA20 (108.4) is above SMA50 (104.9): short-term trend is up.
- RSI14 is 61.2: momentum is positive but not extreme.
```

## Ideas for later

- Scan a whole watchlist at once
- A simple backtest

## Disclaimer

For learning and research only. This is not financial advice.

## License

MIT
