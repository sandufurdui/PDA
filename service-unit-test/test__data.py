import wall
from pydantic import BaseModel
from test__img_byte_sample import img_byte

class prof_request(BaseModel):
    original_text: str 
    id: str

class cache_request(BaseModel):
    request: str 
    to_set: dict

class wall_request(BaseModel):
    original_text: str
    img_saved: str
    img: str

class gateway_request(BaseModel):
    original_text: str
    img_saved: str
    img: str

class gateway_prof_request(BaseModel):
    prof_port: str

class gateway_wall_request(BaseModel):
    wall_port: str

to_test_gateway_prof = gateway_prof_request(prof_port='1234')
resp_gateway_prof = {
        "message": "ok"
    }
  
to_test_gateway_wall = gateway_wall_request(wall_port='1234')
resp_gateway_wall = {
        "message": "ok"
    }

to_test_gateway = gateway_request(original_text="sgsdfgsdfgsdfgsd fuck", img_saved='', img=str(img_byte))
resp_gateway = {
        "wall" : 'False',
        "profanity": 'False',
        "censored": 'True'
}
resp_gateway1 = {
        "wall" : 'True',
        "profanity": 'True',
        "censored": 'True'
    }
to_test_wall = wall_request(original_text="sgsdfgsdfgsdfgsd fuck", img_saved="", img=str(img_byte))
resp_wall = {
            "success" : False,
            "id" : int(12345)
        }
to_test_cache = cache_request(request="set ports", to_set={"prof_port": 123456, "wall_port": 654321})
resp_cache = {
        "prof_port": 123456,
        "wall_port": 654321,
        "success": True
      }
to_test_profanity = prof_request(original_text="sgsdfgsdfgsdfgsd fuck", id=13423)
resp_profanity = {
  "success": True,
  "censored": True 
}
prof_data = {
        "original_text": "dsasdgdsfgdfs",
        "id": 3242342342,
    }

