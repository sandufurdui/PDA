import socket
import json
import random

gateway_wall = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
wall_gateway = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
DESTINATION_ADDR = 'localhost'
GATEWAY_PORT_IN = 5011
GATEWAY_PORT_OUT = 5012
SOURCE_PORT_IN = random.randint(4000, 65535)
SOURCE_PORT_OUT = SOURCE_PORT_IN + 1

wall_gateway.connect((DESTINATION_ADDR, GATEWAY_PORT_IN))
init_schema = {
  "source" : "wall", 
  "destination" : "gateway", 
  "wall_out" : SOURCE_PORT_OUT,
  "wall_in" : SOURCE_PORT_IN
}

jsn = json.dumps(init_schema)
wall_gateway.sendall((jsn).encode())

gateway_wall.bind(('localhost', SOURCE_PORT_IN))
gateway_wall.listen(1)
conn, addr = gateway_wall.accept()
data = conn.recv(1024)
resp_json = json.loads(data.decode())
print("messge from ", resp_json["source"] , resp_json)
