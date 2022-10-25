import socket
import json
import random
import redis
from temp import GATEWAY_PORT_OUT, GATEWAY_PORT_IN

redis = redis.Redis( host= 'localhost', port= '6379')
gateway_cache = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cache_gateway = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
DESTINATION_ADDR = 'localhost'
SOURCE_PORT_IN = random.randint(4000, 65535)
SOURCE_PORT_OUT = SOURCE_PORT_IN + 1

cache_gateway.connect((DESTINATION_ADDR, GATEWAY_PORT_IN))
init_schema = {
  "source" : "cache", 
  "destination" : "gateway", 
  "out" : SOURCE_PORT_OUT,
  "in" : SOURCE_PORT_IN
}

jsn = json.dumps(init_schema)
cache_gateway.sendall((jsn).encode())

gateway_cache.bind(('localhost', SOURCE_PORT_IN))
gateway_cache.listen(1)
conn, addr = gateway_cache.accept()
data = conn.recv(1024)
resp_json = json.loads(data.decode())
print("messge from gateway ", resp_json)


while True:
  # print('urmom')
  conn, addr = gateway_cache.accept()
  data = conn.recv(1024)
  resp_json = json.loads(data.decode())
