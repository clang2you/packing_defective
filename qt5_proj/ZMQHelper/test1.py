import zmq
# import random
import sys
import time
from datetime import datetime

port = "5556"
if len(sys.argv) > 1:
    port = sys.argv[1]
    int(port)

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:%s" % port)

while True:
    topic = "Updated at："
    messagedata = datetime.now().strftime("%Y/%m/%d日 %H:%M:%S")
    print("%s %s" % (topic, messagedata))
    socket.send_string("%s%s" % (topic, messagedata))
    time.sleep(1)
