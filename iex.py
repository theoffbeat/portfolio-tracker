
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#https://api.iextrading.com/1.0/stock/aapl/chart/5y

import pandas as pd
import requests
import matplotlib

from bokeh.plotting import figure, show, output_file

from math import pi

from bokeh.io import export_png


def download(ticker, duration):
    first = "https://api.iextrading.com/1.0/stock/"
    #ticker = ""
    second = "/chart/"
    length = {"5" : "5y", "2" : "2y", "day" : "1d"}

    url = first + ticker.lower() + second + length[duration]

    return url

df = download("mu", "5")

json = pd.read_json(df)

open = json["open"]
ohlc = json.loc[:,["date", "open", "high", "low", "close"]]

#ohlc = ohlc.reindex(ohlc['date'])

ohlc.index = ohlc.date
ohlc.index = ohlc.index.date
ohlc.drop(columns = ['date'], axis=1, inplace=True)

ohlc.plot()


inc = ohlc.close > ohlc.open
dec = ohlc.open > ohlc.close
w = 12*60*60*100
TOOLS = "pan,wheel_zoom,box_zoom,reset,save"

p = figure(x_axis_type="datetime", tools=TOOLS, plot_width=1000, title="MU Candlestick")
p.xaxis.major_label_orientation = pi/4
p.grid.grid_line_alpha = 0.3

p.segment(ohlc.index, ohlc.high, ohlc.index, ohlc.low, color="black")
p.vbar(ohlc.index[inc], w, ohlc.open[inc], ohlc.close[inc], fill_color="#D5E1DD", line_color="black")
p.vbar(ohlc.index[dec], w, ohlc.open[dec], ohlc.close[dec], fill_color="#F2583E", line_color="black")

export_png(p, filename="MU Candlestick.png")

show(p)



df2 = download("mu", 'day')
json2 = pd.read_json(df2)

json2 = json2.dropna()


json2['average'].plot()

json['changeOverTime']


df3 = pd.DataFrame({"change" : json['changeOverTime'], "mine" : json['changeOverTime'] * 100})
df4 = pd.DataFrame({"mine" : json2['changeOverTime'] * 100, "price" : json2['close']})
df4['mine'].plot()

json2['close'].plot()

df5 = json2['changeOverTime'] * 100











