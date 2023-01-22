from fastapi import FastAPI 
import time 
import base64
import os
import cv2
from pydantic import BaseModel 
import numpy as np
import random
import uvicorn
import requests
from logger_setup import test_logger

app = FastAPI()
class Item(BaseModel):
    location: str
    original_text: str
    img_saved: str
    img: str

class Response(BaseModel):
    success: str
    id: str

@app.get("/wall", response_model= Response)
def wall_root(request: Item):
    
    try:
        test_logger.info("LOG - wall received request ")
        # start image decoding
        test_logger.info("LOG - wall started decoding image ")
        string = str(request.img)
        jpg_original = base64.b64decode(string)
        jpg_as_np = np.frombuffer(jpg_original, dtype=np.uint8)
        img = cv2.imdecode(jpg_as_np, flags=1)
        img_code = str(random.randint(0, 9999999999999999999))
        test_logger.info("LOG - wall finished decoding image ")
        # img_code = 12345
        img_name = img_code + ".jpg"
        cv2.imwrite(img_name, img)
        cv2.imwrite("../service-db/"+ img_name, img)
        
        # end image decoding
        # start image upload
        test_logger.info("LOG - wall started uploading image ")
        db_service_request= {
            "function": "set",
            "location": request.location,
            "id": img_code,
            "to_store": {
                "original_text": request.original_text,
                "censored_text": "",
                "img_name": img_name
            }
        }
        db_service_response = requests.get(url='http://pad-nastea-service-db-1:65533/db_service', json=db_service_request)
        print(db_service_response.json())
        test_logger.info("LOG - wall finished uploading image ")
        # end image upload
        time.sleep(1)
        response = {
            "success" : True,
            "id" : img_code
        }
        test_logger.info("LOG - wall uploaded the post to db")
    except:
        test_logger.info("ERROR - wall has met some errors")
        response = {
            "success" : False,
            "id" : img_code
        }
    print(response)
    return response
    
if __name__ == "__main__":
    # service_port = random.randint(4000, 65535)
    service_port = 65534
    test_logger.info("wall service started on port: ",service_port)
    to_send={
        "wall_port": service_port,
        "wall_port2": service_port
    }
    
    # gateway = requests.get(url='http://127.0.0.1:8080/wall_port', json=to_send)
    # uvicorn.run("wall:app", host="0.0.0.0", port=service_port)