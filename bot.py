import requests

from config import TOKEN, MY_CHAT_ID, BASE_URL


def send_message(chat_id: int | str, text: str) -> None:
    url = f'{BASE_URL}{TOKEN}/sendMessage'
    data = {
        'chat_id': chat_id,
        'text': text
    }
    requests.post(url=url, json=data)


def send_photo(chat_id: int | str, photo: str, caption: str = '') -> None:
    url = f'{BASE_URL}{TOKEN}/sendPhoto'
    data = {
        'chat_id': chat_id,
        'photo': photo,
        'caption': caption
    }
    requests.post(url=url, json=data)
