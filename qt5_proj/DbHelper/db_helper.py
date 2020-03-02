import pymysql
from qt5_proj.ConfigHelper.config_helper import CfgHelper

cfg = CfgHelper()
cfg_dict = cfg.cfg_dict
# print(cfg_dict)

class DbHelper():
    def __init__(self, cfg_dict):
        self.db_add = cfg_dict["MySQL"]["address"]
        self.db_user = cfg_dict["MySQL"]["user"]
        self.db_password = cfg_dict["MySQL"]["password"]
        self.db_port = int(cfg_dict["MySQL"]["port"])
        self.db_name = cfg_dict["MySQL"]["dbName"]
    
    def connectToDb(self):
        return pymysql.connect(
            host=self.db_add,
            port=self.db_port,
            user=self.db_user,
            password=self.db_password
            )

    def createDb(self):
        db_conn = self.connectToDb()
        cursor = db_conn.cursor()
        try:
            cursor.execute('create database if not exists %s default charset utf8mb4' % self.db_name)
            db_conn.commit()
        except:
            db_conn.rollback()
        finally:
            cursor.close()
            db_conn.close()
    
    def runNonQuerySql(self, sql):
        db_conn = self.connectToDb()
        cursor = db_conn.cursor()
        try:
            cursor.execute('use %s' % self.db_name)
            cursor.execute(sql)
            db_conn.commit()
        except:
            db_conn.rollback()
        finally:
            cursor.close()
            db_conn.close()  
    
    def runQuerySql(self, sql):
        db_conn = self.connectToDb()
        cursor = db_conn.cursor()
        try:
            cursor.execute('use %s' % self.db_name)
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                fid = row[0]
                fname = row[1]
                fsalary = row[2]
                print("Id: %s ; Name: %s ; Salary: %s" % (fid, fname, fsalary))
        finally:
            cursor.close()
            db_conn.close()

dbHelper = DbHelper(cfg_dict)
dbHelper.createDb()
# sql = ''
sql= '''DROP TABLE IF EXISTS boss 
CREATE table if not exists boss(id int auto_increment primary key,
                name varchar(20) not null,
                salary int not null)'''
dbHelper.runNonQuerySql(sql)
sql = """INSERT into boss(name,salary) 
      values ('Jack',91),
      ('Harden',1300),
      ('Pony',200)"""
dbHelper.runNonQuerySql(sql)
sql = 'delete from boss where salary > 200'
dbHelper.runNonQuerySql(sql)
sql = "UPDATE boss set salary = 2000 where name = 'Pony'"
dbHelper.runNonQuerySql(sql)
sql = "select * from boss"
dbHelper.runQuerySql(sql)


        