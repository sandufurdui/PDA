import socket
import json

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 12344))

while True:
        msg = s.recv(100)
        mmmm = msg.decode()
        y = json.loads(mmmm)
        print("wall service: message from", y["source"], "is", y["text"] )
        print("sending back")
        s.send("text back".encode("utf-8"))
