import tushare as ts
import datetime
a=ts.get_hist_data('600848') #一次性获取全部日k线数据
print(a['open'][0],a['close'][0],a['high'][0],a['low'][0])
date_end = time = datetime.datetime.now().strftime("%Y-%m-%d")
date_end = datetime.datetime.strptime(date_end, "%Y-%m-%d")
date_start = (date_end + datetime.timedelta(days=-1)).strftime("%Y-%m-%d")
print(date_start)
i=600000
while True:
    try:
        a = ts.get_hist_data(str(i))  # 一次性获取全部日k线数据
        z=0
        date_end = time = datetime.datetime.now().strftime("%Y-%m-%d")
        date_end = datetime.datetime.strptime(date_end, "%Y-%m-%d")
        for x in range(len(a)):
                print(a['open'][z], a['close'][z], a['high'][z], a['low'][z])
                print('1')
                from database_root import Insert_Into_SQL
                import database_root
                database_name = ['sh'+str(i)]
                database_key = ['stock_date', 'open', 'close', 'high', 'low']
                database_value=[date_start,a['open'][z], a['close'][z], a['high'][z], a['low'][z]]

                date_start = (date_end + datetime.timedelta(days=-z)).strftime("%Y-%m-%d")
                database_root.New_Database(database_name, ['stock_date', 'open', 'close', 'high', 'low']).New()

                Insert_Into_SQL(database_name,database_key,database_value).Insert()
                print(date_start)
                z=z+1
    except:
        i=i+1


#open high close low volume price_change p_change ma5 ma10 ma20 v_ma5 v_ma10 v_ma20 turnover


