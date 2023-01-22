import socket
import json
import random
import redis
from temp import GATEWAY_PORT_OUT, GATEWAY_PORT_IN

redis = redis.Redis(
     host= 'localhost',
     port= '6379')

gateway_wall = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
wall_gateway = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
DESTINATION_ADDR = 'localhost'
SOURCE_PORT_IN = random.randint(4000, 65535)
SOURCE_PORT_OUT = SOURCE_PORT_IN + 1

wall_gateway.connect((DESTINATION_ADDR, GATEWAY_PORT_IN))

init_schema = {
  "source" : "cache", 
  "destination" : "gateway", 
  "out" : SOURCE_PORT_OUT,
  "in" : SOURCE_PORT_IN
}

jsn = json.dumps(init_schema)
wall_gateway.sendall((jsn).encode())

gateway_wall.bind(('localhost', SOURCE_PORT_IN))
gateway_wall.listen(1)
# while True:
conn, addr = gateway_wall.accept()
data = conn.recv(1024)
resp_json = json.loads(data.decode())
print("messge from ", resp_json["source"] , resp_json)
redis.set('cache_port', resp_json['cache_port'])
redis.set('wall_port', resp_json['wall_port'])
print('successfuly updated cache with cache_port to ', redis.get('cache_port').decode(), ' and wall_port to ', redis.get('wall_port').decode())
