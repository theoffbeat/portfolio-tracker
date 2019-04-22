#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 19:49:59 2019

@author: marko
"""
import urllib.request
import json
import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
from datetime import date

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
    while datetime.datetime.now(timezone('US/Eastern')).minute <= 56:
        jsonData = requests.get(stockUrl).text
        response = json.loads(jsonData)
        quote = response[current]
        timeUS = datetime.datetime.now(timezone('US/Eastern')).strftime("%H:%M:%S")
        print("Time: {} Price: {}".format(timeUS, quote))
        time.sleep(15)
        
        price.append(quote)
        
    return price
        
def GetPrice(ticker):
    stockUrl = 'https://api.iextrading.com/1.0/stock/' + str(ticker.lower()) + '/chart/1m'
    jsonData = requests.get(stockUrl).text
    response = json.loads(jsonData)
    return response

quote2 = GetPrice("MU")

def DownloadAndCreatedf(ticker):
    stockUrl = 'https://api.iextrading.com/1.0/stock/' + str(ticker.lower()) + '/chart/1m'
    jsonData = requests.get(stockUrl).text
    response = json.loads(jsonData)
    
    openLis = []
    highLis = []
    lowLis = []
    closeLis = []
    volumeLis = []
    dateLis = []
    changeLis = []
    changePercentLis = []
    
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
            if k == "change":
                changeLis.append(v)
            if k == "changePercent":
                changePercentLis.append(v)
            
    iexdf = pd.DataFrame(
        {"open": openLis,
         "high": highLis,
         "low": lowLis,
         "close": closeLis,
         "volume": volumeLis,
         "change": changeLis,
         "changePercent": changePercentLis}, index=dateLis)
    
    return iexdf
    
quoteMU = DownloadAndCreatedf('mu')
quoteBAC = DownloadAndCreatedf('bac')
quoteAIG = DownloadAndCreatedf('aig')
    
#OHLC data gathering
def ohlc(ticker, df=None):
    stockUrl = 'https://api.iextrading.com/1.0/stock/' + str(ticker.lower()) + '/ohlc'
    #stockUrl = 'https://api.iextrading.com/1.0/stock/dnp/ohlc'    
    jsonData = requests.get(stockUrl).text
    response = json.loads(jsonData)
    
    #creates the dataframe if it is empty or does not exist
    if df is None or df.empty:
        ohlcdf = pd.DataFrame(
        {"date":[],
         "open": [],
         "high": [],
         "low": [],
         "close": []})

    
    #convert from Unix time to normal time
    unixDate = response['open']['time']
    date = datetime.utcfromtimestamp(unixDate/1000).strftime('%Y-%m-%d')
    
    data = [[date,
        response['open']['price'],
        response['high'],
        response['low'],
        response['close']['price']]]
    
    if df is not None and df.index[-1] == date:
        print("Stop! Already have this data")
    
    ohlcdf = pd.DataFrame(data, columns=['date','open', 'high', 'low', 'close'])
    ohlcdf2 = ohlcdf.set_index('date')


    return ohlcdf2
    
test = ohlc('aig')

test.to_excel("/home/marko/Downloads/Stock App/aig.xlsx", index_label='date', sheet_name="AIG")

df = pd.read_excel("/home/marko/Downloads/Stock App/aig.xlsx", sheet_name="AIG", index_col=0)
    
x2 = ohlc('aig', df)