from backtester.data import get_close_prices
from backtester.engine import run_backtest
from backtester.metrics import sharpe_ratio, total_return, max_drawdown
from backtester.strategy import crossover_strategy
from backtester.portfolio import Portfolio
import pandas as pd
prices = get_close_prices("AAPL", start="2020-01-01", end="2024-12-31")
STARTING_CASH = 10000

#Find out how much money we will have in 2024 when buying $10,000 shares in 2020.
if len(prices) == 0:
    print("No data")
else:
    xo_curve = run_backtest(prices, crossover_strategy(prices), STARTING_CASH)
    bh_curve = run_backtest(prices, pd.Series(True, index=prices.index), STARTING_CASH)

print("Buy & Hold")
print(f"  Final value: ${bh_curve.iloc[-1]:,.2f}")
print(f"  Total return: {total_return(bh_curve):.2f}%")
print(f"  Max drawdown: {max_drawdown(bh_curve):.2f}%")
print(f"  Sharpe ratio: {sharpe_ratio(bh_curve):.2f}")

print("50/200 Crossover")
print(f"  Final value: ${xo_curve.iloc[-1]:,.2f}")
print(f"  Total return: {total_return(xo_curve):.2f}%") 
print(f"  Max drawdown: {max_drawdown(xo_curve):.2f}%")
print(f"  Sharpe ratio: {sharpe_ratio(xo_curve):.2f}")
