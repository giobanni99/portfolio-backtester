from backtester.data import get_close_prices
from backtester.portfolio import Portfolio
import pandas as pd
prices = get_close_prices("AAPL", start="2020-01-01", end="2024-12-31")
STARTING_CASH = 10000
p = Portfolio(STARTING_CASH)
#Find out how much money we will have in 2024 when buying $10,000 shares in 2020.
if len(prices) == 0:
    print("No data")
else:
    for date, price in prices.items():
        if p.shares == 0:
            p.buy(price)
        p.record_value(price)

total_series = pd.Series(p.history, index=prices.index)
print(f"${total_series.iloc[-1]:,.2f}")