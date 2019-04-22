#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 14:39:51 2019

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



def GetTops(ticker):
    stockUrl = "https://api.iextrading.com/1.0/tops?symbols=
    
    
    
def GetLast(ticker):
    stockUrl = "https://api.iextrading.com/1.0/tops/last?symbols=" + ticker
    response = pd.read_json(stockUrl)
    return response

x = GetLast('aig')



def GetMultipleLast(*ticker):
    stockUrl = "https://api.iextrading.com/1.0/tops/last?symbols="
    for x in ticker:
        stockUrl += x
        if x == ticker[-1]:
            break
        stockUrl += ','
    response = pd.read_json(stockUrl)
    return response


tickers = ('aig', 'fb', 'snap')
x2 = GetMultipleLast(*tickers)

x2 = GetMultipleLast(*('aig','fb','snap'))






