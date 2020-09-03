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
            self.lineName = cfg_dict["Line"]["name"]
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

    def GetMonthDataResult(self, startDate, stopDate, lineName):
        sql = "SELECT DATE_FORMAT(time,'%Y-%m-%d') 日期,SUM(IF(`type`='投料',qty,0)) as '投料', SUM(IF(`type`='包装',qty,0)) as '包装', SUM(IF(`type`='FMA',qty,0)) as 'FMA',"
        defList = list(self.cfg_dict["DefReasons"].values())
        for type in defList:
            temp_sql = "SUM(IF(`type`='%s',qty,0)) as '%s'" % (type, type)
            if defList.index(type) != len(defList) - 1:
                sql += temp_sql + ","
            else:
                sql += temp_sql
        sql += "FROM history_input where line = '{}' and DATE_FORMAT(time,'%Y%m%d') BETWEEN '{}' and '{}' GROUP BY 日期".format(lineName,
                                                                                                                              startDate, stopDate)
        results = []
        # print(sql)
        for i in range(2):
            if i > 0:
                sql = sql.replace('history_input', 'realtime_input')
            # print(sql)
            for row in self.runQuerySql(sql):
                resultDic = {}
                resultDic["日期"] = (datetime.datetime.strptime(
                    row[0], '%Y-%m-%d')).strftime("%m/%d")
                resultDic["投料"] = row[1]
                resultDic["包装"] = row[2]
                resultDic["FMA"] = row[3]
                defTotal = 0
                for type in defList:
                    resultDic[type] = row[defList.index(type) + 4]
                    defTotal += row[defList.index(type) + 4]
                resultDic["合计"] = defTotal
                # print(defTotal)
                # print(row[1])
                if row[1] > 0:
                    # print(str(row[1]))
                    resultDic["回收率"] = str(
                        round(float(defTotal) / float(row[1]) * 100, 2)) + "%"
                else:
                    resultDic["回收率"] = "0.0%"

                results.append(resultDic)
                # print(results)
        return results

    def GetDailyDataResults(self, timeSliceList, lineName,isHistory=False, fma = False):
        sql = ""
        # sql = "select type as '不良原因',"
        # for timeSliceItem in timeSliceList:
        #     sql += "sum(case when time BETWEEN '" + timeSliceItem[0].strftime(
        #         "%Y-%m-%d %H:%M") + "' and '" + timeSliceItem[1].strftime("%Y-%m-%d %H:%M") + "' then qty else 0 end) as '" + timeSliceItem[0].strftime("%H:%M") + " to " + timeSliceItem[1].strftime("%H:%M") + "',"
        # sql = sql[:-1]
        # if fma:
        #     sql += " from {} where line = '{}'  and (defType is not null or type = 'FMA') GROUP BY type".format(
        #         "history_input" if isHistory else "realtime_input", lineName)
        # else:
        #     sql += " from {} where line = '{}'  and defType is not null GROUP BY type".format(
        #         "history_input" if isHistory else "realtime_input", lineName) 
        if fma:
            sql = "select concat(type, '-QC', qcPos),"
            for timeSliceItem in timeSliceList:
                sql += "sum(case when time BETWEEN '" + timeSliceItem[0].strftime(
                    "%Y-%m-%d %H:%M") + "' and '" + timeSliceItem[1].strftime("%Y-%m-%d %H:%M") + "' then qty else 0 end) as '" + timeSliceItem[0].strftime("%H:%M") + " to " + timeSliceItem[1].strftime("%H:%M") + "',"
            sql = sql[:-1]     
            # sql += " from {} where line = '{}'  and type = 'FMA'".format("history_input" if isHistory else "realtime_input", lineName) + " GROUP BY type, qcPos HAVING sum(qty) > 0"
            sql += " from {} where line = '{}'  and type = 'FMA' and time between '".format("history_input" if isHistory else "realtime_input", lineName) + timeSliceList[0][0].strftime("%Y-%m-%d") + " 01:00' and '" + timeSliceList[0][0].strftime("%Y-%m-%d") + " 23:00'" + " GROUP BY type, qcPos HAVING sum(qty) > 0"
            sql += '\nUNION ALL'
        sql += "\nselect type as '不良原因',"
        for timeSliceItem in timeSliceList:
            sql += "sum(case when time BETWEEN '" + timeSliceItem[0].strftime(
                "%Y-%m-%d %H:%M") + "' and '" + timeSliceItem[1].strftime("%Y-%m-%d %H:%M") + "' then qty else 0 end) as '" + timeSliceItem[0].strftime("%H:%M") + " to " + timeSliceItem[1].strftime("%H:%M") + "',"
        sql = sql[:-1]
        sql += " from {} where line = '{}'  and defType is not null GROUP BY type".format(
            "history_input" if isHistory else "realtime_input", lineName) 
        # print(sql)
        results = []
        for row in self.runQuerySql(sql):
            resultList = []
            if len(row) < 2:
                tempList = [row[0], 0]
                resultList.extend(tempList)
            else:
                resultList.extend(row)
            results.append(resultList)
        return results

    def GetDailyTotals(self, day, isHistory=False):
        totalDic = {}
        sql1 = "select type as 类型, sum(qty) as 数量 from {} where defType is null and line = '{}' and TO_DAYS({}) = TO_DAYS(time) group by type".format(
            "history_input" if isHistory else "realtime_input", self.lineName, "'" + day + "'")
        sql2 = "select sum(qty) as 不良合计 from {} where line = '{}' and defType is not null and TO_DAYS({}) = TO_DAYS(time)".format(
            "history_input" if isHistory else "realtime_input", self.lineName, "'" + day + "'")
        for row in self.runQuerySql(sql1):
            totalDic[str(row[0])] = str(row[1])
        for row in self.runQuerySql(sql2):
            totalDic["不良合计"] = str(row[0]) if row[0] is not None else "0"
        return totalDic

    def GetRealTimeDefDatas(self, lineName):
        realtimeData = {}
        sql = "select type as '不良原因', sum(qty) as '不良数量' from realtime_input where line = '{}' and defType is not NULL and TO_DAYS(time) = TO_DAYS(NOW()) GROUP BY type".format(
            lineName)
        for row in self.runQuerySql(sql):
            realtimeData[str(row[0])] = str(row[1])
        return realtimeData

    def GetRealTimeTotals(self,lineName):
        totalDic = {"投料":"0", "包装": "0", "回收": "0", "FMA": "0"}
        sql = """select type as 类型, sum(qty) as 数量 from realtime_input where line = '{}' and defType is NULL and TO_DAYS(time) = TO_DAYS(NOW()) GROUP BY type
        union
        select '回收', sum(qty) as 数量 from realtime_input where line = '{}' and defType is not null and TO_DAYS(time) = TO_DAYS(NOW())""".format(lineName, lineName)
        for row in self.runQuerySql(sql):
            for key in totalDic.keys():
                if str(row[0]) == key:
                    totalDic[key] = str(row[1])
        return totalDic

    def InsertDailyTargetData(self, data):
        sql = "replace into daily_target(dep, date, target) values('{}', '{}', {})".format(
            data[0], data[1], data[2])
        self.runNonQuerySql(sql)

    def GetCurrentQcDefData(self, lineName):
        qcDefList = []
        sql = """select type as 不良原因, 
        sum(if(qcPos = '1', qty, 0)) as qc1数量,
        sum(if(qcPos = '2', qty, 0)) as qc2数量,
        sum(if(qcPos = '3', qty, 0)) as qc3数量,
        sum(if(qcPos = '4', qty, 0)) as qc4数量
        from realtime_input where defType is not null and line = '{}' and TO_DAYS(time) = TO_DAYS(NOW()) GROUP BY type""".format(lineName)
        for row in self.runQuerySql(sql):
            tempList = [str(row[0]), str(row[1]), str(
                row[2]), str(row[3]), str(row[4])]
            qcDefList.append(tempList)
        return qcDefList

    def InsertIntoConfigTableDefInfo(self, cfg_dic):
        btnPos = 3
        defTypeNo = 1
        defTypeList = list(cfg_dic["DefReasons"].values())
        # print(defTypeList)
        for qcIndex in range(4):
            for type in defTypeList:
                sql = "REPLACE INTO config(type, def_type_no, btn_pos, qcPos) VALUES('{}', {}, '{}', {})".format(
                    type, defTypeNo, str(btnPos).zfill(2), str(qcIndex + 1))
                btnPos += 1
                defTypeNo += 1
                # print(sql)
                self.runNonQuerySql(sql)

    def GetDailyTargetData(self, name):
        dataList = {}
        sql = "select date as 日期, target as 目标量 from daily_target where dep = '{}' order by date".format(
            name)
        result = self.runQuerySql(sql)
        for row in result:
            dataList[row[0]] = row[1]
        return dataList

    def DeleteDailyTargetData(self, name, date):
        sql = "delete from daily_target where date = '{}' and dep = '{}'".format(
            date, name)
        self.runNonQuerySql(sql)

    def InsertWorkingTimeInfoToDb(self, infoList):
        sql = """replace into workingtimeperiod(amStartTime, amStopTime, pmStartTime, pmStopTime, amWorkHours, pmWorkHours, totalWorkHours, line) 
        values('{}', '{}', '{}', '{}', {}, {}, {}, '{}')
        """.format(*infoList)
        self.runNonQuerySql(sql)
    
    def InsertAdjustingDataToDb(self, data):
        sql1 = "insert into manual_fixed_log(time, qty, type, line) values(NOW(), {}, '{}', '{}')".format(str(data[1]), str(data[0]), self.lineName)
        sql2 = "insert into realtime_input(time, line, type, qty) values (NOW(), '{}', '{}', {})".format(self.lineName, str(data[0]), str(data[1]))
        self.runNonQuerySql(sql1)
        self.runNonQuerySql(sql2)


if __name__ == '__main__':
    cfg = config_mod.CfgHelper()
    cfg_dict = cfg.cfg_dict
    dbHelper = DbHelper(cfg_dict)
    dbHelper.InsertIntoConfigTableDefInfo(cfg_dict)
