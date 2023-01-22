import firebase_admin
from firebase_admin import credentials, storage, db

# https://console.firebase.google.com/u/0/project/padd-798ce/database/padd-798ce-default-rtdb/data
leader_cred = credentials.Certificate('padd-798ce-firebase-adminsdk-2ybyx-8c9d7751d7-2.json')
leader_name = "leader_eu"
leader_eu = firebase_admin.initialize_app(leader_cred, {
    'databaseURL': 'https://padd-798ce-default-rtdb.europe-west1.firebasedatabase.app/',
    'storageBucket': 'padd-798ce.appspot.com'
})

leader_bucket = storage.bucket("padd-798ce.appspot.com", leader_eu)
leader_post_ref = db.reference("posts", leader_eu)
leader_root_ref = db.reference("", leader_eu)

# https://console.firebase.google.com/u/0/project/pad-follower-1/database/pad-follower-1-default-rtdb/data
follower_cred_usa = credentials.Certificate('pad-follower-1-firebase-adminsdk-lmq1g-7cc5adbe92.json')
follower_name_usa = "follower_usa"
follower_usa = firebase_admin.initialize_app(follower_cred_usa, {
    'databaseURL': 'https://pad-follower-1-default-rtdb.europe-west1.firebasedatabase.app/',
    'storageBucket': 'pad-follower-1.appspot.com'
}, follower_name_usa)

follower_bucket_usa = storage.bucket("pad-follower-1.appspot.com" ,follower_usa)
follower_post_ref_usa = db.reference("posts", follower_usa)
follower_usa_root_ref = db.reference("", follower_usa)

# https://console.firebase.google.com/u/0/project/pad-follower-2/database/pad-follower-2-default-rtdb/data
follower_cred_asia = credentials.Certificate('pad-follower-2-firebase-adminsdk-xonjv-6d0134a4f4.json')
follower_name_asia = "follower_asia"
follower_asia = firebase_admin.initialize_app(follower_cred_asia, {
    'databaseURL': 'https://pad-follower-2-default-rtdb.asia-southeast1.firebasedatabase.app/',
    'storageBucket': 'pad-follower-2.appspot.com'
}, follower_name_asia)

follower_bucket_asia = storage.bucket("pad-follower-2.appspot.com" ,follower_asia)
follower_post_ref_asia = db.reference("posts", follower_asia)
follower_asia_root_ref = db.reference("", follower_asia)