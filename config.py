import os

from dotenv import load_dotenv


load_dotenv('.env')

TOKEN = os.getenv('TOKEN')
BASE_URL = 'https://api.telegram.org/bot'
