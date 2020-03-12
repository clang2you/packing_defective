from PyQt5 import QtCore
import zmq
# import time

class CustomThread(QtCore.QObject):
    message = QtCore.pyqtSignal(str)
    def __init__(self):
        super(CustomThread, self).__init__()
        context = zmq.Context()
        self.socket = context.socket(zmq.SUB)
        print("Collecting updates from ZMQ server")
        self.socket.connect ("tcp://localhost:5555")

        self.running = True
    
    def loop(self):
        while self.running:
            string = self.socket.recv()
            self.message.emit(string)
            
