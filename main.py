import requests
import time
from pprint import pprint
API_URL: str = 'https://api.telegram.org/bot'
BOT_TOKEN: str = '6288842116:AAGPEaQ4pDE-3-MDuNjsRGL9zSa5XY7nwzw'
TEXT: str = 'Привет от группы П1М2!!!'  # текст, который выводится
MAX_COUNTER: int = 30  # время работы

offset: int = -2
counter: int = 0
chat_id: int
text: str
update_id: int
if __name__ == '__main__':
    while counter < MAX_COUNTER:
        print('attempt =', counter)# Чтобы видеть в консоли, что код живет

        #  updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?').json()
        updates1 = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset{offset - 1}').json()
        if updates1['result']:
            for result in updates1['result']:
                offset = result['update_id']
                chat_id = result['message']['from']['id']
                # text = result['message']['text']
                # update_id = result['update_id']
            #    requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT}')  # отправка сообщения

        time.sleep(1)
        counter += 1
        # pprint(updates)
        # print()
        pprint(updates1)
        # print(text)
        # print(update_id)
        #  pprint(updates2)
        #  pprint(updates3)

