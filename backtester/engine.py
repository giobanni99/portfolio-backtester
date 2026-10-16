import pandas as pd
from backtester.portfolio import Portfolio

def run_backtest(prices, signals, starting_cash):
    p = Portfolio(starting_cash)
    for date, price in prices.items():
        crossover_signal = signals[date]
        if crossover_signal and p.shares == 0:
            p.buy(price)
        elif not crossover_signal and p.shares > 0:
            p.sell(price)
        p.record_value(price)
    return pd.Series(p.get_history(), index=prices.index)