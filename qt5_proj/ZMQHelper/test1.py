import time
import zmq
import datetime

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind('tcp://*:5555')

while True:
    socket.send(b"World!")
    message = socket.recv()
    print("Received request: %s" % message)

    time.sleep(1)

    