import os

from dotenv import load_dotenv


load_dotenv('.env')

TOKEN = os.getenv('TOKEN')
MY_CHAT_ID = os.getenv('MY_CHAT_ID')
TG_BASE_URL = 'https://api.telegram.org/bot'
DOG_BASE_URL = 'https://dog.ceo/api/breeds/image/random'
