import zmq
# import random
import sys
import time
import random
from datetime import datetime
import qt5_proj.DbHelper.db_helper as dbHelper
import qt5_proj.ConfigHelper.config_helper as config_mod

port = "5556"
if len(sys.argv) > 1:
    port = sys.argv[1]
    int(port)

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:%s" % port)
cfgList = config_mod.CfgHelper().cfg_dict
databaseHelper = dbHelper.DbHelper(cfgList)
sql = "insert into com_input(btn_pos, line) values('{}', 'AL')"
typeList = ["01", "02", "03", "04", "05", "06", "07", "08", "09"]
sleepTimeList = [1, 5, 20, 10, 30, 15, 8, 7, 12]

while True:
    randomInt = random.randint(0, 8)
    databaseHelper.runNonQuerySql(sql.format(typeList[randomInt]))
    # sql = "insert into com_input(btn_pos, line) values('01', 'AL')"
    # databaseHelper.runNonQuerySql(sql)
    # sql = "insert into com_input(btn_pos, line) values('02', 'AL')"
    # databaseHelper.runNonQuerySql(sql)
    topic = "Updated at："
    messagedata = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    print("%s %s" % (topic, messagedata))
    socket.send_string("%s%s" % (topic, messagedata))
    # time.sleep(sleepTimeList[randomInt])
    time.sleep(1)
