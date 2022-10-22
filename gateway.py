import socket
import json
import random
from time import sleep

gateway_wall = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
wall_gateway = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
DESTINATION_ADDR = 'localhost'
SOURCE_PORT_IN = 5011
SOURCE_PORT_OUT= 5012

wall_gateway.bind((DESTINATION_ADDR, SOURCE_PORT_IN))
wall_gateway.listen(1)
conn, addr = wall_gateway.accept()
data = conn.recv(1024)
resp_json = json.loads(data.decode())
print("messge from ", resp_json["source"] , resp_json)

while int(resp_json["wall_in"]) != resp_json["wall_in"]:
    sleep.time(0.5)


print("less go")
print(int(resp_json['wall_in']))
print(resp_json['wall_in'])
gateway_wall.connect((DESTINATION_ADDR, int(resp_json['wall_in'])))
init_schema = {
  "source" : "gateway", 
  "destination" : "wall", 
  "cache" : True,
}

jsn = json.dumps(init_schema)
gateway_wall.sendall((jsn).encode())
