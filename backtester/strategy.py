def crossover_strategy(prices, short_window=50, long_window=200):
    """
    A simple moving average crossover strategy.



    Parameters
    ----------
    prices : pd.Series
        The historical price data.
    short_window : int
        The window size for the short-term moving average.
    long_window : int
        The window size for the long-term moving average.

    Returns
    -------
    pd.Series
        A series of signals where A series of booleans where True means the strategy should be
        holding the asset and False means it should be in cash.
        Trades occur only where this value changes.
    
    Notes
        The first long_window - 1 values are False because the long
        moving average is undefined until enough history exists.
        Assumes short_window < long_window.
    """
    short = prices.rolling(window=short_window).mean()
    long = prices.rolling(window=long_window).mean()

    return short > long