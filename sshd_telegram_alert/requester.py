import os
import requests
from dotenv import load_dotenv
from .utils import Utils
from pathlib import Path
from .logger import Logger


class Requester():
    """
        Load data and send to telegram API
    """

    def __init__(self) -> None:
        self.log = Logger(debug_flag=True)
        self.utils = Utils()

    def open_session(self):
        """
            Detect if there is an sshd opened session
        """
        pam_type = os.environ()

    def send_message(self, config_path) -> None:
        """
            Send mesage to telegram API using requests package
        """
        credentials = self.utils.read_config(config_path)
        telegram_token = credentials["TELEGRAM_TOKEN"]
        chat_id = credentials["CHAT_ID"]
        base_url = f"https://api.telegram.org/bot{telegram_token}/sendMessage"
        data = {'chat_id': chat_id, 'text': 'Testing'}
        r = requests.post(url=base_url, data=data)
        print(r.text)

        if r.status_code == 200:
            self.log.info("Message sended")
        else:
            self.log.error("Error sending message")
