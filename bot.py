import requests

from config import TOKEN, BASE_URL


def send_message(chat_id: int | str, text: str) -> None:
    url = f'{BASE_URL}{TOKEN}/sendMessage'
    data = {
        'chat_id': chat_id,
        'text': text
    }
    requests.post(url=url, json=data)
