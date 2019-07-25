import pandas as pd
import tushare as ts
import datetime
from sklearn import linear_model

#################准备股票数据。#################
date_end_str = '2019-01-01'
code = "000004"

date_end = datetime.datetime.strptime(date_end_str, "%Y-%m-%d")
date_start = (date_end + datetime.timedelta(days=-400)).strftime("%Y-%m-%d")
date_end = date_end.strftime("%Y-%m-%d")

# open high close low volume price_change p_change ma5 ma10 ma20 v_ma5 v_ma10 v_ma20 turnover
stock_X = ts.get_hist_data(code, start=date_start, end=date_end)
stock_X = stock_X.sort_index(0)  # 将数据按照日期排序下。
stock_y = pd.Series(stock_X["close"].values) #标签停盘价格
print(stock_y)
stock_X_test = stock_X.iloc[len(stock_X)-1]
# 使用今天的交易价格，13 个指标预测明天的价格。偏移股票数据，今天的数据，目标是明天的价格。
stock_X = stock_X.drop(stock_X.index[len(stock_X)-1]) # 删除最后一条数据
stock_y = stock_y.drop(stock_y.index[0]) # 删除第一条数据
#删除掉close 也就是收盘价格。
del stock_X["close"]
del stock_X_test["close"]

#使用最后一个数据做测试。
stock_y_test = stock_y.iloc[len(stock_y)-1]
print(stock_y_test)
print(stock_X.tail(5))
print("****************************")
print(stock_y.tail(5)) #
#print(stock_X.values[0])

print("****************************")
print(len(stock_X),",",len(stock_y))

print("****************************")
print(stock_X_test.values,stock_y_test)

model = linear_model.LinearRegression()
model.fit(stock_X.values,stock_y)
print("******* 测试价格 & 实际价格 ********")
print(model.predict([stock_X_test.values]))
print(stock_y_test)

print("******* 参数 & 偏置值  ********")
print(model.coef_) #系数
print(model.intercept_) #截断
print("预测置信度:", model.score(stock_X.values,stock_y)) #评分
