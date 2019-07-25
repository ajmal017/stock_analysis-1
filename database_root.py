import pymysql
import database_config
class Connect_To_Database():
    def __init__(self,):
        self.ip=database_config.ip
        self.user=database_config.user
        self.password=database_config.password
        self.database=database_config.database
    def Connecting(self):
        # 打开数据库连接
        try:
            db = pymysql.connect(self.ip, self.user, self.password, self.database)
            print('操作数据库:'+str(self.database))
            return db
        except:
            print('请检查：database_config中'+str(self.database)+'配置信息')

class New_Database():
    def __init__(self, database_name, database_key,):
        self.database_name = database_name  # 需要插入的数据库
        self.database_key = database_key  # 数据库的key值,,,,[]格式
    def New(self):
        db = Connect_To_Database().Connecting()
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        set_key=self.database_key.pop(0)+' varchar(100) primary key not null,'

        for key in self.database_key:

            if key==self.database_key[-1]:
                set_key = set_key + key + " varchar(100)"
            else:
                set_key = set_key + key + " varchar(100),"
        print(set_key)
        sql ="create table %s(%s)"%(self.database_name[0],set_key)
        print('SQL语句:' + str(sql))
        try:
            cursor.execute(sql)
            db.commit()
            print('操作成功')
        except:
            print('写入数据库出错，请直接尝试SQL语句')




class Insert_Into_SQL():#数据的增删改查
    def __init__(self,database_name,database_key,database_value):
        self.database_name=database_name#需要插入的数据库
        self.database_key=database_key#数据库的key值,,,,[]格式
        self.database_value=database_value#数据库的value值,[]格式
    def Insert(self):
        db=Connect_To_Database().Connecting()
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        # SQL 查询语句
        sql_name=self.database_name[0]
        sql_keys=''
        for one_key in self.database_key:
            if one_key!=self.database_key[-1]:
                sql_keys=sql_keys+'`'+one_key+'`'+','
            else:
                sql_keys = sql_keys + '`' + one_key + '`'
        sql_values = tuple(self.database_value)
        sql = "INSERT INTO %s (%s) VALUES %s" % (sql_name, sql_keys, sql_values)
        #sql="INSERT INTO a (`b`,`c`) VALUES ('b', 'c')"
        print('SQL语句:'+str(sql))
        try:
            cursor.execute(sql)
            db.commit()
            print('操作成功')
        except:
            print('写入数据库出错，请直接尝试SQL语句')



#非条件查询
class Select_Without_State():
    def __init__(self,database_name):
        self.database_name=database_name
    def Select(self):
        db = Connect_To_Database().Connecting()
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        # SQL 查询语句
        sql_name = self.database_name[0]
        sql = 'SELECT * FROM '+sql_name
        print('SQL语句:'+str(sql))
        try:
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            print('操作成功')
            return results
        except:
            print('写入数据库出错，请直接尝试SQL语句')



#条件查询
class Select_With_State():
    def __init__(self,database_name,select_key,select_state):
        self.database_name=database_name
        self.select_key = select_key
        self.select_state=select_state

    def Select(self):
        db = Connect_To_Database().Connecting()
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        # SQL 查询语句
        sql_name = self.database_name[0]
        select_key = self.select_key
        select_state = self.select_state
        times=len(select_key)
        select = ''
        try:
            for x in range(times):
                one_key=select_key.pop()
                one_state=select_state.pop()
                if x+1!=times:
                    select=select+' '+'`'+one_key+'`'+ '=' +one_state+' '+ 'and'
                    #sql_keys+'`'+x+'`'+','
                else:
                    select = select +' '+ '`'+one_key+'`' + '=' + one_state
        except:
            print('条件中key不等于state值')

        sql = "select * from `%s` where %s" %(sql_name,select)
        print('SQL语句:'+str(sql))
        try:
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            #print(results)
            print('操作成功')
            return results
        except:
            print('写入数据库出错，请直接尝试SQL语句')

#插入

class Updata_Into_SQL():
    def __init__(self,database_name,updata_key ,updata_value ,select_key,select_state):
        self.database_name=database_name
        self.updata_key =updata_key
        self.updata_value =updata_value
        self.select_key=select_key
        self.select_state=select_state
    def Updata(self):
        db = Connect_To_Database().Connecting()
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        # SQL 查询语句
        sql_name = self.database_name[0]
        updata_key=self.updata_key
        updata_value=self.updata_value
        updata=''
        updata_times = len(updata_key)
        try:
            for x in range(updata_times):
                one_key = updata_key.pop()
                one_value = updata_value.pop()
                if x + 1 != updata_times:
                    updata = updata + ' ' + '`' + one_key + '`' + '=' + '"'+ one_value + '"'+ ' ' + ','
                    # sql_keys+'`'+x+'`'+','
                else:
                    updata = updata + ' ' + '`' + one_key + '`' + '=' + '"'+one_value+ '"'
        except:
            print('key不等于value值')

        select_key = self.select_key
        select_state = self.select_state
        select_times = len(select_key)
        select = ''
        try:
            for x in range(select_times):
                one_key = select_key.pop()
                one_state = select_state.pop()
                if x + 1 != select_times:
                    select = select + ' ' + '`' + one_key + '`' + '=' + one_state + ' ' + 'and'
                    # sql_keys+'`'+x+'`'+','
                else:
                    select = select + ' ' + '`' + one_key + '`' + '=' + one_state
        except:
            print('条件中key不等于state值')

        sql = "UPDATE `%s` SET  %s WHERE %s" % (sql_name,updata, select)
        print('SQL语句:'+str(sql))
        try:
            cursor.execute(sql)
            db.commit()
            print('操作成功')
        except:
            print('写入数据库出错，请直接尝试SQL语句')








