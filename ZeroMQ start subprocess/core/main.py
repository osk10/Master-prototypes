import json
import time
import subprocess
import zmq

x = {
    'addition': 5,
}

my_data = json.dumps(x)

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

# Start tool as subprocess. Start
subprocess.Popen(["python", "/Users/oskar/Documents/Skole/Master/Prototypes/ZeroMQ start subprocess/tool/tool.py", "5555"], stdin=subprocess.PIPE)

while True:
    #  Wait for next request from client
    message = socket.recv()
    print("Received request: %s" % message)

    time.sleep(1)

    #  Send reply back to client
    socket.send_json(my_data)
