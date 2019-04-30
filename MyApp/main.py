from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from kivy.properties import ObjectProperty


import requests
import json





class AddLocationForm(BoxLayout):
    search_input = ObjectProperty()
    price_result = ObjectProperty()
    search_results = ObjectProperty()
    
    def MyTestMethod(self):
        print("It works...maybe")
        print(self.size)

    def TheString(self):
        url = "https://api.iextrading.com/1.0/stock/"
        return url

    def Price(self, ticker):
        url = self.TheString() + str.lower(ticker) + "/price"
        price = requests.get(url).text
        #for later to return the value
        #return price
        print("The stock price: {0}".format(price))

    def UserPrice(self):
        url = self.TheString() + str.lower(self.search_input.text) + "/price"
        price = requests.get(url).text
        #for later to return the value
        #return price
        #print("The stock price: {0}".format(price))
        self.price_result.text = price


    def BestMatch(self):
        searchStock =  "https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={}&apikey=VC61"
        ticker = str.upper(self.search_input.text)
        searchUrl = searchStock.format(ticker)
        request = requests.get(searchUrl)
        response = json.loads(request.text)
        
        bm = response['bestMatches']
        stocks = ["Symbol: {0} Name: {1}".format(tickers['1. symbol'], tickers['2. name']) for tickers in bm]
        self.search_results.item_strings = stocks








class MarkoApp(App):
        pass









if __name__ == '__main__':
    MarkoApp().run()
