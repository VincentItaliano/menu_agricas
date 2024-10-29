"""Class to deals with the telegram API"""

import requests

class TelegramAPI:
    """
    Telegram API
    """

    def __init__(self, bot_token):

        self.bot_token = bot_token
        self.api_endpoint = f"https://api.telegram.org/bot{self.bot_token}/"

    def send_message(self, chat_id, message):
        """
        Send text message in the specified telegram chat
        """

        # Prepare data
        url = self.api_endpoint + 'sendMessage'
        json = {"chat_id": chat_id, "text": message}

        # Make the API request
        try:
            response = requests.post(url=url, json=json, timeout=30)
            response.raise_for_status()
        except requests.exceptions.RequestException as err:
            print('Something went wrong with request or telegram', err)

    def send_image(self, chat_id, img_bytes):
        """
        Send image in the specified telegram chat
        """

        url = self.api_endpoint + 'sendPhoto'
        data = {"chat_id": chat_id}
        files = {"photo": img_bytes}

        # Make the API request
        try:
            response = requests.post(url=url, data=data, files=files, timeout=30)
            response.raise_for_status()
        except requests.exceptions.RequestException as err:
            print('Something went wrong with request or telegram', err)
