from backtester.data import get_close_prices
import pandas as pd
prices = get_close_prices("AAPL", start="2020-01-01", end="2024-12-31")

if len(prices) == 0:
    print("No data")
else:
    first_price = prices.iloc[0]
    shares = 10000 / first_price
    total_list = []
    for date, price in prices.items():
        total = shares * price
        total_list.append(total)

total_series = pd.Series(total_list, prices.index)
print(total_series.iloc[-1])
