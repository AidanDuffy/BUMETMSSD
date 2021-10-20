import datetime
from os import environ as env
from dotenv import load_dotenv, find_dotenv
import requests
from datetime import date

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)
API_KEY = env.get("API_KEY")

RATING_GRADES = {"BUY": 25, "SELL" : -25}

url = "https://socialsentiment.io/api/v1/stocks/"

headers = {
    'Authorization': "Token " + API_KEY,
    'Accept': 'application/json'
    }

SUPPORT_STOCKS = {"AAPL":15, "PLTR":5, "GOOG":35, "COIN":20, "WMT":-30, "SQ":0}
STOCK_OBJECTS = dict()
INVESTORS = list()

yesterday = date.today() - datetime.timedelta(days=1)
yesterday_str = yesterday.strftime("%Y-%m-%d")

class Stock():

    def __init__(self, ticker, rating_initial = 0):
        self.ticker = ticker
        self.rating = rating_initial

    def updateRating(self, rating):
        current_grade = self.getRating()
        self.rating = rating
        new_grade = self.getRating()
        if current_grade != new_grade:
            if new_grade != "HOLD":
                return True
        return False

    def getTicker(self):
        return self.ticker

    def getRating(self):
        if self.rating >= RATING_GRADES["BUY"]:
            return "BUY"
        elif self.rating <= RATING_GRADES["SELL"]:
            return "SELL"
        else:
            return "HOLD"


class Investor():

    def __init__(self, name):
        self.watchlist = list()
        self.id = name

    def addToWatchlist(self, stock):
        stock_obj = STOCK_OBJECTS[stock]
        self.watchlist.append(stock_obj)

    def notifyChange(self, stock):
        if stock in self.watchlist:
            print(str(self.id) + ", the rating for " + stock.getTicker() + " has been updated to a " + stock.getRating())


def setup_stocks():
    for ticker,rating in SUPPORT_STOCKS.items():
        STOCK_OBJECTS[ticker] = Stock(ticker,rating)
    return


def setup_users():
    user1 = Investor(1)
    user1.addToWatchlist("AAPL")
    user1.addToWatchlist("PLTR")
    user2 = Investor(2)
    user2.addToWatchlist("PLTR")
    user2.addToWatchlist("SQ")
    user2.addToWatchlist("WMT")
    INVESTORS.append(user1)
    INVESTORS.append(user2)
    return


def setup():
    setup_stocks()
    setup_users()
    return

def notifyInvestors(stock):
    for i in INVESTORS:
        i.notifyChange(stock)

def example1():
    stock_str = "GOOG"
    stock = STOCK_OBJECTS[stock_str]
    response = requests.request("GET", url + stock_str + "/sentiment/daily", headers=headers)
    response = response.json()
    for i in response:
        if i['date'] == yesterday_str:
            stock.updateRating(i['score'])
    print("The current rating for the stock " + stock_str + " is a " + stock.getRating())


def example2():
    stock_str = "F"
    stock = Stock(stock_str)
    STOCK_OBJECTS[stock_str] = stock
    response = requests.request("GET", url + stock_str + "/sentiment/daily", headers=headers)
    response = response.json()
    for i in response:
        if i['date'] == yesterday_str:
            stock.updateRating(i['score'])
    print("The stock " + stock_str + " has been added and has a rating of " + stock.getRating())


def example3():
    stock_str = "SQ"
    stock = STOCK_OBJECTS[stock_str]
    response = requests.request("GET", url + stock_str + "/sentiment/daily", headers=headers)
    response = response.json()
    for i in response:
        if i['date'] == yesterday_str:
            if stock.updateRating(i['score']):
                notifyInvestors(stock)


def natlang_example():
    setup()
    #Shows a basic Query
    #example1()
    #Shows a stock being added
    example2()
    # This shows an update
    #example3()


if __name__ == '__main__':
    natlang_example()