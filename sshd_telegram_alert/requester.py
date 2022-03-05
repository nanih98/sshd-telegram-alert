import os
import requests
from .utils import Utils
from .logger import Logger


class Requester():
    """
        Load data and send to telegram API
    """

    def __init__(self) -> None:
        self.log = Logger(debug_flag=True)
        self.utils = Utils()

    def send_message(self, config_path, message) -> None:
        """
            Send mesage to telegram API using requests package
        """        
        self.log.info("Sending message to telegram bot")
        credentials = self.utils.read_config(config_path)
        telegram_token = credentials["TELEGRAM_TOKEN"]
        chat_id = credentials["CHAT_ID"]
        base_url = f"https://api.telegram.org/bot{telegram_token}/sendMessage"
        data = {'chat_id': chat_id, 'text': message}
        r = requests.post(url=base_url, data=data)

        if r.status_code == 200:
            self.log.success("Message sended")
        else:
            self.log.error("Error sending message")
    
    def requester(self, config_path, message, args, os) -> None:
        """
            Send message depend of the case (PAM enabled or not)
        """
        if args.sshd_pam_detection and os.environ.get('PAM_TYPE') == "open_session" and os == "Linux":
            self.log.info("PAM enabled (Linux system)")
            self.send_message(config_path,message)
        else:
            self.log.info("PAM don't enabled, this system is not Linux, sending normal message")
            self.send_message(config_path,message)
        


