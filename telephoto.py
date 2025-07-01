from PIL import Image, ImageDraw, ImageFont
import requests
import configparser
import os
import logging

logging.basicConfig(filename='telegram_bot.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def send_photo_to_telegram_group(photo_path, caption, bot_token, chat_id):
    base_url = f"https://api.telegram.org/bot{bot_token}/sendPhoto"
    with open(photo_path, "rb") as my_file:
        parameters = {
            "chat_id" : chat_id,
            "caption" : caption
        }
        files = {
            "photo" : my_file
        }
        resp = requests.post(base_url, data=parameters, files=files)
        return resp.text

if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read('config.ini')
    bot_token = config.get('BotSettings', 'token')
    chat_id = config.get('BotSettings', 'chatid')

    # Get the path of the current directory
    current_directory = os.path.dirname(os.path.abspath(__file__))

    photo_path = os.path.join(current_directory, "new_image.jpg")

    with open('custom_text.txt', 'r', encoding='utf-8') as f:
        caption = f.read()

    response = send_photo_to_telegram_group(photo_path, caption, bot_token, chat_id)
    print(response)
