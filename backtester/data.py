import yfinance as yf

#Create function for getting close prices
def get_close_prices(ticker: str, start: str, end: str):
    stock = yf.Ticker(ticker)
    hist = stock.history(start= start, end= end)
    close = hist["Close"]
    return close

print(get_close_prices("AAPL", start="2020-01-01", end="2024-12-31"))