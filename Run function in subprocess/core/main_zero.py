import json
import time

import zmq

x = {
    'addition': 5
}

my_data = json.dumps(x)

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    #  Wait for next request from client
    message = socket.recv()
    print("Received request: %s" % message)

    # message_json = socket.recv()
    # print("Received request json: %s" % message_json)

    # for i in range(1):
    #    socket.send_json(x)

    #  Do some 'work'
    time.sleep(1)

    #  Send reply back to client
    socket.send_json(my_data)
