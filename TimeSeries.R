#Creating a time series
sales <- c(453735,465404,474742,477841,501775,503578,521750,562246,572453,592955,607816,614864,656448,658781,690422,708860)

#Yearly time series
sales_ts <- ts(sales, start = 2000,end = 2015, frequency = 1)

#Quarterly time series
sales_ts <- ts(sales, start = 2000,end = 2015, frequency = 4)

#Monthly time series
sales_ts <- ts(sales, start = c(2000 ,end = 2015), frequency = 12)

#Plotting time series
plot.ts(sales_ts)

#Transformation of timeseries in case of seasonal and random fluctuations
sales_ts_log <- log(sales_ts)

plot.ts(sales_ts_log)

#Decomposing time series
library(TTR)

#In case fluctuations are present and you want to smooth the time series
orderval <- c(1580,1560,1750,1407,1309,1424,1676,1936,1684,1488,1562,1618,1686,1840,1865,1636,1652,1699,1696,1545)
orderval_ts <- ts(orderval, start = 1996,end = 2015,frequency = 1)
plot.ts(orderval_ts)
orderval_sma3 <- SMA(orderval_ts,3)
plot.ts(orderval_sma3)
orderval_sma5 <- SMA(orderval_ts,5)
plot.ts(orderval_sma5)
orderval_sma7 <- SMA(orderval_ts,7)
plot.ts(orderval_sma7)

#Exponential smoothing
orderval_ema1_25 <- EMA(orderval_ts,1,ratio = .25)
plot.ts(orderval_ema1_25)
        
orderval_ema3_25 <- EMA(orderval_ts,3,ratio = .25)
plot.ts(orderval_ema3_25)

orderval_ema3_5 <- EMA(orderval_ts,3, ratio = .5)
plot.ts(orderval_ema3_5)

orderval_ema3_75 <- EMA(orderval_ts,3, ratio = .75)
plot.ts(orderval_ema3_75)

sales_ts_decompose <- decompose(sales_ts)
plot(sales_ts_decompose)

sales_ts_without_random <- sales_ts -sales_ts_decompose$random
sales_ts_without_random
