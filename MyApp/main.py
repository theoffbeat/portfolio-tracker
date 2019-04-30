from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from kivy.properties import ObjectProperty


import requests





class AddLocationForm(BoxLayout):
    seach_input = ObjectProperty()
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
        self.search_results.text = price






class MarkoApp(App):
    def test(self):
        pass









if __name__ == '__main__':
    MarkoApp().run()
