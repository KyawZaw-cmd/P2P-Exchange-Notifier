import configparser
import requests
import textgenerator


config = configparser.ConfigParser()
config.read("config.ini")

page_id = config.get("Facebook", "page_id")
access_token = config.get("Facebook", "access_token")

message = textgenerator.f_text
url = f"https://graph.facebook.com/{page_id}/feed"

data = {
    "message": message,
    "access_token": access_token,
}

response = requests.post(url, data=data)

if response.status_code == 200:
    print("Message posted successfully!")
else:
    print(f"Failed to post message: {response.text}")

