import requests
# from db import leader_ref, leader_bucket
# from db import follower_ref_usa, follower_bucket_usa
# from db import follower_ref_asia, follower_bucket_asia
# to_store = {
#   "original_text": "request.original_text",
#   "censored_text": '',
#   "img_saved" : True,
#   "img": "img_name11111"
# }

# post_ref = leader_ref.child('12345')
# post_ref.set(to_store)

# blob_leader = leader_bucket.blob("img1.jpg")
# blob_leader.upload_from_filename("img1.jpg")

# post_ref = follower_ref_usa.child('12345')
# post_ref.set(to_store)

# blob_usa = follower_bucket_usa.blob("img1.jpg")
# blob_usa.upload_from_filename("img1.jpg")

# post_ref = follower_ref_asia.child('12345')
# post_ref.set(to_store)

# blob_asia = follower_bucket_asia.blob("img1.jpg")
# blob_asia.upload_from_filename("img1.jpg")

db_service_request= {
  "function": "set",
  "id": "1231232bb3134jjjdd33fd343dsfhdfj443232",
  "to_store": {
    "original_text": "yourrrrr mom gay",
    "censored_text": "your mom ***",
    "img_name": "img6.jpg",
    "xxx": "xxx"
  }
}

db_service_response = requests.get(url='http://127.0.0.1:65533/db_service', json=db_service_request)
json_response = db_service_response.json()
print(json_response)
