# import socket
# import json

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect((socket.gethostname(), 12344))

# while True:
#         msg = s.recv(100)
#         mmmm = msg.decode()
#         y = json.loads(mmmm)
#         print("wall service: message from", y["source"], "is", y["text"] )
#         schema = {
#           "source" : "wall", 
#           "destination" : "gateway", 
#           "text" : "hello world"
#         }
#         print("sending acknoledgement")
#         s.send(json.dumps(schema).encode('utf-8'))

import socket
import time
import json

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
gatewaySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

gateway_port = 2000
wall_port = 2001
gatewaySocket.connect(("127.0.0.1", gateway_port))
# gatewaySocket.connect(("127.0.0.1", gateway_port))
s.bind((socket.gethostname(), 2001))
s.listen(5)
# s1.bind((socket.gethostname(), 2000))

while True:
    # clientsocket, address = s.accept()
    # print(f"Connection from {address} has been established.")

    schema = {
        "source" : "gateway", 
        "destination" : "wall", 
        "text" : "hello world"
    }
    
    print("dsd ", schema)
    message = json.dumps(schema).encode('utf-8')
    print(message)
    gatewaySocket.send(message)
    msg = gatewaySocket.recv(100)
    print("received text " , msg.decode('utf-8'))
