# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#from urllib2 import Request, urlopen
import datetime
from datetime import datetime

import matplotlib.pyplot as plt
#%matplotlib inline

import pandas as pd
import numpy as np

#pd.set_option('display.notebook_repr_html', False)
#pd.set_option('display.max_columns', 8)
#pd.set_option('display.max_rows', 8)



#gets MU3 from JSON format
mu = pd.read_json('D:\Downloads\Computer Notes\Stock App Files\MU3.json')
#puts the data into a dataframe, but with meta data
opn = pd.read_json(mu['Time Series (1min)'].to_json(), orient = 'index')
#drops the volume data
mu2 = opn.drop(['5. volume'], axis = 1)
#selects (really removes 1st 2 rows, and the last 4, keeps all columns)
mu3 = mu2.iloc[2:-4, 0:4]
#same as above, but keeps all columns, volume is included
mu4 = opn.iloc[2:-4]


#different selection process, removing metadata
opn2 = opn[[ "1. open", "2. high", "3. low", "4. close", "5. volume"]]
opn3 = opn["2017-05-30 15:53:00": "2017-05-30 16:00:00"]
#different selection process, removing metadata and volume
opn4 = opn.loc["2017-05-30 15:53:00": "2017-05-30 16:00:00", [ "1. open", "2. high", "3. low", "4. close"]]
#renames column names
opn4.columns = ['Open', 'High', 'Low', 'Close']
#creates custom numbered index
df = pd.DataFrame(np.array(opn4), columns = ['Open', 'High', 'Low', 'Close'], index = [np.arange(0,8)])
#creates dataframe of that type only
Open = pd.Series(opn3['1. open'])
High = pd.Series(opn3['2. high'])
Low = pd.Series(opn3['3. low'])
Close = pd.Series(opn3['4. close'])
#creates dataframe, but renames based on the dictionary pairing in the column
mustock = pd.DataFrame({'Open' : Open, 'High': High, 'Low': Low, 'Close': Close})


#gets a fuller dataset                  
muTemp = pd.read_json('D:\Downloads\Computer Notes\Stock App Files\mu10.json')
muFull = pd.read_json(muTemp['Time Series (1min)'].to_json(), orient = 'index')


#removes meta data rows (top & bottom) and the volume columns
muFull2 = muFull.iloc[2:-4, 0:4]
#selects data only for this part
open2 = muFull.iloc[2:-4, 0]
high2 = muFull.iloc[2:-4, 1]
low2 = muFull.iloc[2:-4, 2]
close2 = muFull.iloc[2:-4, 3]



#2 different syntaxes for cleaning data
stocks = muFull.loc["2017-08-24 09:30:00" : "2017-09-07 16:00:00", ["1. open", "2. high", "3. low", "4. close"]]
stocks = muFull.loc["2017-08-24 09:30:00" : "2017-09-07 16:00:00", "1. open" : "4. close"]
#renaming the columns using the dictionary pairing in the column
stocks = stocks.rename(columns = {'1. open' : 'Open', '2. high' : 'High', '3. low':'Low', '4. close': 'Close'})
#gets and prints the column names
cols = stocks.columns
print(cols[0])
print(stocks[cols[0]])

#multiple selection example
volume = muFull["2017-08-24 09:30:00" : "2017-09-07 16:00:00"][["4. close" ,"5. volume"]]
#drop close and keep only the volume
volume2 = volume.drop(['4. close'], axis=1)

#WithOut VOLume
wovol = muFull.copy()
#removes the volume column
wovol.pop('5. volume')
#drops some of the metadata
wovol.drop(['1. Information', '2. Symbol'], axis = 0, inplace=True)
#dropping a number of indexes based on the last for, a range of them
wovol2 = wovol.drop(wovol.index[-4:], axis = 0)
#gets only the close column
close = muFull["2017-08-24 09:30:00" : "2017-09-07 16:00:00"][[ "4. close"]]

#selection example syntaxes
stocks.loc["2017-08-24 09:30:00" : "2017-08-24 10:33:00"]
#just selects 2 data points
stocks.iloc[[0,200]]
#copying the data
copy = stocks.copy()
#inserts copy into the 2nd spot
copy.insert(1, 'Volume', volume2)

stocks2 = stocks.copy()
#adds back in volume
stocks2['5. volume'] = volume2
#adds back in volume
stocks3 = pd.concat([stocks, volume2], axis=1)
#resets the index
times = stocks3.reset_index()
#???
stocks3.set_index('Open')

#writes to excel
stocks3.to_excel('D:\mu.xlsx', sheet_name='MU')
#reads from an excel file
excel = pd.read_excel('D:\mu.xlsx')

#pandas-datareader must be installed via Anaconda
pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader.data as web
import pandas.io.data as web

#creates 2 datetimes
start = datetime(2012, 1, 1)
end = datetime(2014, 1, 27)

#write to excel file, all 3 lines of code are needed
writer = pd.ExcelWriter('D:\mufull.xlsx')
stocks.to_excel(writer,'Sheet1')
writer.save()




#gives us
    #count
    #mean
    #std
    #25%
    #50%
    #75%
    #max
#for each column
stocks3.describe()

#date time chapter

#sets 2014-15-15 17:30:00
print(datetime(2014, 12, 15, 17, 30))
#date and time (down to the millisecond) right now
print(datetime.now())
#2014-12-15
print(datetime.date(datetime(2014, 12, 15)))
#date only right now
print(datetime.now().date())
#date and time from a timestamp
print(pd.Timestamp('2018-7-11 11:38'))
#date and time now, but different syntax
print(pd.Timestamp('now'))

date1 = datetime(2018, 7, 11)
date2 = datetime(2010, 7, 11)
#difference in days
print(date1 - date2)

#creates a list of different dates
dates=[datetime(2014,8,1), datetime(2014,8,2)]

#syntax for creating a dataframe of times
periods = pd.date_range('8/1/2014 09:30:00', periods=100, freq='1min')
periods = pd.date_range(start = '1/1/2014 09:30:00', end = '1/1/2014 16:00:00', freq='1min')

#every minute of the timeseries
stockday = pd.date_range(start='09:30:00', periods=391, freq='T')

#selection of the dataframe, 15 minute selection, based on index
stocks['2017-08-24 09:30:00': '2017-08-24 09:45:00']
#1 point slection, based on ndex
stocks.loc['2017-08-24 09:30:00']
#prints the monthly points
print(pd.period_range('1/1/2013', '12/31/2013', freq = 'M'))


#import time series holiday schedule
from pandas.tseries.holiday import *
#gets the US Federal Holiday Calendar
cal = USFederalHolidayCalendar()
for d in cal.holidays(start='2014-01-01', end='2014-12-31'):
    print(d)


#gets timezones
from pytz import common_timezones
#to call time zones
print(common_timezones[:])
periods = 31 * 24
#sets a Series object for 2 hour intervals, and assigins a value (periods)
hourly = Series(np.arange(0, periods), pd.date_range('08-01-2014', freq='2H', periods = periods))
print(hourly)
#changes the value to hourly now and assigins values from periods
daily = hourly.asfreq('H')
print(daily)

#only selects open all
opnall = stocks.drop(["High", "Low", "Close"], axis = 1)
#plots data
opnall.rolling(100).mean().plot()
opnall.plot()


#graphing chapter
import numpy as np
import pandas as pd
import datetime
from datetime import datetime
seedval = 111111
import matplotlib as mpl
import matplotlib.pyplot as plt
#%matplotlib inline

#creates and graphs a random seed value
np.random.seed(seedval)
s = pd.Series(np.random.randn(1096), index = pd.date_range('2012-01-01', '2014-12-31'))
walk_ts = s.cumsum()
walk_ts.plot();

#graphs the data, but uses different line types and colors
stocks.plot(style=['r-', 'g--', 'b:', 'm-.'])
labels = plt.xticks()

#sets the bins size and graphs a histograph
mu3.hist(bins=100);
#histograph for just open
opnall.hist();
#histrograph for 4 columns, therefore 4 graphs
stocks.hist();


#graphs 4 graphs on top of each other with some transparency
#Open, High, Low, Close ==> var2 is for the full set
plt.hist(open2, alpha = 0.25)
plt.hist(high2, alpha = 0.25)
plt.hist(low2, alpha = 0.25)
plt.hist(close2, alpha = 0.25)

#boxplots for different dataframes
mu3.boxplot();
opnall.boxplot();
stocks.boxplot();

#stacked graphing
open2.plot(kind='area', stacked = False);
high2.plot(kind='area', stacked = False);
low2.plot(kind='area', stacked = False);
close2.plot(kind='area', stacked = False);

#scatter plot, attempting to see any correlation between Open and Close
stocks.plot(kind='scatter', x='Open', y='Close');


#scatter matrix graphs, the correlation and matrixes type
from pandas.plotting import scatter_matrix
scatter_matrix(stocks, alpha = 0.2, figsize=(6,6), diagonal='kde');



#graphs a volume and line graph (based on a subsection of data)
#labels the graph properly
#saves to PNG file
stocks4 = stocks2.iloc[0:100]
top = plt.subplot2grid((4,4), (0,0), rowspan = 3, colspan = 4)
top.plot(stocks4.index, stocks4['Open'], stocks4['High'], label = 'Close')
top.plot(stocks4.index, stocks4['Low'], stocks4['Close'], label = 'Close')
top.legend(['Open', 'High', 'Low', 'Close'], loc = 'lower left')
plt.title("MU Price Movement")
plt.tick_params(axis = 'x', which = 'both', bottom = False, labelbottom = False)
bottom = plt.subplot2grid((4,4), (3,0), rowspan = 1, colspan = 4)
bottom.bar(stocks4.index, stocks4['5. volume'])			
plt.title("MU Trading Volume")
plt.tick_params(axis = 'x', which = 'both', bottom = False, labelbottom = False)
plt.gcf().set_size_inches(15,8)
plt.savefig('D:\mu.png')


#another example of the above
top = plt.subplot2grid((4,4), (0,0), rowspan = 3, colspan = 4)
top.plot(mu4.index, mu4['4. close'], label = 'Close')
plt.tick_params(axis = 'x', which = 'both', bottom = False, labelbottom = False)
bottom = plt.subplot2grid((4,4), (3,0), rowspan = 1, colspan = 4)
bottom.bar(mu4.index, mu4['5. volume'])
plt.tick_params(axis = 'x', which = 'both', bottom = False, labelbottom = False)
plt.gcf().set_size_inches(15,8);


#plots a rolling mean, but useless with such a small dataset
mu5 = mu4.drop(['1. open', '2. high', '3. low', '5. volume'], axis = 1)
vol = mu5.rolling(4).std() * np.sqrt(4)
vol.plot()


#plots a rolling standard deviation
stocks5 = stocks.drop(['Open', 'High', 'Low'], axis = 1)
vol2 = stocks5.rolling(100).std() * np.sqrt(100)
vol2.plot()






#cannot get this to work in Windows, try Linux

#need to import plotly via Anaconda
import plotly.plotly as py
from plotly.tools import FigureFactory as FF
pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader.data as web
#import pandas.io.data as web



#duplicate selection code just to ensure correct selection of the data
muTemp = pd.read_json('D:\Downloads\Computer Notes\Stock App Files\mu10.json')
muFull = pd.read_json(muTemp['Time Series (1min)'].to_json(), orient = 'index')
stocks = muFull.loc["2017-08-24 09:30:00" : "2017-09-07 16:00:00", ["1. open", "2. high", "3. low", "4. close"]]
stocks = muFull.loc["2017-08-24 09:30:00" : "2017-09-07 16:00:00", "1. open" : "4. close"]
#stocks.plot()
#creates a graph via plotly, but need to provide account information
fig  = FF.create_candlestick(muFull["1. open"], muFull["2. high"], muFull["3. low"], muFull["4. close"], dates=muFull.index)
py.plot(fig, filename = 'basic-line', auto_open=True)    