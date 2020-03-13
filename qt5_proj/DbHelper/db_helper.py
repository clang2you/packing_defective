import pymysql
import qt5_proj.ConfigHelper.config_helper as config_mod
import datetime
# # print(cfg_dict)


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
        except Exception as ex:
            print(ex)
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
        sql += "FROM history_input where DATE_FORMAT(time,'%Y%m%d') BETWEEN '{}' and '{}' GROUP BY 日期".format(
            startDate, stopDate)
        results = []
        # print(sql)
        for i in range(2):
            if i > 0:
                sql = sql.replace('history_input', 'realtime_input')
            for row in self.runQuerySql(sql):
                resultDic = {}
                resultDic["日期"] = (datetime.datetime.strptime(
                    row[0], '%Y-%m-%d')).strftime("%m/%d")
                resultDic["投料"] = row[1]
                resultDic["包装"] = row[2]
                defTotal = 0
                for type in defList:
                    resultDic[type] = row[defList.index(type) + 3]
                    defTotal += row[defList.index(type) + 3]
                resultDic["合计"] = defTotal
                if row[1] >0 :
                    resultDic["回收率"] = str(round((defTotal / row[1]), 1) * 100) + "%"
                else:
                    resultDic["回收率"] = "0.0%"
                
                results.append(resultDic)
        return results

    def GetDailyDataResults(self, timeSliceList, isHistory=False):
        sql = "select type as '不良原因',"
        for timeSliceItem in timeSliceList:
            sql += "sum(case when time BETWEEN '" + timeSliceItem[0].strftime(
                "%Y-%m-%d %H:%M") + "' and '" + timeSliceItem[1].strftime("%Y-%m-%d %H:%M") + "' then qty else 0 end) as '" + timeSliceItem[0].strftime("%H:%M") + " to " + timeSliceItem[1].strftime("%H:%M") + "',"
        sql = sql[:-1]
        sql += " from {} where defType is not null GROUP BY type".format("history_input" if isHistory else "realtime_input")
        # print(sql)
        results = []
        for row in self.runQuerySql(sql):
            resultList = []
            resultList.extend(row)
            results.append(resultList)
        return results
    
    def GetDailyTotals(self, day, isHistory=False):
        totalDic = {}
        sql1 = "select type as 类型, sum(qty) as 数量 from {} where defType is null and TO_DAYS({}) = TO_DAYS(time) group by type".format("history_input" if isHistory else "realtime_input", "'" + day + "'")
        sql2 = "select sum(qty) as 不良合计 from {} where defType is not null and TO_DAYS({}) = TO_DAYS(time)".format("history_input" if isHistory else "realtime_input", "'" + day + "'")
        for row in self.runQuerySql(sql1):
            totalDic[str(row[0])] = str(row[1])
        for row in self.runQuerySql(sql2):
            totalDic["不良合计"] = str(row[0]) if row[0] is not None else "0"
        return totalDic
    
    def GetRealTimeDefDatas(self):
        realtimeData = {}
        sql = "select type as '不良原因', sum(qty) as '不良数量' from realtime_input where defType is not NULL and TO_DAYS(time) = TO_DAYS(NOW()) GROUP BY type"
        for row in self.runQuerySql(sql):
            realtimeData[str(row[0])] = str(row[1])
        return realtimeData
    
    def GetRealTimeTotals(self):
        totalDic = {}
        sql = """select type as 类型, sum(qty) as 数量 from realtime_input where defType is NULL and TO_DAYS(time) = TO_DAYS(NOW()) GROUP BY type
        union
        select '回收', sum(qty) as 数量 from realtime_input where defType is not null and TO_DAYS(time) = TO_DAYS(NOW())"""
        for row in self.runQuerySql(sql):
            totalDic[str(row[0])] = str(row[1])
        return totalDic


if __name__ == '__main__':
    cfg = config_mod.CfgHelper()
    cfg_dict = cfg.cfg_dict
    dbHelper = DbHelper(cfg_dict)
    print(dbHelper.GetRealTimeTotals())
