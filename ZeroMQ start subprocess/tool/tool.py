import json
import sys
import zmq


def addition(x):
    print("Running function in tool... ")
    y = x + 2
    print("result", y)


# Get server port
port = sys.argv[1]


context = zmq.Context()

#  Socket to talk to server
print("Connecting to hello world server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:"+port)

#  Do 10 requests, waiting each time for a response
for request in range(1):
    print("Sending request %s …" % request)
    socket.send(b"Hello")

    #  Get the reply.
    message = socket.recv_json()
    print("Received reply %s [ %s ]" % (request, message))
    # print(type(json.loads(message)))

    # Running function specified in the received JSON object.
    for func_name, value in json.loads(message).items():
        print(func_name)
        print(value)
        globals()[func_name](value)
