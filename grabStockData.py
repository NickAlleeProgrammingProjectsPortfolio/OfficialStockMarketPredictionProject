def grabStockData(ticker):
    import yfinance as yf
    tickerGrabber = yf.Ticker(ticker)
    data = tickerGrabber.history(period = "max")
    return data