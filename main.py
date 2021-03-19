from telethon import TelegramClient
from datetime import datetime
import pytz
import socks


def parser(x):
    splited = x.split(",")

    return {
        "fullName": splited[0],
        "fistName": splited[1],
        "id": splited[2],
        "persianFirstName": splited[3].strip(),
    }


if __name__ == '__main__':
    api_id = -1  # paste your API ID
    api_hash = 'YOUR_API_HASH_GOES_HERE'  # paste your API hash
    sessionName = "ali4heydari"

    # i used Brave browser's tor as proxy :) remove proxy if you use VPN
    client = TelegramClient(sessionName, api_id, api_hash, proxy=(socks.SOCKS5, '127.0.0.1', 9350))
    client.start()

    with open("IntimateContacts.csv", "r", encoding="utf-8") as file:
        lines = file.readlines()
        intimateContacts = list(map(lambda x: parser(x), lines))

        for i, intimateContact in enumerate(intimateContacts):
            messageText = f"""
    سلام {intimateContact['persianFirstName']} جان
    عیدت مبارک.🥗 امیدوارم سال جدید پر از موفقیت و اتفاقای خوب واست باشه و به چیزایی که دوست داری برسی.
    """

            client.loop.run_until_complete(
                client.send_message(
                    intimateContact['id'], messageText,
                    schedule=datetime(
                        2020, 3, 20, 7, 19, 37,
                        tzinfo=pytz.timezone("Asia/Tehran")
                    )
                )
            )
            print(f"message scheduled for {intimateContact['fullName']}")
