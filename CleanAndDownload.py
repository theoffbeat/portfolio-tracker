# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 22:51:25 2018

@author: Marko
"""

import json
import requests
import pandas as pd

class GetTickers:
        
    def GetTickerIntraDay(self, ticker, intervals):   
        interval = {'one': '1min', 'five' : '5min', 'fifteen' : '15min', 'thirty' : '30min', 'sixty' : '60min'}
        #interval[intervals]
    
        stockUrl = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=' \
        + str(ticker.upper()) + '&interval=' + str(interval[intervals]) + '&outputsize=full&apikey=VC61'
        return stockUrl


    def GetTickerIntraDay1Min(self, ticker):   
        stockUrl = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=' \
        + str(ticker.upper()) + '&interval=1min&outputsize=full&apikey=VC61'
        return stockUrl


    def GetTickerDaily(self, ticker):   
        stockUrl = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' \
        + str(ticker.upper()) + '&outputsize=full&apikey=VC61'
        return stockUrl


    def GetTickerDailyAdjusted(self, ticker):   
        stockUrl = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=' \
        + str(ticker.upper()) + '&outputsize=full&apikey=VC61'
        return stockUrl


    def GetTickerWeekly(self, ticker):   
        stockUrl = 'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol=' \
        + str(ticker.upper()) + '&outputsize=full&apikey=VC61'
        return stockUrl


    def GetTickerWeeklyAdjusted(self, ticker):   
        stockUrl = 'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY_ADJUSTED&symbol=' \
        + str(ticker.upper()) + '&outputsize=full&apikey=VC61'
        return stockUrl


    def GetTickerMonthly(self, ticker):   
        stockUrl = 'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=' \
        + str(ticker.upper()) + '&outputsize=full&apikey=VC61'
        return stockUrl


    def GetTickerMonthlyAdjusted(self, ticker):   
        stockUrl = 'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY_ADJUSTED&symbol=' \
        + str(ticker.upper()) + '&outputsize=full&apikey=VC61'
        return stockUrl
    
    

        
    def GetCorrectTicker(self, series, ticker, intervals=None):
        
        timeSeries = dict(intraDay=self.GetTickerIntraDay,
                          daily=self.GetTickerDaily,
                          dailyAdjusted=self.GetTickerDailyAdjusted,
                          weekly=self.GetTickerWeekly,
                          weeklyAdjusted=self.GetTickerWeeklyAdjusted,
                          monthly=self.GetTickerMonthly,
                          monthlyAdjusted=self.GetTickerMonthlyAdjusted
                          )
        
        if (series != 'intraDay'):
            tickerString = timeSeries[series](ticker)        
        elif (series == 'intraDay'):
            tickerString = timeSeries[series](ticker, intervals)
        
        return tickerString  
    
    
    #this searchs for an axpproximate phrase and gets the index location of it
    #great for removing some variant of 'Time Series' from the data
    def SearchForPhrase(self, theCollection, phrase):
    
        if [str(phrase) in i for i in theCollection]:
            outTS = [x for x in theCollection if str(phrase) in x]
            outTS = ''.join(outTS)
            return outTS
        else:
            print('Error')
        
    def RenameColumns(self, dataframe):
        #renames the columns to open, high, low, close
        holding = {}
        for name in dataframe.columns:
            holding[name] = name[3:]
        #might need to indent this too
            for keys, values in holding.items():
                dataframe.rename(columns={keys : values}, inplace=True)

        return dataframe
    
    
    response = {}
    jsonData = ''
    #meta list is a list type
    metaList = ''
    
    #use this method to download
    #much faster than DownloadAndClean2
    def DownloadAndClean(self, series, ticker, intervals=None):
        #gets the appropriate string and puts it into a dataframe
        stock = self.GetCorrectTicker(series, ticker, intervals)
        jsonFile = pd.read_json(stock)
        #gets a list of column names
        cols = list(jsonFile.columns.values)
                
        #checks if 'Time Series' appears anywhere in the column
        #and if its does locate where
        #convert it to a regular string
        #and use that to sort the JSON to a dataframe
        outTS = self.SearchForPhrase(cols, 'Time Series')        
        stockDF2 = pd.read_json(jsonFile[outTS].to_json(), orient='index')
        
        
        #finally drops the 'Meta Data' rows by dropping NAN, because they contain NAN
        stockDF2.dropna(axis=0, inplace=True)
        
        stockDF2 = self.RenameColumns(stockDF2)
        
        
        return stockDF2
    
    def OpenHighLowCloseData(self, frame):
        ohlc = ['open', 'high', 'low', 'close']
        frame = frame[ohlc]
        return frame
    
    
    def DownloadAndCleanOHLC(self, frame):
        frame = self.OpenHighLowCloseData(frame)
        return frame
    
    
    
    
    #this is the slower verision because it downloads twice
    #once for the data
    #and again for the pandas
    def DownloadAndClean2(self, series, ticker, intervals=None):
        """
        parameters = timeSeries, ticker, intervals
        intervals defaults to None and is really used for intraday
        choices:
            intraDay,
            daily,
            dailyAdjusted,
            weekly,
            weeklyAdjusted,
            monthly,
            monthlyAdjusted
        
        intraDay choices:
            one,
            five,
            fifteen,
            thirty,
            sixty
        """
        stock = self.GetCorrectTicker(series, ticker, intervals)
        jsonData = requests.get(stock).text
        response = json.loads(jsonData)
        jsonFile = pd.read_json(stock)
                
        metaList = list(response['Meta Data'])
        cols = list(jsonFile.columns.values)
        if any('Time Series' in x for x in cols):
            stockDF = pd.read_json(jsonFile[cols[1]].to_json(), orient='index')
        for item in metaList:
            stockDF.drop(item, axis=0, inplace=True)
        return stockDF
    

    
    
#    #@DownloadAndClean
#    #def Download(self, series, ticker, intervals=None):
#    def Download():
#        stock = self.GetCorrectTicker(series, ticker, intervals)
#        jsonFile = pd.read_json(stock)
#                
#        return jsonFile
#        #return stockDF
#    
#    
#    
#    @Download
#    def GetMetaData(self, jsonFile):
#        #basically this algorithm does the following:
#        # 1 resets the index to a column
#        # 2 drops the time series data
#        metaList = jsonFile.reset_index()
#        
#        
#        #fix this its not always time series daily
#        #metaList.drop('Time Series (Daily)', axis=1, inplace=True)
#        
#        #the method to remove an approximate phrase
#        outTS = SearchForPhrase(metaList, 'Time Series')
#        
#        metaList.drop(outTS, axis=1, inplace=True)
#        metaList.dropna(inplace=True)
#        metaList.set_index('index', inplace=True)
#        return metaList
    
   

    
down10 = GetTickers()    
f10 = down10.DownloadAndClean('daily', 'F')



f12 = down10.DownloadAndClean('daily', 'F')


f11 = f10.copy(deep=True)

#Intraday
down01 = GetTickers()
intraDay = down01.DownloadAndClean('intraDay', 'BAC', 'one')
f1 = intraDay.copy(deep=True)


#Daily
down02 = GetTickers()
daily = down02.DownloadAndClean('daily', 'BAC')


#Daily Adjusted
down03 = GetTickers()
dailyAdjusted = down03.DownloadAndClean('dailyAdjusted', 'BAC')
da = down03.OpenHighLowCloseData(dailyAdjusted)

da = down03.DownloadAndCleanOHLC(dailyAdjusted)



#Weekly
down04 = GetTickers()
weekly = down04.DownloadAndClean('weekly', 'BAC')


#Weekly Adjusted
down05 = GetTickers()
weeklyAdjusted = down05.DownloadAndClean('weeklyAdjusted', 'BAC')


#Monthly
down06 = GetTickers()
monthly = down06.DownloadAndClean('monthly', 'BAC')


#Monthly Adjusted
down07 = GetTickers()
monthlyAdjusted = down07.DownloadAndClean('monthlyAdjusted', 'BAC')




dasub = da['2019-05-31':]

#testing appends, but not duplicating the data

da1 = dasub.iloc[0:6]
da2 = dasub.iloc[4:]





#stack overflow, this worked
da3 = da1.reset_index().merge(da2.reset_index(), how='outer').set_index('index')





da3[da3 == dasub]
#should return True if the 2 dataframes match
test = da3 == dasub











#down11 = GetTickers()
#f11 = down11.DownloadAndClean('intraDay', 'AAPL', 'one')
#
#import time
#
#
#
#down = GetTickers()
#file = down.DownloadAndClean('daily', 'AIG')
#s1 = down.GetCorrectTicker('daily', 'AIG')
#
#time.sleep(30)
#
#down2 = GetTickers()
#file2 = down.DownloadAndClean('monthlyAdjusted', 'BAC')
#s2 = down.GetCorrectTicker('monthlyAdjusted', 'BAC')
#
#time.sleep(30)
#
#down3 = GetTickers()
#file3 = down.DownloadAndClean('monthly', 'MU')
#s3 = down.GetCorrectTicker('monthly', 'MU')
#
#time.sleep(30)
#        
##down34 = Downloads()
#file4 = down.DownloadAndClean('intraDay', 'MU', 'one')
#s4 = down.GetCorrectTicker('intraDay', 'MU', 'one')
#
#tick = GetTickers()
#tick.GetCorrectTicker('daily', 'F')
#s5 = tick.DownloadAndClean('daily', 'F')
#
#
#
#
#
#
#
#t = test()
#end = time.time()
#test1 = end-start
#print('Test 1: ', test1)
#
#start2 = time.time()
#use test2()


#test of HDF5 file format

#path = r'D:\test.h5'
#store = pd.HDFStore(path)
#store['aig'] = file
#store.close()
#
#
#read = pd.HDFStore(path)
#read['aig']




