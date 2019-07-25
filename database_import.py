
"""
#插入数据格式;
from database_root import Insert_Into_SQL
database_name=['a']
database_key=['b','c']
database_value=['b','c']
Insert_Into_SQL(database_name,database_key,database_value).Insert()


#非条件查询所有
from database_root import Select_Without_State
database_name=['a']
a=Select_Without_State(database_name).Select()
print(a)

#条件查询所有
from database_root import Select_With_State
database_name=['a']
select_key=['b','c']
select_state=['b','c']
Select_With_State(database_name,select_key,select_state).Select()

"""
'''

#插入语句
from database_root import Updata_Into_SQL
database_name=['a']
updata_key =['b','c']
updata_value=['e','f']
select_key=['b','c']
select_state=['b','c']
Updata_Into_SQL(database_name,updata_key ,updata_value ,select_key,select_state).Updata()

'''
#新建数据库：

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
import database_root
for x in all_stock_number:
    for y in range(x[0],x[1]):
        print(y)
        y='sh'+str(y)

        database_root.New_Database([y], ['stock_date','open','close','high','low']).New()




