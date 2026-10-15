def total_return(equity_curve):
    """
    Calculate the total return of an equity curve.

    Assumes a non-empty curve with a nonzero starting value.

    Parameters
    ----------
    equity_curve : pd.Series
        The equity curve of the strategy.

    Returns
    -------
    float
        The total return of the strategy as a percentage (e.g. 246.45 means 246.45% growth).
    """
    return ((equity_curve.iloc[-1] - equity_curve.iloc[0]) / equity_curve.iloc[0]) * 100

def max_drawdown(equity_curve):
    """
    Calculate the maximum drawdown of an equity curve.

    Assumes a non-empty curve with a nonzero starting value.

    Parameters
    ----------
    equity_curve : pd.Series
        The equity curve of the strategy.

    Returns
    -------
    float
        The maximum drawdown of the strategy as a percentage (e.g. -27.3 means a 27.3% peak-to-trough decline).
    """
    peak = equity_curve.cummax()
    drawdown = (equity_curve - peak) / peak
    return drawdown.min() * 100

def sharpe_ratio(equity_curve):
    """
    Calculate the Sharpe ratio of an equity curve.

    Assumes a non-empty curve with a nonzero starting value.

    Risk-free rate is assumed to be 0 for simplicity.

    Parameters
    ----------
    equity_curve : pd.Series
        The equity curve of the strategy.

    Returns
    -------
    float
        The Sharpe ratio of the strategy.
    """
    returns = equity_curve.pct_change()
    return (returns.mean() / returns.std()) * (252 ** 0.5)  # Annualized Sharpe ratio