import pandas as pd
import tushare as database_root
import datetime
from sklearn import linear_model


class stock_arithmetic():
    def __init__(self,stock_code,stock_kind):
        #self.date_end = '2019-01-01'
        #self.stock_code = "600848"
        self.stock_kind="low"
        date_end = datetime.datetime.now().strftime('20%y-%m-%d')
        print(date_end)
        self.date_end = date_end
        #self.stock_code = stock_code
        #print(self.stock_code)
        self.stock_kind = stock_kind

    @property
    def stock_code(self):
        return self.stock_code
    @stock_code.setter
    def stock_code(self,value):
        self.stock_code=value


        # open high close low volume price_change p_change ma5 ma10 ma20 v_ma5 v_ma10 v_ma20 turnover

    def stock_data_cleaning(self):#数据清理
        date_end = datetime.datetime.strptime(self.date_end, "%Y-%m-%d")
        date_start = (date_end + datetime.timedelta(days=-400)).strftime("%Y-%m-%d")
        date_end = date_end.strftime("%Y-%m-%d")
        get_stock = database_root.get_hist_data(self.stock_code, start=date_start, end=date_end)
        stock_sort = get_stock.sort_index(0)  # 将数据按照日期排序下。
        return stock_sort

    def stock_sklearn(self):#sklearn核心算法
        stock_sort=stock_arithmetic('','').stock_data_cleaning()
        stock_y = pd.Series(stock_sort[self.stock_kind].values) #标签停盘价格
        stock_sort_test = stock_sort.iloc[len(stock_sort)-1]
        # 使用今天的交易价格，13 个指标预测明天的价格。偏移股票数据，今天的数据，目标是明天的价格。
        stock_sort = stock_sort.drop(stock_sort.index[len(stock_sort)-1]) # 删除最后一条数据
        stock_y = stock_y.drop(stock_y.index[0]) # 删除第一条数据
        #删除掉close 也就是收盘价格。
        del stock_sort[self.stock_kind]
        del stock_sort_test[self.stock_kind]

        stock_y_test = stock_y.iloc[len(stock_y)-1]
        model = linear_model.LinearRegression()
        model.fit(stock_sort.values,stock_y)
        price=model.predict([stock_sort_test.values])
        print(price)
        print(self.stock_kind)
        print('预测价格:',model.predict([stock_sort_test.values]))
        print('实际价格:',stock_y_test)
        print('系数:',model.coef_) #系数
        print('误差值:',model.intercept_) #截断
        print("预测置信度:", model.score(stock_sort.values,stock_y)) #评分
        return price


