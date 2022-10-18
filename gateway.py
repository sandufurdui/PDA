import socket
import time
import json

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 12344))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established.")

    d = {
        "source" : "gateway", 
        "destination" : "wall", 
        "text" : "hello world"
    }
    
    print("dsd ", d)
    message = json.dumps(d).encode('utf-8')
    print(message)
    clientsocket.send(message)
    msg = clientsocket.recv(100)
    print("received text " , msg.decode('utf-8'))
