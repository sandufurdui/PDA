import uvicorn
from fastapi import FastAPI
import requests
import time
from pydantic import BaseModel
from logger_setup import test_logger

services = {
    "prof_port": 0,
    "profanity_port": 5555,
    "wall_port": 0,
    "wall_port2": 0,
    "last_port": 0
}
sent_to = services["wall_port2"]
i = 0
app = FastAPI()
class Item(BaseModel):
    original_text: str
    img_saved: str
    img: str
    action: str
    location: str

class GatewayResponse(BaseModel):
    wall: str
    profanity: str
    censored: str

class prof(BaseModel):
    prof_port: str

class wall(BaseModel):
    wall_port: str
    wall_port2: str

@app.get("/prof_port")
def prof_port(data: prof):
    test_logger.info("SETUP - gateway received connection from profanity service with port: %s", data.prof_port)
    time.sleep(0.2)
    print(data)
    services["prof_port"] = data.prof_port
    cache_request={
        "request": "set ports",
        "to_set" : {
            "prof_port": data.prof_port
        }
    }
    # test_logger.info("gateway registered profanity service on port %s", data.prof_port)
    test_logger.info("SETUP - gateway requested to write in cache profanity port: %s", data.prof_port)
    cache_response = requests.get(url='http://127.0.0.1:9999/cache', json=cache_request)
    json_response = cache_response.json()
    test_logger.info("SETUP - gateway registered profanity service port")
    services["prof_port"] = json_response["prof_port"]
    return {"message": "ok"}

@app.get("/wall_port")
def wall_port(data: wall):
    print(data) 
    test_logger.info("SETUP - gateway received connection from wall service on port: %s", data.wall_port )
    time.sleep(0.2)
    if services["wall_port"] == 0 :
        services["wall_port"] = data.wall_port
    else:
        services["wall_port2"] = data.wall_port
        services["last_port"] = data.wall_port
    print(services)
    cache_request={
        "request": "set ports",
        "to_set" : {
            "wall_port": services["wall_port"],
            "wall_port2": services["wall_port2"]
        }
    }
    test_logger.info("SETUP - gateway requested to write in cache wall port: %s", data.wall_port)
    cache_response = requests.get(url='http://127.0.0.1:9999/cache', json=cache_request)
    print(cache_response.json())
    test_logger.info("SETUP - gateway registered wall service port")
    json_response = cache_response.json()
    services["wall_port"] = json_response["wall_port"]
    return {"message": "ok"}

@app.get("/gateway")
def gateway(request: Item):
    test_logger.info("LOG - gateway received request from client")
    response = {}
    wall_response = {}

    if request.action == "set":
        print("action is set ")
        # if services["wall_port"] != 0 and services["wall_port2"] != 0:
        #     if services["last_port"] == services["wall_port2"]:
        #         if services["wall_port"] != 0:
        #             services["last_port"] = services["wall_port"]
        #         print("sending to ", services["last_port"])
        #         test_logger.info("LOG - gateway redirects request to wall: %s",services["last_port"])
        #         wall_response = requests.get(url=f'http://127.0.0.1:{services["last_port"]}/wall', json=wall_data)
        #     elif services["last_port"] == services["wall_port"]:
        #         services["last_port"] = services["wall_port2"]
        #         print("sending to ", services["last_port"])
        #         test_logger.info("LOG - gateway redirects request to wall: %s",services["last_port"])
        #         wall_response = requests.get(url=f'http://127.0.0.1:{services["last_port"]}/wall', json=wall_data)
        #         # test_logger.info("gateway redirects request to wall: %s",services["last_port"])
        # elif services["wall_port"] != 0: 
        #     services["last_port"] = services["wall_port"]
        #     test_logger.info("LOG - gateway redirects request to wall: %s",services["last_port"])
        #     wall_response = requests.get(url=f'http://127.0.0.1:{services["last_port"]}/wall', json=wall_data)
        #     # test_logger.info("gateway redirects request to wall: %s",services["last_port"])
        # elif services["wall_port2"] != 0: 
        #     services["last_port"] = services["wall_port2"]
        #     test_logger.info("LOG - gateway redirects request to wall: %s",services["last_port"])
        #     wall_response = requests.get(url=f'http://127.0.0.1:{services["last_port"]}/wall', json=wall_data)
        #     # test_logger.info("gateway redirects request /to wall: %s",services["last_port"])
        wall_data = {
            "location": request.location,
            "original_text": request.original_text,
            "img_saved": request.img_saved,
            "img": request.img
        }
        try:
            wall_response = requests.get('http://pad-nastea-service-wall-1:65534/wall', json=wall_data)
        except:
            print("lol xdd")
        
        
        wall_response1 = wall_response.json()
        
        
        prof_data = {
            "original_text": request.original_text,
            "id": wall_response1["id"],
        }
        test_logger.info("LOG - gateway redirects request to profanity: %s",services["prof_port"])
        # prof_response = requests.get(url = f'http://127.0.0.1:{services["profanity_port"]}/profanity', json=prof_data)
        time.sleep(2)
        
        res = requests.post('http://pad-nastea-service-profanity-1:5555/profanity_js', json=prof_data)
            
        test_logger.info("LOG - gateway received response from profanity service")
        prof_response1 = res.json()
        

        print(prof_response1)
        # temp_img
        db_service_request= {
            "location": request.location,
            "function": "update",
            "id": wall_response1["id"],
            "to_store": {
                "original_text": request.original_text,
                "censored_text": prof_response1["result"],
                "img_name": str(wall_response1["id"] + ".jpg"),
                "location": request.location

            }
        }

        db_service_response = requests.get(url='http://pad-nastea-service-db-1:65533/db_service', json=db_service_request)
        print(db_service_response)
        
        response = {
        "wall" : wall_response1["success"],
            "profanity": wall_response1["success"],
            "censored": prof_response1["censored"]
        }


    elif request.action == "get":
        print("action is get ")
        db_service_request= {
            "location": request.location,
            "function": "get",
            "id": 'wall_response1["id"]',
            "to_store": {
                "original_text": "request.original_text",
                "censored_text": "prof_response1[result]",
                "img_name": "str(wall_response1)"
            }
        }
            
        db_service_response = requests.get(url='http://pad-nastea-service-db-1:65533/db_service', json=db_service_request)

        print(db_service_response)
        response = {
            "posts" : db_service_response.text
        }

    test_logger.info("LOG - gateway responds to the client")
    time.sleep(0.5)
    test_logger.info("---------------------------------------")
    print(response)
    return response

if __name__ == "__main__":
    # uvicorn.run("gateway:app", host="127.0.0.1", port=8080)
    test_logger.info("gateway service started on port: 8080")
