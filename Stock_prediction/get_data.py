import yfinance as yf
import pandas as pd
import pickle
from tqdm import tqdm

def get_top_stocks():
    tickers = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0]['Symbol'].values.tolist()
    return tickers

def get_stock_data(ticker):
    stock = yf.Ticker(ticker)
    data = stock.history(period="max")
    return data

top_stocks = get_top_stocks()

data = {}
for ticker in tqdm(top_stocks):
    data[ticker] = get_stock_data(ticker)

with open("data.pickle", "wb") as file:
    pickle.dump(data, file)