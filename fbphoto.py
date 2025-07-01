
import configparser
import requests
import os
import textgenerator

config = configparser.ConfigParser()
config.read("config.ini")

page_id = config.get("Facebook", "page_id")
access_token = config.get("Facebook", "access_token")
photo_path = os.path.join(os.getcwd(), "new_image.jpg")

url = f"https://graph.facebook.com/{page_id}/photos"

data = {
    "access_token": access_token,
    "message": textgenerator.f_text1,
}

files = {
    "source": open(photo_path, "rb"),
}

response = requests.post(url, data=data, files=files)

if response.status_code == 200:
    print("Photo uploaded successfully!")
else:
    print(f"Failed to upload photo: {response.text}")


'''
import configparser
import requests
import os

config = configparser.ConfigParser()
config.read("config.ini")

page_id = config.get("Facebook", "page_id")
access_token = config.get("Facebook", "access_token")

current_directory = os.path.dirname(os.path.abspath(__file__))
photo_path = os.path.join(current_directory, "new_image.jpg")

url = f"https://graph.facebook.com/{page_id}/photos"

data = {
    "access_token": access_token,
}

files = {
    "source": open(photo_path, "rb"),
}

response = requests.post(url, data=data, files=files)

if response.status_code == 200:
    print("Photo uploaded successfully!")
else:
    print(f"Failed to upload photo: {response.text}")
'''