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
    def __init__(self, dir: str) -> None:
        self.dir = dir
        self.log = Logger(debug_flag=True)

    def load_env(self):
        """
            Load variables from .env file
        """
        dotenv_path = Path(get_env_path(self.dir))
        load_dotenv(dotenv_path=dotenv_path)

        return os.getenv('TELEGRAM_TOKEN'), os.getenv('CHAT_ID')

    def send_message(self) -> None:
        """
            Send mesage to telegram API using requests package
        """
        telegram_token, chat_id = self.load_env()
        base_url = f"https://api.telegram.org/bot{telegram_token}/sendMessage"
        data = {'chat_id': chat_id, 'text': 'hello world'}
        r = requests.post(url=base_url, data=data)

        if r.status_code == 200:
            self.log.info("Message sended")
        else:
            self.log.error("Error sending message")
