import requests
import re
import multi_process_threading_root as mpd
import database_root as dbs
import time
import datetime

def get_page(url):#获得网页源代码
	headers = {'"User-Agent","Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0)"'}#网页头文件
	page = requests.get(url)#以requests包中的get方法请求
	page.addheaders = [headers]
	print(page.text)
	return page.text

def get_stock(stock_list):
	#print(stock_list)
	stock_url = ["http://hq.sinajs.cn/rn=ithwg&list="+str(code) for code in stock_list]
	print(stock_url)
	return stock_url

def traversing(queue,url):
	page=get_page(url)
	res=re.findall(r"var hq_str_(.*?);\n", page)
	print(res)
	queue.put(res)

if __name__ =='__main__':
	all_stock_number = [
		# 沪市A股票买卖的代码是以600或601打头，如：运盛实业，股票代码是600767，中国国航(7.72,0.32,4.32%)是601111。
		[600001,601999],
		# B股买卖的代码是以900打头，如：上电B股(0.448,0.00,0.90%)，代码是900901。
		[900001,901000],
		# B股买卖的代码是以200打头，如：深中冠B(4.04,-0.03,-0.74%)股，代码是200018。
		[200001,201000],
		# 沪市新股申购的代码是以730打头。如：中信证券(40.89,-0.88,-2.11%)申购的代码是730030。
		[730001,731000],
		# 配股代码，沪市以700打头，深市以080打头。如：运盛实业配股代码是700767。深市草原兴发配股代码是080780。
		[700001,701000]
	]
	for kind_stock in all_stock_number:
		print(kind_stock)
		stock_list = ['sh'+str(x) for x in range(kind_stock[0], kind_stock[1])]#迭代生成所有stock_number
		for x in range(0,100):
			odds = stock_list[x::100]#为防止电脑卡死，将长stock_list切片
			print('切片'+str(x),odds)
			usl_list=''
			for x in odds:
				usl_list=usl_list+x+','
			print(usl_list)
			#stock=get_stock(odds)
			all_stock=mpd.multiprocess().Multiprocess_queue(traversing, get_stock(odds))#调用多进程
			print('多线程采集完结果：')
			print(all_stock)
			print('多线程采集完成')
			for x in all_stock:
				print(x[0])
				res= re.findall(r'(.*?),',x[0])
				print(res)
				database_name = [x[0][:8]]
				database_key = ['stock_date', 'open', 'clos', 'now', 'high', 'low']
				time=datetime.datetime.now().strftime('%Y%m%d%H%M%S')
				if res:
					database_value = [time, res[1], res[2], res[3], res[4], res[5]]
					dbs.Insert_Into_SQL(database_name,database_key,database_value).Insert()#插入数据库

