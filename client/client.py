import base64
import cv2
from fastapi import FastAPI
import requests
import random
BASE_URL = "http://127.0.0.1:8080/"

nouns = ("puppy", "car", "rabbit", "girl", "monkey", "puppy", "car")
verbs = ("runs", "hits", "jumps", "drives", "barfs", "runs", "hits") 
adv = ("crazily", "dutifully", "foolishly", "merrily", "occasionally", "zoophilia", "p0rn")
adj = ("bitchers", "fingerfuckers", "fucka", "negro", "snowballing", "zoophilia", "p0rn")

image_list = ['img1.jpg', 'img2.jpg', 'img3.jpg', 'img4.jpg', 'img5.jpg', 'img6.jpg', 'img7.jpg']

app = FastAPI()
if __name__ == "__main__":
    def post_text(user_location):
        num = random.randrange(0,6)
        image_name = "img"+str(num)+".jpg"
        img = cv2.imread(image_name)
        xxx = base64.b64encode(cv2.imencode('.jpg', img)[1]).decode()
        sentence = nouns[num] + ' ' + verbs[num] + ' ' + adv[num] + ' ' + adj[num]
        data = {
            "original_text": str(sentence),
            "img_saved": "",
            "action": "set",
            "img": str(xxx),
            "location": user_location
        }
        response = requests.get(url='http://127.0.0.1:8080/gateway', json=data)
        print("\nExamples")
        print("gateway response ----------\n" ,response.json())

    def get_posts(user_location):
        print(user_location)
        data = {
            "original_text": '',
            "img_saved": "",
            "img": '',
            "action": "get",
            "location": user_location

        }
        response = requests.get(url='http://127.0.0.1:8080/gateway', json=data)
        idk = response.json()
        print("gateway response ", idk["posts"])
        # print("gateway response ----------\n" ,response.json())

if __name__ == "__main__":
    print("select one of the following location: ")
    print("1: USA")
    print("2: Asia")
    int_location = input("Location: ")
    location = ''
    if int_location == '1' :
        location = 'USA'
    elif int_location == '2' :
        location = 'Asia'
    else : 
        print("please type a valid number")
    # print(location)

    print("select one of the following actions: ")
    print("1: Get posts")
    print("2: Post something")
    int_action = input("Action: ")
    if int_action == '1' :
        get_posts(location)
        action = 'get'
    elif int_action == '2' :
        post_text(location)
        action = 'set'
    else : 
        print("please type a valid number")


