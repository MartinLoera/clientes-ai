import requests
import pprint

DETECTION_URL = "http://35.193.135.203/"
TEST_IMAGE = "test1.jpg" 

image_data = open(TEST_IMAGE, "rb").read()

response = requests.post(DETECTION_URL, files={"image": image_data})

print(response.content)

