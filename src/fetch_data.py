import yfinance as yf
from datetime import datetime, timedelta

def get_stock_data(ticker):
    end = datetime.today()
    start = end - timedelta(days=365)  # last 1 year
    df = yf.download(ticker, start=start.strftime('%Y-%m-%d'), end=end.strftime('%Y-%m-%d'))
    df.reset_index(inplace=True)
    return df
