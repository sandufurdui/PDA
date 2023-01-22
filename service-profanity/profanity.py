from fastapi import FastAPI
from pydantic import BaseModel
from profanity_list import profanity_list
from gateway.logger_setup import test_logger
from db import ref
import time
import requests
import uvicorn
import random

def censore(sent):
    st = str(sent).lower()
    org_st = str(sent) 
    for item in profanity_list:
        if item in st:
            st = st.replace(item, '*' * len(item))
    st = list(st)           
    org_st = list(org_st)   
    runs = -1
    for char in st:
        runs+=1
        if char == "*":
            org_st[runs] = "*"
    return "".join(org_st) 

class Item(BaseModel):
    original_text: str 
    id: str

class Response(BaseModel):
    success: str
    censored: str
    # passed_check: str

app = FastAPI()



@app.get("/profanity", response_model= Response)
def profanity( request: Item ):
    test_logger.info("LOG - profanity service received the request")
    text = str(request.original_text)
    censored = censore(text)
    time.sleep(3)
    if text != censored:
        # print("your text was censored")
        test_logger.info("LOG - profanity service censored the post")
        response = {
            "success" : True,
            "censored": True,
            # "passed_che/ck": False
        }
    else:
        test_logger.info("LOG - profanity service did not censore the post")
        response = {
            "success" : True,
            "censored": False,
            # "passed_check": False
        }
    post_ref = ref.child(request.id)
    post_ref.update({
        "censored_text": censored
    })
    test_logger.info("LOG - profanity service sends response")
    return response

if __name__ == "__main__":
    service_port = random.randint(4000, 65535)
    to_send={
        "prof_port": service_port
    }
    gateway = requests.get(url='http://127.0.0.1:8080/prof_port', json=to_send)
    uvicorn.run("profanity:app", host="0.0.0.0", port=service_port)