import time

import requests

from handlers import get_updates, send_message, send_photo, get_randomdog_image


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
