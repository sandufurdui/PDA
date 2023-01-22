from fastapi import FastAPI
from pydantic import BaseModel
# from http import HTTPStatus
# from db import ref
from logger_setup import test_logger
import redis
import uvicorn
r = redis.Redis(host='localhost', port=6379)

class Item(BaseModel):
    request: str 
    to_set: dict

class get_status(BaseModel):
    get_status: str 

class Response(BaseModel):
    prof_port: str
    wall_port: str
    wall_port2: str
    success: str

app = FastAPI()
 

@app.get("/cache", response_model= Response)
def cache( request: Item ):
    # text = str(request.original_text)
    # print(request)
    test_logger.info("SETUP - cache service received the request")
    if(request.request == "get ports"):
      # print(request.to_set)
      
      response = {
        "prof_port": r.get("prof_port"),
        "wall_port": r.get("wall_port"),
        "wall_port2": r.get("wall_port2"),
        "success": True
      }
    if(request.request == "set ports"):
      r.mset(request.to_set)
      k = r.get("wall_port")
      # print("------------------------------------------------------------------(-------------------------------")
      m = r.get("wall_port2")
      f = r.get("prof_port")
      print("wall port stored in cache ", int(k))
      print("wall port 2 stored in cache ", int(m))
      print("porf port stored in cache ", int(f))
      response = {
        "prof_port": int(f),
        "wall_port": int(k),
        "wall_port2": int(m),
        "success": True
      }
      # status["processed_requests"] = status["processed_requests"] + 1
      # print(status)
      test_logger.info("SETUP - cache service sent response")
    return response

if __name__ == "__main__":
    # uvicorn.run("cache:app", host="0.0.0.0", port=9999)
    print()