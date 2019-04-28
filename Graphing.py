
#example, works
from math import pi
from bokeh.plotting import figure, show, output_file
from bokeh.sampledata.stocks import MSFT


df = pd.DataFrame(MSFT)[:50]
df["date"] = pd.to_datetime(df["date"])

inc = df.close > df.open
dec = df.open > df.close
w = 12*60*60*1000 # half day in ms

TOOLS = "pan,wheel_zoom,box_zoom,reset,save"

p = figure(x_axis_type="datetime", tools=TOOLS, plot_width=1000, title = "MSFT Candlestick")
p.xaxis.major_label_orientation = pi/4
p.grid.grid_line_alpha=0.3

p.segment(df.date, df.high, df.date, df.low, color="black")
p.vbar(df.date[inc], w, df.open[inc], df.close[inc], fill_color="#D5E1DD", line_color="black")
p.vbar(df.date[dec], w, df.open[dec], df.close[dec], fill_color="#F2583E", line_color="black")

output_file("candlestick.html", title="candlestick.py example")

show(p)

#also works
from math import pi
from bokeh.plotting import figure, show, output_file
df2 = f2[:50]
df3 = df2.copy()

df3.rename(columns={"1. open":"open", "2. high":"high",
                    "3. low":"low", "4. close":"close", "5. volume":"volume"},
            inplace=True)


df3["date"] = pd.to_datetime(df2.index)

inc = df3.close > df3.open
dec = df3.open > df3.close

w = 12*60*60*1000

TOOLS = "pan,wheel_zoom,box_zoom,reset,save"
p = figure(x_axis_type="datetime", tools=TOOLS, plot_width=1000, title = "AAPL Candlestick")
p.xaxis.major_label_orientation = pi/4
p.grid.grid_line_alpha=0.3
p.segment(df3.date, df3.high, df3.date, df3.low, color="black")
p.vbar(df3.date[inc], w, df3.open[inc], df3.close[inc], fill_color="#D5E1DD", line_color="black")
p.vbar(df3.date[dec], w, df3.open[dec], df3.close[dec], fill_color="#F2583E", line_color="black")

output_file("candlestick.html", title="candlestick.py example")

show(p)


df4 = df3.date[inc]

df5 = df3['date'][inc]






#also works
from math import pi
from bokeh.plotting import figure, show, output_file

inc = df3.close > df3.open
dec = df3.open > df3.close

w = 24*60*60*1000

TOOLS = "pan,wheel_zoom,box_zoom,reset,save"
p = figure(x_axis_type="datetime", tools=TOOLS, plot_width=1000, title = "AAPL Candlestick")
p.xaxis.major_label_orientation = pi/4
p.grid.grid_line_alpha=0.3
p.segment(df3.date, df3.high, df3.date, df3.low, color="black")
p.vbar(df3['date'][inc], w, df3['open'][inc], df3['close'][inc],
       fill_color="#D5E1DD", line_color="black")

p.vbar(df3['date'][dec], w, df3['open'][dec], df3['close'][dec], 
       fill_color="#F2583E", line_color="black")

output_file("candlestick.html", title="candlestick.py example")

show(p)


#based on AV intraday
stock_df['date'] = pd.to_datetime(stock_df.index)    
#390 is the number of mintues the exchange is open
#6.5 hours
stock_df = stock_df[-390:]

inc = stock_df["4. close"] > stock_df["1. open"]
dec = stock_df["1. open"] > stock_df["4. close"]
#this is the key to the formatting
#based in milliseconds, so 1000*60 is 1 minute
w = 60*1000
TOOLS = "pan,wheel_zoom,box_zoom,reset,save, crosshair, hover"
p = figure(x_axis_type="datetime", tools=TOOLS, plot_width=1000, title = "Candlestick")
p.xaxis.major_label_orientation = pi/4
p.grid.grid_line_alpha=0.3
p.segment(stock_df['date'], stock_df['4. close'], stock_df['date'], stock_df['3. low'], color='black')

p.vbar(stock_df['date'][inc], w, stock_df['1. open'][inc], stock_df['4. close'][inc],
       fill_color="#D5E1DD", line_color="black")
       
p.vbar(stock_df['date'][dec], w, stock_df['1. open'][dec], stock_df['4. close'][dec], 
           fill_color="#F2583E", line_color="black")
           
output_file("candlestick.html", title="test")
show(p)
