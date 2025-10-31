import yfinance as yf
import pandas as pd

# Download data from Jan 2020 to Oct 2025
tata = yf.download("TATAMOTORS.NS", start="2020-01-01", end="2025-10-31")

# Save locally
tata.to_csv("data/tatamotors.csv")

tata.head()


import numpy as np

# Daily percentage return
tata['Daily Return (%)'] = tata['Adj Close'].pct_change() * 100

# Log return
tata['Log Return'] = np.log(tata['Adj Close'] / tata['Adj Close'].shift(1))

tata[['Adj Close', 'Daily Return (%)', 'Log Return']].head()


import matplotlib.pyplot as plt

plt.figure(figsize=(12,6))
plt.plot(tata['Adj Close'], label='Tata Motors Closing Price', color='blue')
plt.title('Tata Motors Stock Price (2020–2025)')
plt.xlabel('Date')
plt.ylabel('Price (INR)')
plt.legend()
plt.show()

# Daily return plot
plt.figure(figsize=(12,6))
plt.plot(tata['Daily Return (%)'], color='orange')
plt.title('Daily Returns of Tata Motors')
plt.xlabel('Date')
plt.ylabel('Daily Return (%)')
plt.show()

# Rolling volatility (30-day standard deviation)
tata['Rolling Volatility'] = tata['Daily Return (%)'].rolling(window=30).std()

plt.figure(figsize=(12,6))
plt.plot(tata['Rolling Volatility'], color='red')
plt.title('30-Day Rolling Volatility (Tata Motors)')
plt.xlabel('Date')
plt.ylabel('Volatility (%)')
plt.show()


tata['Year'] = tata.index.year
annual_returns = tata.groupby('Year')['Daily Return (%)'].mean().round(2)
print(annual_returns)

tata['Cumulative Return'] = (1 + tata['Daily Return (%)']/100).cumprod()

plt.figure(figsize=(12,6))
plt.plot(tata['Cumulative Return'], color='green')
plt.title('Cumulative Return of Tata Motors (Base ₹100 in 2020)')
plt.xlabel('Date')
plt.ylabel('Growth Factor')
plt.show()

summary = tata[['Daily Return (%)', 'Log Return']].describe().T
print(summary)

nifty = yf.download("^NSEI", start="2020-01-01", end="2025-10-31")
nifty['Return'] = nifty['Adj Close'].pct_change()

# Merge and compute correlation
merged = pd.merge(tata['Daily Return (%)'], nifty['Return'], left_index=True, right_index=True, how='inner')
merged.columns = ['Tata Motors', 'Nifty50']

print("Correlation between Tata Motors and Nifty50:", merged.corr().iloc[0,1])

tata['MA50'] = tata['Adj Close'].rolling(50).mean()
tata['MA200'] = tata['Adj Close'].rolling(200).mean()
