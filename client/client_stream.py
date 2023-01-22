import requests
import base64
import cv2
from fastapi import FastAPI
import requests
import random
import time
BASE_URL = "http://127.0.0.1:8080/"


nouns = ("puppy", "car", "rabbit", "girl", "monkey", "puppy", "car")
verbs = ("runs", "hits", "jumps", "drives", "barfs", "runs", "hits") 
adv = ("crazily", "dutifully", "foolishly", "merrily", "occasionally", "zoophilia", "p0rn")
adj = ("bitchers", "fingerfuckers", "fucka", "negro", "snowballing", "zoophilia", "p0rn")

image_list = ['img1.jpg', 'img2.jpg', 'img3.jpg', 'img4.jpg', 'img5.jpg', 'img6.jpg', 'img0.jpg']
app = FastAPI()
if __name__ == "__main__":

    def test_preprocessing_example02():
        num = random.randrange(0,6)
        image_name = "img"+str(num)+".jpg"
        print(image_name)
        img = cv2.imread(image_name)
        xxx = base64.b64encode(cv2.imencode('.jpg', img)[1]).decode()
        sentence = nouns[num] + ' ' + verbs[num] + ' ' + adv[num] + ' ' + adj[num]
        data = {
            "original_text": str(sentence),
            "img_saved": "",
            "img": str(xxx)
        }
        response = requests.get(url='http://127.0.0.1:8080/gateway', json=data)
        print("\nExamples")
        print("gateway response ----------\n" ,response.json())

if __name__ == "__main__":
  while True:
    # time.sleep(2)
    test_preprocessing_example02()