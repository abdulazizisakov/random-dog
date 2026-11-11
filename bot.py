import time

import requests

from config import TOKEN, MY_CHAT_ID, TG_BASE_URL, DOG_BASE_URL


def send_message(chat_id: int | str, text: str) -> None:
    url = f'{TG_BASE_URL}{TOKEN}/sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': text
    }
    requests.post(url=url, json=payload)


def send_photo(chat_id: int | str, photo: str, caption: str = '') -> None:
    url = f'{TG_BASE_URL}{TOKEN}/sendPhoto'
    payload = {
        'chat_id': chat_id,
        'photo': photo,
        'caption': caption
    }
    requests.post(url=url, json=payload)


def get_updates(offset: int | None = None) -> list[dict]:
    url = f'{TG_BASE_URL}{TOKEN}/getUpdates'
    payload = {
        'offset': offset
    }
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        data = response.json()
        return data['result']

    return []


def get_randomdog_image() -> str:
    url = DOG_BASE_URL
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        url = data['message']
        return url

    return ''


def main() -> None:
    last_update_id = None
    while True:
        updates = get_updates(offset=last_update_id)

        for update in updates:
            text = update['message'].get('text', '')
            chat_id = update['message']['chat']['id']
            first_name = update['message']['from']['first_name']

            if text == '/start':
                send_message(chat_id, f'salom {first_name} botga xush kelibsiz, rasm olish uchun /dog degan yozing.')
            elif text == '/dog':
                url = get_randomdog_image()
                send_photo(chat_id, url)

            last_update_id = update['update_id'] + 1

        time.sleep(0.3)

main()
