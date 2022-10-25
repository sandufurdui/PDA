import socket
import json
import random
from time import sleep
from temp import GATEWAY_PORT_OUT, GATEWAY_PORT_IN

gateway_out_cache = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
gateway_out_wall = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
gateway_in = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
DESTINATION_ADDR = 'localhost'
gateway_in.bind((DESTINATION_ADDR, GATEWAY_PORT_IN))
gateway_in.listen(1)

while True:
  conn111, addr111 = gateway_in.accept()

  data = conn111.recv(1024)
  resp_json = json.loads(data.decode())
  print("messge from ", resp_json["source"] , resp_json)

  while int(resp_json["in"]) != resp_json["in"]:
      sleep.time(0.5)

  try:
    k = gateway_out_wall.sendall(b"ping")
    print("ddd   " + k)
  except:
    print('lol')





  if resp_json["source"] == 'wall':
    print("wall")
    gateway_out_wall.connect((DESTINATION_ADDR, int(resp_json['in'])))
    init_schema = {
    "source" : "gateway", 
    "destination" : resp_json['source']
    }

    jsn = json.dumps(init_schema)
    gateway_out_wall.sendall((jsn).encode())
    # gateway_out_wall.shutdown(1)
  else:
    print("urmom")

  # if resp_json["source"] == 'cache':
  #   print("wall")
  #   gateway_out_cache.connect((DESTINATION_ADDR, int(resp_json['in'])))
  #   init_schema = {
  #   "source" : "gateway", 
  #   "destination" : resp_json['source']
  #   }

  #   jsn = json.dumps(init_schema)
  #   gateway_out_cache.sendall((jsn).encode())
  #   # gateway_out_cache.shutdown(1)
  # else:
  #   print("urmom")