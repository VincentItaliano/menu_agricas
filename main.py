""" Main script"""

import os
import requests

from dotenv import load_dotenv
from telegram_api import TelegramAPI


if __name__ == "__main__":

    # Load tokens and create telegram bot
    load_dotenv()
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    CHAT_ID = os.getenv("CHAT_ID")
    telegram_bot = TelegramAPI(BOT_TOKEN)

    # Agricas url and headers
    URL = "https://www.agricas.fr/images/menu/Cite-Menu.jpg"

    HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:99.0) Gecko/20100101 "
                    "Firefox/99.0",
    "Host": "www.agricas.fr",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,"
                "image/webp,*/*;q=0.8",
    "Accept-Language": "fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding": "gzip, deflate",
    "DNT": "1",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    }

    # Get the menu
    res = requests.get(URL, headers=HEADERS, timeout=30, stream=True)
    img = res.content

    # Send the menu
    telegram_bot.send_image(CHAT_ID, img)
