"""Market Signal Engine — explainable SMA + RSI signals from a CSV of daily closes.

Usage:
    python signals.py prices.csv

Education and research only. Not financial advice.
"""
import csv
import sys


def load_closes(path: str) -> list:
    with open(path, newline="", encoding="utf-8") as f:
        return [float(row["close"]) for row in csv.DictReader(f)]


def sma(values: list, period: int) -> float:
    return sum(values[-period:]) / period


def rsi(values: list, period: int = 14) -> float:
    changes = [b - a for a, b in zip(values[-period - 1:-1], values[-period:])]
    gains = sum(c for c in changes if c > 0) / period
    losses = sum(-c for c in changes if c < 0) / period
    if losses == 0:
        return 100.0
    return 100 - 100 / (1 + gains / losses)


def analyze(closes: list) -> tuple:
    if len(closes) < 51:
        raise ValueError("Need at least 51 daily closes.")
    fast, slow, momentum = sma(closes, 20), sma(closes, 50), rsi(closes)
    reasons, points = [], 0

    if fast > slow:
        points += 1
        reasons.append(f"SMA20 ({fast:.1f}) is above SMA50 ({slow:.1f}): short-term trend is up.")
    else:
        points -= 1
        reasons.append(f"SMA20 ({fast:.1f}) is below SMA50 ({slow:.1f}): short-term trend is down.")

    if momentum > 70:
        points -= 1
        reasons.append(f"RSI14 is {momentum:.1f}: overbought, a pullback is possible.")
    elif momentum < 30:
        points += 1
        reasons.append(f"RSI14 is {momentum:.1f}: oversold, a rebound is possible.")
    else:
        points += 1 if momentum >= 50 else -1
        side = "positive" if momentum >= 50 else "negative"
        reasons.append(f"RSI14 is {momentum:.1f}: momentum is {side} but not extreme.")

    signal = "BULLISH" if points >= 2 else "BEARISH" if points <= -2 else "NEUTRAL"
    return signal, reasons


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    signal, reasons = analyze(load_closes(sys.argv[1]))
    print(f"Signal: {signal}")
    for reason in reasons:
        print(f"- {reason}")
    print("\nEducation and research only. Not financial advice.")
