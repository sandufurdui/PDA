from fastapi import FastAPI
from pydantic import BaseModel
from db import leader_post_ref, leader_bucket, leader_root_ref
from db import follower_post_ref_usa, follower_bucket_usa, follower_usa_root_ref
from db import follower_post_ref_asia, follower_bucket_asia, follower_asia_root_ref
from logger_setup import test_logger
import time
import uvicorn
import os

class Item(BaseModel):
  location: str
  function: str
  id: str
  to_store: dict 

class Response(BaseModel):
  stored: str
  syncronized: str
  replicated_locations: list

app = FastAPI()
@app.get("/db_service")
def db_service( request: Item ):
    
    replicated_locations = ["", ""]

    stored = False
    syncronized = False
    test_logger.info("LOG - db service received request")
    parsed_request = request.to_store
    
    
    if request.function == "set":
      post_leader_ref = leader_post_ref.child(request.id)
      post_follower_usa_ref = follower_post_ref_usa.child(request.id)
      post_follower_asia_ref = follower_post_ref_asia.child(request.id)

      test_logger.info("LOG - db service function is set")
      test_logger.info("LOG - db service started setting data")
      try:
        post_leader_ref.set(request.to_store)
      except:
        print("couldn't write to leader db")
      try:
        post_follower_usa_ref.set(request.to_store)
        replicated_locations[0] = "usa_db"
      except:
        print("couldn't write to leader db")
      try:
        post_follower_asia_ref.set(request.to_store)
        replicated_locations[1] = "asia_db"
      except:
        print("couldn't write to leader db")

      test_logger.info("LOG - db service finished setting data")
      stored = True
    

    if request.function == "update":
      post_leader_ref = leader_post_ref.child(request.id)
      post_follower_usa_ref = follower_post_ref_usa.child(request.id)
      post_follower_asia_ref = follower_post_ref_asia.child(request.id)

      test_logger.info("LOG - db service function is update")
      test_logger.info("LOG - db service started updating data")
      try:
        post_leader_ref.update(request.to_store)
      except:
        print("couldn't write to leader db")
      try:
        post_follower_usa_ref.update(request.to_store)
        replicated_locations[0] = "usa_db"
      except:
        print("couldn't write to leader db")
      try:
        post_follower_asia_ref.update(request.to_store)
        replicated_locations[1] = "asia_db"
      except:
        print("couldn't write to leader db")
      
      test_logger.info("LOG - db service finished updating data")
      stored = True
    
    
    leader_root_data = leader_root_ref.get()
    follower_usa_root_data = follower_usa_root_ref.get()
    follower_asia_root_data = follower_asia_root_ref.get()
    

    if leader_root_data != follower_usa_root_data:
      test_logger.info("LOG - USA and Leader dbs are not syncronized")
      test_logger.info("LOG - Syncronizing...")
      try:
        follower_usa_root_ref.set(leader_root_data)
        test_logger.info("LOG - USA and Leader dbs are now syncronized")
      except:
        test_logger.info("ERROR - An error occured while syncronizing USA and Leader dbs")
        syncronized = False
    if leader_root_data != follower_asia_root_data:
      test_logger.info("LOG - Asia and Leader dbs are not syncronized")
      test_logger.info("LOG - Syncronizing...")
      try:
        follower_asia_root_ref.set(leader_root_data)
        test_logger.info("LOG - Asia and Leader dbs are now syncronized")
      except:
        test_logger.info("ERROR - An error occured while syncronizing Asia and Leader dbs")
        syncronized = False
    leader_root_data = leader_root_ref.get()
    follower_usa_root_data = follower_usa_root_ref.get()
    follower_asia_root_data = follower_asia_root_ref.get()
   

    if leader_root_data == follower_usa_root_data and leader_root_data == follower_asia_root_data:
      test_logger.info("LOG - All dbs are syncronized")
      syncronized = True
    time.sleep(0.5)
    

    # test_logger.info("LOG - Leader db size is %s ",len(leader_root_data["posts"]))
    # test_logger.info("LOG - USA follower db size is %s ",len(follower_usa_root_data["posts"]))
    # test_logger.info("LOG - Asia follower db size is %s ",len(follower_asia_root_data["posts"]))


    response = {
      "stored": stored,
      "syncronized": syncronized,
      "replicated_locations": replicated_locations
    }

    print(request)
    if request.function == "get":
      
      print("received function is get")
      if request.location == "USA":
        try:
          print("getting data from usa db")
          response1 = follower_post_ref_usa.get()
        except:
          print("couldnt get data from usa, trying asia db")
          response1 = follower_post_ref_asia.get()
      if request.location == "Asia":
        try:
          print("getting data from asia db")
          response1 = follower_post_ref_asia.get()
        except:
          print("couldnt get data from asia, trying usa db")
          response1 = follower_post_ref_usa.get()
      # print(response1)

      response = response1
    print(response)
    return response

if __name__ == "__main__":
  # uvicorn.run("db_service:app", host="0.0.0.0", port=65533)
  print()