import requests

from config import TOKEN, MY_CHAT_ID, TG_BASE_URL, DOG_BASE_URL


def send_message(chat_id: int | str, text: str) -> None:
    url = f'{TG_BASE_URL}{TOKEN}/sendMessage'
    data = {
        'chat_id': chat_id,
        'text': text
    }
    requests.post(url=url, json=data)


def send_photo(chat_id: int | str, photo: str, caption: str = '') -> None:
    url = f'{TG_BASE_URL}{TOKEN}/sendPhoto'
    data = {
        'chat_id': chat_id,
        'photo': photo,
        'caption': caption
    }
    requests.post(url=url, json=data)


def get_randomdog_image() -> str:
    url = DOG_BASE_URL
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        url = data['message']
        return url

    return ''


url = get_randomdog_image()
send_photo(MY_CHAT_ID, url)

