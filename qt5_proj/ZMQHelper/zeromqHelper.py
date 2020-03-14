from PyQt5 import QtCore
import zmq
import random
import sys
import time

class ZMQListener(QtCore.QObject):
    message = QtCore.pyqtSignal(str)

    def __init__(self):
        super(ZMQListener, self).__init__()
        context = zmq.Context()
        self.socket = context.socket(zmq.SUB)
        self.message.emit("Monitoring MQ Server ...")
        self.socket.connect("tcp://localhost:5556")

        topicfilter = "Updated@"
        self.socket.setsockopt_string(zmq.SUBSCRIBE,topicfilter)

        self.running = True

    def loop(self):
        while True:
            string = self.socket.recv_string()
            self.message.emit(string)
            time.sleep(0.1)