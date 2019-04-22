# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import urllib.request
import json
import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
from datetime import date
import datetime
import requests

#ticker = 'MU'
#stockUrl = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=' \
#    + ticker + '&interval=1min&outputsize=full&apikey=VC61'
#website = urllib.request.urlopen(stockUrl)
#
#jsonFile = website.read()
#
#path = r"D:\mu.json"
#
#file = open(path, "w+")
#
#file.write(jsonFile)
#
#
#myJson = pd.read_json(stockUrl)
#stock = pd.read_json(myJson['Time Series (1min)'].to_json(), orient = 'index')



#best match code
import requests
class test:
    def search_location(self, ticker):
        searchStock =  "https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={}&apikey=VC61"
        searchUrl = searchStock.format(ticker)
        request = requests.get(searchUrl)
        return request
    
    def best_match(self):
        hold = self.search_location("BAC")
    
        response = json.loads(hold.text)
        
        bm = response['bestMatches']
    
        stocks = ["Symbol: {0} Name: {1}".format(ticker['1. symbol'], ticker['2. name']) for ticker in bm]
        print("\n".join(stocks))


t = test()
print(t.best_match())


#Global quote
quote = "https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={}&apikey=VC61"
endQuote = quote.format("BAC")
requestQuote = requests.get(endQuote)
quoteData = json.loads(requestQuote.text)
print(quoteData["Global Quote"]["09. change"])
type(quoteData["Global Quote"]["09. change"])

quoteData["Global Quote"]["09. change"]



import collections
orderedData = collections.OrderedDict(sorted(quoteData.items()))



for k, v in orderedData["Global Quote"].items():
    print("{}\t\t\t{}".format(k,v))
    




#Gets the website must insert the ticker
def GetTickerIntraDay(ticker):   
    stockUrl = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=' \
    + str(ticker.upper()) + '&interval=1min&outputsize=full&apikey=VC61'
    return stockUrl

#Gets the website, ticker input is in the function
def GetTickerInputIntraDay():
    print("Enter in the ticker: ")
    user = input()
    stockUrl = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=' \
    + user.upper() + '&interval=1min&outputsize=full&apikey=VC61'
    return stockUrl

#Gets the website, ticker input is in the function
def GetTickerInputDaily():
    print("Enter in the ticker: ")
    user = input()
    stockUrl = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' \
    + user.upper() + '&outputsize=full&apikey=VC61'
    #https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&outputsize=full&apikey=demo
    return stockUrl

def GetTickerDaily(ticker):
    stockUrl = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' \
    + ticker.upper() + '&outputsize=full&apikey=VC61'
    return stockUrl

def GetTickerDailyAdjusted(ticker):
    stockUrl = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=' \
    + ticker.upper() + '&outputsize=full&apikey=VC61'
    return stockUrl

#Gets the data and removes the meta data for IntraDay
def CleanJsonIntraDay(ticker):
    jsonFile = pd.read_json(ticker)
    stock = pd.read_json(jsonFile['Time Series (1min)'].to_json(), orient = 'index')
    metaData = ["1. Information", "2. Symbol", "3. Last Refreshed", "4. Interval", "5. Output Size", "6. Time Zone"]
    for item in metaData:
        stock.drop(item, axis = 0, inplace = True)
    return stock

#Gets the data and removes the meta data for Daily
def CleanJsonDaily(ticker):
    jsonFile = pd.read_json(ticker)
    stock = pd.read_json(jsonFile['Time Series (Daily)'].to_json(), orient = 'index')
    metaData = ["1. Information", "2. Symbol", "3. Last Refreshed", "4. Output Size", "5. Time Zone"]
    for item in metaData:
        stock.drop(item, axis = 0, inplace = True)
    return stock

def CleanJsonDailyAdjusted(ticker):
    jsonFile = pd.read_json(ticker)
    stock = pd.read_json(jsonFile['Time Series (Daily)'].to_json(), orient = 'index')
    metaData = ["1. Information", "2. Symbol", "3. Last Refreshed", "4. Output Size", "5. Time Zone"]
    for item in metaData:
        stock.drop(item, axis = 0, inplace = True)
    return stock

#Saves the json the a location parameter
def SaveJson(data, path):
    #data.to_json(path) #OHLC becomes the index
    data.to_json(path, orient='index')
    
def SJ(data, path):
    data = pd.DataFrame(data)    
    f = open(path, 'w')
    out = data.to_json(path)
    with open(path, 'w') as f:
        f.write(out)
    f.flush()
    f.close()
    
def ReadJson(path):
    stock = pd.read_json(path, orient = 'index') #to remove OHLC as index
    #stock = pd.read_json(path)
    return stock



#the different stock accounts
accountCMAStocks = ['AIG', 'BAC', 'GECC', 'LXP', 'MU', 'NYMT', 'OCSL', 'PSEC']
accountIRAStocks = ['ARR', 'DNP', 'F', 'FNMA']
accountROTHStocks = ['DLTNX', 'GPMT', 'TWO']

#The path to save
path = r'D:\mu.json'
path2 = r'D:\mu2.json'

#my purchase price
purchaseMU = 9.89
#download MU stock price
dataMU = CleanJsonDaily(GetTickerDaily(accountCMAStocks[4]))
#the close price, notice selection syntax
closeAug31MU = dataMU.at["2018-08-31", "4. close"]

def SlicingData(dataframe, entryDate, EndOrCurrentDate):
    newDataFrame = pd.DataFrame(dataframe.loc[entryDate : EndOrCurrentDate])
    return newDataFrame

#Slicing data test
myMU = SlicingData(dataMU, '2013-03-26', '2018-11-06')

#doesn't seem to work, recheck
from sqlalchemy import create_engine
engine = create_engine('sqlite:///D:\stocksTest.db')
connection = engine.connect()
dataMU.to_sql('MU', con=connection)
engine.execute("SELECT * FROM mu").fetchall()
connection.close()

#Candlestick OHLC from Mastering Pandas Packt Publisihing
import datetime
import matplotlib.dates as mdates

#graphing section
#setups the date into its own column
#creates a copy of the dataMU for simpler graphing
dataMU2 = dataMU[1:100]
#creates a copy of myMU data
subset = myMU.copy()
#creates a date column setting to date from another DF instance
subset['Date'] = myMU.index
#moves the data index into its own column
subset.reset_index(inplace=True)
#drops the index named column
subset.drop(['index'], axis=1, inplace=True)

#creates new column, dateNum, as a number from date
subset['dateNum'] = pd.to_datetime(subset['Date'])
#creates a number from the date
subset['dateNum'] = subset['dateNum'].apply(lambda date: mdates.date2num(date.to_pydatetime()))


subsetAsTuples = [tuple(x) for x in subset[['dateNum', '1. open', '2. high', '3. low', '4. close']].values]

#graph based on months
from matplotlib.dates import DateFormatter
#monthFormatter = DateFormatter('%b %d')
import matplotlib.dates as mdates
yearFormatter = DateFormatter('%b %Y')

#months = mdates.MonthLocator()
years = mdates.YearLocator()
#plt.figure(figsize=(24,16), dpi=120)
fig, ax = plt.subplots(figsize=(24,16), dpi=50)
#ax = fig.add_subplot()
#ax.xaxis.set_major_locator(months)
ax.xaxis.set_major_locator(years)
#ax.xaxis.set_major_formatter(monthFormatter)
ax.xaxis.set_major_formatter(yearFormatter)



#from matplotlib.finance import candlestick_ohlc
import mpl_finance as mpf
mpf.candlestick_ohlc(ax, subsetAsTuples, width=0.6, colorup='g', colordown='r')

#plt.tick_params(axis = 'x', which = 'both', bottom = False, labelbottom = False)

plt.tick_params(axis = 'x')
plt.grid(b=None, which='major', axis='both')
#plt.grid(b=None, which='major', axis='x')

plt.xticks(rotation=90)
plt.title("MU", size=24)
plt.ylabel('Stock Price', size=20)
plt.xlabel('Date', size=20)
plt.savefig('D:\mu2.png')
plt.show()


#year
from matplotlib.dates import DateFormatter
yearFormatter = DateFormatter('%b %Y')
from matplotlib.dates import YearLocator
years = mdates.YearLocator()
plt.figure(figsize=(24,16), dpi=120)
#ax = fig.add_subplot()
fig, ax = plt.subplots()
ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(yearFormatter)
from matplotlib.finance import candlestick_ohlc
import mpl_finance as mpf
mpf.candlestick_ohlc(ax, subsetAsTuples, width=0.6, colorup='g', colordown='r')


#from packt publishing, used as an example
from matplotlib.dates import DateFormatter
weekFormatter = DateFormatter('%b %d')

from matplotlib.dates import (WeekdayLocator, MONDAY)
mondays = WeekdayLocator(MONDAY)

plt.figure(figsize=(12,8))
fig, ax = plt.subplots()
ax.xaxis.set_major_locator(mondays)
ax.xaxis.set_major_formatter(weekFormatter)
#from matplotlib.finance import candlestick_ohlc
import mpl_finance as mpf
mpf.candlestick_ohlc(ax, subsetAsTuples, width=0.6, colorup='g', colordown='r')






#Candlestick graph with volume
topGraph = plt.subplot2grid((4,4), (0,0), rowspan=3, colspan=4)
topGraph.plot(myMU.index, myMU['1. open'], myMU['2. high'], label = 'Close')
topGraph.plot(myMU.index, myMU['3. low'], myMU['4. close'], label = 'Close')
topGraph.legend(['Open', 'High', 'Low', 'Close'], loc = 'lower left')
plt.title("MU Price Ownership")
plt.tick_params(axis='x', which='both', bottom=False, labelbottom=False)
bottomGraph = plt.subplot2grid((4,4), (3,0), rowspan=1, colspan=4)
bottomGraph.bar(myMU.index, myMU['5. volume'])
plt.title("MU Trading Volume")
plt.tick_params(axis = 'x', which = 'both', bottom = False, labelbottom = False)
plt.gcf().set_size_inches(15,8)
plt.savefig('D:\mu.png')






















#the close module

yesterday = (datetime.date.today() - datetime.timedelta(1))
closeYesterday = dataMU.at[str(yesterday), "4. close"]


print("{0}".format((closeYesterday - purchaseMU) * 100))

#indexes
#DOW DJI
dataDOW = CleanJsonDaily(GetTickerDaily('DJI'))
#NASDAQ IXIC
dataNASDAQ = CleanJsonDaily(GetTickerDaily('IXIC'))
#S&P INX
dataSP500 = CleanJsonDaily(GetTickerDaily('INX'))
#Russell 2000  RUT
dataRUSSELL = CleanJsonDaily(GetTickerDaily('RUT'))

class stocks:
    def Buy(self, ticker, quantity, entryPrice, comission, year, month, day):
        return {"Ticker": ticker, "Quantity":quantity, "Entry Price":entryPrice, "Comission":comission, "Entry Date":date(year, month, day)}
    
    #Need to get yesterdays close only if its before the market close
    def YesterdayClose():
        if (datetime.datetime.hour < 16):
            yesterday = (datetime.date.today() - datetime.timedelta(1))
        else:
            pass
    
    #Gets the EOD data    
    def EODChanges():
        pass
    
    
    def returnPercentage():
        pass


#creates instance of our stock class
#CMA Account
aig = stocks()
aigInfo = aig.Buy('AIG',100, 38.10, 0, 2013, 3, 27)        
bac = stocks()
bacInfo = bac.Buy('BAC', 100, 12.3245, 0, 2013, 4, 1)    
gecc = stocks()
geccInfo = gecc.Buy('GECC', 22, 31.97, 0, 2013, 3, 25)
lxp = stocks()
lxpInfo = lxp.Buy('LXP', 100, 10.64, 0, 2013, 3, 25)        
mu = stocks()
muInfo = mu.Buy('MU', 100, 9.89, 0, 2013, 3, 26)
muInfo["Quantity"]
nymt = stocks()
nymtInfo = nymt.Buy('NYMT', 100, 5.7122, 0, 2013, 3, 26)
ocsl = stocks()
ocslInfo = ocsl.Buy('OCSL', 100, 10.8462, 0, 2013, 4, 1)
psec = stocks()
psecInfo = psec.Buy('PSEC', 100, 11.3137, 0, 2013, 3, 14)
#IRA Account
arr = stocks()
arrInfo = arr.Buy('ARR', 12, 28.92, 0, 2014, 2, 26)
dnp = stocks()
dnpInfo = dnp.Buy('DNP', 945, 9.4966, 0, 2015, 6, 30)
ford = stocks()
fordInfo = ford.Buy('F', 100, 15.64, 0, 2014, 11, 21)
fnma = stocks()
fnmaInfo = fnma.Buy('FNMA', 100, 3.6, 0, 2013, 5, 28)
#ROTH IRA Account
dltnx = stocks()
dltnxInfo = dltnx.Buy('DLTNX', 181, 10.99, 0, 2014, 11, 17)
gpmt = stocks()
gpmtInfo = gpmt.Buy('GPMT', 18, 18.78, 0, 2017, 11, 6)
two = stocks()
twoInfo = two.Buy('TWO', 100, 16.9223, 0, 2014, 2, 26)



#portfolio = [aigInfo, bacInfo, geccInfo, lxpInfo, muInfo, nymtInfo, ocslInfo, psecInfo]
#portfolio = [aigInfo, bacInfo, geccInfo, lxpInfo, muInfo, nymtInfo, ocslInfo, psecInfo, 
#             arrInfo, dnpInfo, fordInfo, fnmaInfo, 
#             dltnxInfo, gpmtInfo, twoInfo]

#had to remove dltnx, because no trades on that day, need way to check for this later
portfolio = [aigInfo, bacInfo, geccInfo, lxpInfo, muInfo, nymtInfo, ocslInfo, psecInfo, 
             arrInfo, dnpInfo, fordInfo, fnmaInfo, 
             gpmtInfo, twoInfo]





#weekends sunday
yesterdayClose = str(datetime.date.today() - datetime.timedelta(3))
todayClose = str(datetime.date.today() - datetime.timedelta(2))

#monday
yesterdayClose = str(datetime.date.today() - datetime.timedelta(2))
todayClose = str(datetime.date.today() - datetime.timedelta(1))

test = (dataMU.at[str(todayClose), '4. close']- dataMU.at[str(yesterdayClose), '4. close']) * portfolio[0]['Quantity']

#this works, however only works after close of market, not during market hours
#get my holding periods
import time
totalGain = 0
retstest = []
for index, x in enumerate(portfolio[:]):    
    dataTemp = CleanJsonDaily(GetTickerDaily(x['Ticker']))
    gainTemp = (dataTemp.at[str(todayClose), '4. close'] - dataTemp.at[str(yesterdayClose), '4. close']) * x['Quantity']
    retstest.append(gainTemp)
    totalGain += gainTemp
    
    time.sleep(20)
    print("Getting data for {0} {1} of {2} Gain: {3}".format(x['Ticker'], index+1, len(portfolio), gainTemp))

print(totalGain)
#to tell what position we are in
for index, x in enumerate(portfolio[:]):
    print("Getting data for {0} {1} of {2}".format(x['Ticker'], index+1, len(portfolio)))






dataTest = CleanJsonDaily(GetTickerDaily('DNP'))


#gets the day of week, 0 based
datetime.date.weekday(todayClose)






#gain in dollars
print("{0}".format((closeYesterday - muInfo['Entry Price']) * muInfo['Quantity']))
#gain in percentage terms
returnMU = ((closeYesterday - muInfo['Entry Price']) * muInfo['Quantity']) / (muInfo['Entry Price'] * muInfo['Quantity'])
print("{0}%".format(returnMU * 100))

def SlicingData(dataframe, entryDate, EndOrCurrentDate):
    newDataFrame = pd.DataFrame(dataframe.loc[entryDate : EndOrCurrentDate])
    return newDataFrame
#Slicing data test
myMU = SlicingData(dataMU, str(muInfo['Entry Date']), '2018-11-03')



#Checking if the market is closed, to determine when to collect data
import datetime
theTime = datetime.datetime.now()
from datetime import datetime
from pytz import timezone
#Checks it market is open/closed and allows us to determine which close to use
def CheckIfMarketIsClosed():
    #Market is still open, use previous close
    if(datetime.now(timezone('US/Eastern')).hour < 16):
        print('The market is not closed')
        print(datetime.now(timezone('US/Eastern')).hour)
        return False
    #Market is closed, use today's close
    elif(datetime.now(timezone('US/Eastern')).hour > 16):
        print('The market is closed')
        print(datetime.now(timezone('US/Eastern')).hour)
        return True
marketStatus = CheckIfMarketIsClosed()
print(marketStatus)

#Graphing the various functions
#This works, but uses a web interface of ploty
import plotly.plotly as py
from plotly.tools import FigureFactory as FF
from datetime import datetime
#import pandas.io.data as web, does not work
import pandas_datareader.data as web
plotly.tools.set_credentials_file(username='theoffbeat', api_key='NUr9b8u0BGhNpvMgjlrB')
fig = plotly.figure_factory.create_candlestick(myMU['1. open'], myMU['2. high'], myMU['3. low'], myMU['4. close'], dates=myMU.index)
py.plot(fig, filename=r'D:\muohlc')

#This also works, but not the dates on the X-Axis
import matplotlib
import mpl_finance as mpf
import matplotlib.dates as mdates

#fig, ax = plt.subplots(figsize=(8, 5))
fig, ax = plt.subplots()
mpf.candlestick2_ohlc(ax, myMU['1. open'], myMU['2. high'], myMU['3. low'], myMU['4. close'], colorup='g', colordown='r', alpha=0.75)
#ax.xaxis_date()
#ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
#plt.Axes.xaxis_date()
plt.title("MU")
plt.ylabel('Stock Price')
plt.xlabel('Date')
plt.show()

#Candlestick graph with volume
#careful might be duplicate
topGraph = plt.subplot2grid((4,4), (0,0), rowspan=3, colspan=4)
topGraph.plot(myMU.index, myMU['1. open'], myMU['2. high'], label = 'Close')
topGraph.plot(myMU.index, myMU['3. low'], myMU['4. close'], label = 'Close')
topGraph.legend(['Open', 'High', 'Low', 'Close'], loc = 'lower left')
plt.title("MU Price Ownership")
plt.tick_params(axis='x', which='both', bottom=False, labelbottom=False)
bottomGraph = plt.subplot2grid((4,4), (3,0), rowspan=1, colspan=4)
bottomGraph.bar(myMU.index, myMU['5. volume'])
plt.title("MU Trading Volume")
plt.tick_params(axis = 'x', which = 'both', bottom = False, labelbottom = False)
plt.gcf().set_size_inches(15,8)
plt.savefig('D:\mu.png')



SaveJson(dataMU, path)
dataMU = ReadJson(path)

df = ReadJson(path)
#removes 00:00:00 from datetime index
df.index = df.index.normalize()
#removes 00:00:00 from datetime index, even better
df.index = df.index.date
#graphs the close based on a time interval
dataMU = df.copy()
start = date(2013,3,26)
end = date(2018,8,31)
my = df.loc[start:end, '4. close']
my.plot()

#single column via the [] [[]], syntax
rangeMU2018 = dataMU["2018-01-01" : "2018-08-31"][["4. close"]]
rangeMU2018.plot()
#range via .loc
rangeMUOHLC = dataMU.loc["2018-01-01" : "2018-08-30", "1. high" : "4. close"]

#AIG, capital gains, divs and total gains
purchaseAIG = 38.10
dataAIG = CleanJsonDaily(GetTickerInputDaily())
closeAug28 = dataAIG.at["2018-08-28", "4. close"]
print("{0}".format((closeAug28 - purchaseAIG) * 100))

dataAIG = CleanJsonDaily(GetTickerDailyAdjusted('AIG'))
divAIG = dataAIG["2013-03-27" : '2018-08-29'][["7. dividend amount"]].sum() * 100
#the capital gains
cgAIG = (closeAug28 - purchaseAIG) * 100
#dollar amounts
print("Captial Gains: {0} Dividends: {1} Total: {2}".format(math.ceil(cgAIG), divAIG[0], cgAIG + divAIG[0]))
#percentage
print("Captial Gains: {0:.4}% Dividends: {1:.4}% Total: {2:.4}%"\
      .format(math.ceil(cgAIG) / (purchaseAIG), divAIG[0]/purchaseAIG, (cgAIG + divAIG[0]) / purchaseAIG))

#DNP, capital gains, divs and total gains
purchaseDNP = 9.497#9.4966
totalpurchaseDNP = purchaseDNP * 945
dataDNP = CleanJsonDaily(GetTickerDaily('DNP'))
#gets just the close value
closeDNP = dataDNP.drop(columns=['1. open', '2. high', '3. low', '5. volume'], axis = 1)
closeDNP.plot()

dataIntraDayDNP = CleanJsonIntraDay(GetTickerIntraDay('DNP'))
oneDay = dataIntraDayDNP.loc['2019-02-12 09:30:00' : '2019-02-12 15:59:00']
#gets just the open
oneDay2 = oneDay.iloc[:,0:1]
oneDay2.plot()

divDNP = CleanJsonDailyAdjusted(GetTickerDailyAdjusted('DNP'))
closeSep = divDNP.loc['2018-09-07', '4. close']
#gain between these 2 dates
print("{0}".format((closeAug31MU - purchaseMU) * 100))
capitalGains = (closeSep - purchaseDNP) * 945
print("{0}".format((closeSep - purchaseDNP) * 945))
#purchases of DNP
firstlot = (divDNP.loc['2015-06-30' : '2018-09-07', '7. dividend amount'].sum())*100
secondlot = (divDNP.loc['2015-08-25' : '2018-09-07', '7. dividend amount'].sum())*845
totalDivs = firstlot + secondlot
totaltoal = totalDivs + capitalGains
print("Captial Gains: {0} Dividends: {1} Total: {2}".format(math.ceil(capitalGains), totalDivs, totaltoal))
print("Captial Gains: {0:.4}% Dividends: {1:.4}% Total: {2:.4}%"\
      .format(math.ceil(capitalGains) / (totalpurchaseDNP), totalDivs/totalpurchaseDNP, totaltoal / totalpurchaseDNP))

#divs = pd.Series({'div' : np.repeat(0.065, len(retire))})
#ret.add(pd.Series({'div' : np.repeat(0.065, len(retire))}))

#some retiring data with DNP
start = '2018-09-01'
end = '2058-09-01'
#create DF with monthly timeseries
retire = pd.DataFrame(pd.date_range(start, end, freq = 'M'))
#rename the first column to Date
retire = retire.rename(columns = {0 : 'Date'})
#change the Date column into an index
retire = retire.set_index('Date')
#convert the index into a date, not datetime
retire.index = retire.index.date
#create divs column with a dividend amount
retire['divs'] = np.repeat(0.065, len(retire))
#create amount column with your monthly dividend
retire['amount'] = retire['divs'] * 945
#add the previous amount, cumulative sum
retire['total'] = retire['amount'].cumsum() + totaltoal
#plotting
retire['total'].plot()
retire.plot()


#quandl, for what its worth
import quandl
quandl.ApiConfig.api_key = 'WWKUqZdxQ2xF-fQxFLgM'
mydata = quandl.get("WIKI/AIG", start_date="2013-03-27", end_date="2018-08-29")
div = mydata["Ex-Dividend"]
div.sum() * 100



#quantiacs
import quantiacsToolbox
stock = ['AIG', 'BAC', 'MU']
listMU = quantiacsToolbox.loadData(marketList = stock, dataToLoad = ['DATE', 'OPEN', 'HIGH', 'LOW', 'CLOSE', 'VOL'], beginInSample = '20130326', endInSample = '20180830')
#close = np.ndarray.flatten(listMU['CLOSE'])

#downloads the data into a dictionary

#gets the closes of all stocks
closeAll = listMU['CLOSE'][0:]
#gets the closes of the stock #3, in this case MU
closeMUonly = listMU['CLOSE'][0:, 2]





aig = closeAll[:,0]
import numpy as np
import pandas as pd
#takes the dataframe and converts it to a series
close2 = np.ndarray.flatten(aig)
#gets the date
date2 = np.ndarray.flatten(listMU['DATE'])
#creats dataframe with date as index
ts2 = pd.DataFrame({"Close" : close2}, pd.to_datetime(date2, yearfirst=True, format='%Y%m%d'))
ts2.plot()

#gets the 'HIGH' key, all the rows, and the 3rd column
high2=listMU['HIGH'][:, 2]


date = np.ndarray.flatten(listMU['DATE'])
high = np.ndarray.flatten(listMU['HIGH'][:,2])
low = np.ndarray.flatten(listMU['LOW'][:,2])
open2 = np.ndarray.flatten(listMU['OPEN'][:,2])
close2 = np.ndarray.flatten(listMU['CLOSE'][:,2])
volume = np.ndarray.flatten(listMU['VOL'][:,2])

#dataFrameName = pd.DataFrame({'columnName1': data1, 'columnName2': data2})
#creates the dataframe
ts = pd.DataFrame({"Open": open2, "High" : high, "Low" : low, "Close" : close2, "Volume" : volume}, pd.to_datetime(date, yearfirst=True, format='%Y%m%d'))
todayValue = ts.loc['2018-08-27', 'Close']

ts.plot()

#syntax for getting simply 1 stock, Intel
stocks = ['INTC']
listStocks = quantiacsToolbox.loadData(marketList = stocks, dataToLoad = ['DATE', 'OPEN', 'HIGH', 'LOW', 'CLOSE', 'VOL'], beginInSample = '20130326', endInSample = '20180829')



#from quantopian.pipeline import Pipeline








#barchart
import ondemand

od = ondemand.OnDemandClient(api_key='cf6e893a8324a661f82c65da1a79df0a')

# or if you are using a free sandbox API

od = ondemand.OnDemandClient(api_key='cf6e893a8324a661f82c65da1a79df0a', end_point='https://marketdata.websol.barchart.com/')

# get quote data for Apple and Microsoft
quotes = od.quote('AAPL,MSFT')['results']

for q in quotes:
    print('Symbol: %s, Last Price: %s' % (q['symbol'], q['lastPrice']))

# get 1 minutes bars for Apple
resp = od.history('AAPL', 'minutes', maxRecords=50, interval=1)

# generic request by API name
resp = od.get('getQuote', symbols='AAPL,EXC', fields='bid,ask')

# or, get the crypto
resp = od.crypto('^BTCUSD,^LTCUSD')

myquotes = od.quote('MU')['results']



print(myquotes[0]['volume'])
print(dataTest.at[str(datetime.date.today()), '5. volume'])




#IEX
import json
import requests
def GetTickerIntraDay(ticker):   
    stockUrl = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=' \
    + str(ticker.upper()) + '&interval=1min&outputsize=full&apikey=VC61'
    return stockUrl
t = GetTickerIntraDay('MU')
jsonData = requests.get(t).text
type(jsonData)
response = json.loads(jsonData)
ts = response['Time Series (1min)']
for k, v in ts.items():
    print(k)    
    for key in v:
        print(key + ' : ' + v[key])
#to save
json.dump(GetTickerIntraDay('MU'))

import datetime  

#https://api.iextrading.com/1.0/stock/aapl/quote


def GetIEXDate(ticker):   
    stockUrl = 'https://api.iextrading.com/1.0/stock/' \
    + str(ticker.lower()) + '/quote'
    return stockUrl
tick = GetIEXDate('MU')

jsonData = requests.get(tick).text
response = json.loads(jsonData)

lis = ['open', 'high', 'low', 'close']

#list data
for i in lis:
    for k, v in response.items():
        if k == i:
            print("{} {}".format(k, v))


#comprehensions
ohlc = {k: response.get(k) 
        for i in lis        
        for k in response.keys()
        if i == k}

for k, v in ohlc.items():
    print("{} {}".format(k, v))

#get current price
import time
import datetime
from pytz import timezone
import requests
quotes = []

def GetCurrentPrice(ticker):
    stockUrl = 'https://api.iextrading.com/1.0/stock/' \
    + str(ticker.lower()) + '/quote'
    current = "latestPrice"
    price = []
    while datetime.datetime.now(timezone('US/Eastern')).minute <= 26:
        jsonData = requests.get(stockUrl).text
        response = json.loads(jsonData)
        quote = response[current]
        timeUS = datetime.datetime.now(timezone('US/Eastern')).strftime("%H:%M:%S")
        print("Time: {} Price: {}".format(timeUS, quote))
        time.sleep(15)
        
        price.append(quote)
        
    return price
        
    
    
#returns a nested list
#if you do go this way, might make sense to use a generator
#quotes.append(GetCurrentPrice("MU"))
quote2 = GetCurrentPrice("MU")
    

#creats a dataframe of data from IEX info
def GetTickerIntraDay(ticker):   
    stockUrl = 'https://api.iextrading.com/1.0/stock/' \
    + str(ticker.lower()) + '/chart/ytd'
    return stockUrl
tick = GetTickerIntraDay('MU')

jsonData = requests.get(tick).text
response = json.loads(jsonData)

#creates the dataframe
df = pd.DataFrame()


openLis = []
highLis = []
lowLis = []
closeLis = []
volumeLis = []
dateLis = []
timeLis = []

#gets the revelant data
for i in response:
    for k, v in i.items():
        if k == "open":
            openLis.append(v)
        if k == "high":
            highLis.append(v)
        if k == "low":
            lowLis.append(v)
        if k == "close":
            closeLis.append(v)
        if k == "volume":
            volumeLis.append(v)
        if k == "date":
            dateLis.append(v)
        ##label seems to be a problem with the dating system
        #if k == "label":
            #timeLis.append(v)

#combines the data to be more AlphaVantage Style
iexdf = pd.DataFrame(
        {"open": openLis,
         "high": highLis,
         "low": lowLis,
         "close": closeLis,
         "volume": volumeLis}, index=dateLis)
