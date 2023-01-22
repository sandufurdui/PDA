# from asyncio.windows_events import NULL
import socket
import json
import random
from time import sleep
from temp import GATEWAY_PORT_OUT, GATEWAY_PORT_IN
def is_json(myjson):
  try:
    json.loads(myjson)
  except ValueError as e:
    return False
  return True

wall_connected = False
cache_connected = False
wall_port = 0
cache_port = 0
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
  print(resp_json)
  print("messge from ", resp_json["source"] , resp_json)
  
  # if cache_connected == False | wall_connected == False:
  #   print("wall connected: ", wall_connected)
  #   print("cache connected: ", cache_connected)
  while int(resp_json["in"]) != resp_json["in"]:
    sleep.time(0.5)

  command = input("Enter command: ")
  if command == "send":
      if resp_json["source"] == 'wall':
        # print("wall")
        wall_port = resp_json['in']
        if wall_connected == False:
          gateway_out_wall.connect((DESTINATION_ADDR, int(resp_json['in'])))
          wall_connected = True
        init_schema = {
        "source" : "gateway", 
        "destination" : resp_json['source']
        }
        jsn = json.dumps(init_schema)
        gateway_out_wall.sendall((jsn).encode())
      else:
        print()
        

      if resp_json["source"] == 'cache':
        cache_port = resp_json['in']
        # print("wall")
        if cache_connected == False:
          gateway_out_cache.connect((DESTINATION_ADDR, int(resp_json['in'])))
          cache_connected = True
        init_schema = {
        "source" : "gateway", 
        "destination" : resp_json['source']
        }

        jsn = json.dumps(init_schema)
        gateway_out_cache.sendall((jsn).encode())
        # gateway_out_cache.shutdown(1)
      else:
        print()

  if command == "update":
    if resp_json["source"] == 'wall' :
      wall_port = resp_json['in']
    if resp_json["source"] == 'cache' :
      cache_port = resp_json['in']
    schema = {
      "source" : "gateway", 
      "destination" : 'cache',
      "cache_port" : cache_port,
      "wall_port" : wall_port
      }
    if cache_connected == False:
          gateway_out_cache.connect((DESTINATION_ADDR, int(resp_json['in'])))
          cache_connected = True
    jsn = json.dumps(schema)
    gateway_out_cache.sendall((jsn).encode())
