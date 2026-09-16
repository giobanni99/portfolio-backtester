import yfinance as yf

#Create function for getting close prices
def get_close_prices(ticker: str, start: str, end: str):
    stock = yf.Ticker(ticker)
    hist = stock.history(start= start, end= end)
    close = hist["Close"]
    return close