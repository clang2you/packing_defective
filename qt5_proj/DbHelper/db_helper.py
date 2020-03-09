import pymysql
import qt5_proj.ConfigHelper.config_helper as config_mod
# # print(cfg_dict)
# cfg = config_mod.CfgHelper()
# cfg_dict = cfg.cfg_dict

class DbHelper():
    def __init__(self, cfg_dict):
        if cfg_dict["MySQL"] != None:
            self.db_add = cfg_dict["MySQL"]["address"]
            self.db_user = cfg_dict["MySQL"]["user"]
            self.db_password = cfg_dict["MySQL"]["password"]
            self.db_port = 3306
            self.db_name = cfg_dict["MySQL"]["dbName"]
            self.cfg_dict = cfg_dict
        else:
            self.db_add = None
            self.db_user = None
            self.db_password = None
            self.db_port = None
            self.db_name = None

    def connectToDb(self):
        if self.db_name != None:
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
            cursor.execute(
                'create database if not exists %s default charset utf8mb4' % self.db_name)
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
        results = []
        try:
            cursor.execute('use %s' % self.db_name)
            cursor.execute(sql)
            results = cursor.fetchall()
            # for row in results:
            #     date = row[0]
            #     input = row[1]
            #     pack = row[2]
            #     def_1 = row[3]
            #     print("日期: %s ; 投料: %s ; 包装: %s; 高胶：%s" % (date, input, pack, def_1))
        finally:
            cursor.close()
            db_conn.close()
        return results

    def GetMonthDataResult(self, startDate, stopDate):
        sql = "SELECT DATE_FORMAT(time,'%Y-%m-%d') 日期,SUM(IF(`type`='投料',qty,0)) as '投料', SUM(IF(`type`='包装',qty,0)) as '包装',"
        defList = list(self.cfg_dict["DefReasons"].values())
        for type in defList:
            temp_sql = "SUM(IF(`type`='%s',qty,0)) as '%s'" % (type, type)
            if defList.index(type) != len(defList) - 1:
                sql += temp_sql + ","
            else:
                sql += temp_sql
        sql += "FROM realtime_input where DATE_FORMAT(time,'%Y%m%d') BETWEEN '{}' and '{}' GROUP BY 日期".format(startDate, stopDate)
        results = []
        for row in self.runQuerySql(sql):
            resultDic = {}
            resultDic["日期"] = row[0]
            resultDic["投料"] = row[1]
            resultDic["包装"] = row[2]
            defTotal = 0
            for type in defList:
                resultDic[type] = row[defList.index(type) + 3]
                defTotal += row[defList.index(type) + 3]
            resultDic["合计"] = defTotal
            resultDic["回收率"] = defTotal / row[1] * 100
            results.append(resultDic)
        return results
            
            
if __name__ == '__main__':
    dbHelper = DbHelper(cfg_dict)
    # print(dbHelper.db_name)
    print(dbHelper.GetMonthDataResult('20200301', '20200325'))