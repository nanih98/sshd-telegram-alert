import os
import requests
from .utils import Utils
from .logger import Logger
import platform
from datetime import date

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
        self.log.info("Trying to send message to telegram bot")
        credentials = self.utils.read_config(config_path)
        telegram_token = credentials["TELEGRAM_TOKEN"]
        chat_id = credentials["CHAT_ID"]
        base_url = f"https://api.telegram.org/bot{telegram_token}/sendMessage"
        data = {'chat_id': chat_id, 'text': message}
        r = requests.post(url=base_url, data=data)

        if r.status_code == 200:
            self.log.success(f"Message sended. Date: {date.today()}")
        else:
            self.log.error(f"Error sending message. Date: {date.today()}")
    
    def requester(self,args,config_path,message):
        """
            Send message depend of the case (PAM enabled or not)
        """
        if args.sshd_pam_detection and platform.system() != "Linux":
            self.log.error_and_exit("Pam flag enabled but this is not a Linux system. Skipping")
        elif "PAM_TYPE" in os.environ:            
            if os.environ.get('PAM_TYPE') == "open_session":
                self.log.info("PAM enabled (Linux system) and PAM_TYPE = open_session")
                self.send_message(config_path, message)
        else:
            self.log.info("PAM don't enabled")
            self.send_message(config_path,message)