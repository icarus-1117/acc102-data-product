#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Run notebook code with simulated data"""

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

print("=" * 60)
print("Stock Risk and Return Analysis")
print("=" * 60)

# Cell 1: Imports (already done above)
print("\n[Cell 1] Imports completed")

# Cell 2: Download stock data (using simulated data due to rate limit)
print("\n[Cell 2] Creating simulated stock data...")
stocks = ['AAPL', 'MSFT', 'TSLA']
start = '2020-01-01'
end = '2025-01-01'

np.random.seed(42)
dates = pd.date_range(start=start, end=end, freq='B')
initial_prices = {'AAPL': 75, 'MSFT': 160, 'TSLA': 28}

data = pd.DataFrame(index=dates)
for stock in stocks:
    if stock == 'AAPL':
        returns = np.random.normal(0.0008, 0.018, len(dates))
    elif stock == 'MSFT':
        returns = np.random.normal(0.0006, 0.015, len(dates))
    else:
        returns = np.random.normal(0.0012, 0.035, len(dates))
    price = initial_prices[stock] * np.exp(np.cumsum(returns))
    data[stock] = price

print(data.head())

# Cell 3: Calculate returns
print("\n[Cell 3] Calculating daily returns...")
returns = data.pct_change().dropna()
print(returns.isnull().sum())

# Cell 4: Summary
print("\n[Cell 4] Calculating annualized metrics...")
mean_returns = returns.mean() * 252
risk = returns.std() * np.sqrt(252)

summary = pd.DataFrame({
    'Annual Return': mean_returns,
    'Risk': risk
})
print(summary)

# Cell 5: Plot 1
print("\n[Cell 5] Creating stock price trends chart...")
plt.figure(figsize=(10, 6))
for stock in stocks:
    plt.plot(data.index, data[stock], label=stock, linewidth=2)
plt.title('Stock Price Trends', fontsize=14, fontweight='bold')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('C:/Users/james/Desktop/notebook_plot1.png', dpi=150)
print("Saved: notebook_plot1.png")
plt.close()

# Cell 6: Plot 2
print("\n[Cell 6] Creating risk-return tradeoff chart...")
plt.figure(figsize=(8, 6))
for stock in stocks:
    plt.scatter(risk[stock], mean_returns[stock], s=100)
    plt.text(risk[stock], mean_returns[stock], stock, fontsize=12, ha='center')
plt.xlabel('Risk')
plt.ylabel('Return')
plt.title('Risk Return Tradeoff', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('C:/Users/james/Desktop/notebook_plot2.png', dpi=150)
print("Saved: notebook_plot2.png")
plt.close()

# Cell 7: Correlation
print("\n[Cell 7] Correlation matrix:")
corr = returns.corr()
print(corr)

print("\n" + "=" * 60)
print("All cells executed successfully!")
print("=" * 60)
