import os
import platform
import getpass
import subprocess
from .logger import Logger
from .utils import Utils

class Configuration():
    """
        Configuration of the app
    """

    def __init__(self) -> None:
        self.log = Logger(debug_flag=True)
        self.utils = Utils()

    def info(self) -> None:
        self.log.success(f"OS: {platform.system()}")
        self.log.success(f"USER ID: {os.getuid()}")

    def check_os(self) -> None:
        if platform.system() != "Linux":
            raise Exception("This program by the moment only works with linux system")
        else:
            self.info()

    def create_config(self, args, config_path: str) -> None:
        """
            Set configuration .env file
        """
        if args.create_config:
            self.log.success("Interactive credentials creator :)")
            telegram_token = getpass.getpass("Introduce your telegram token: ")
            chat_id = getpass.getpass("Introduce your chat id: ")
            config = {
                "TELEGRAM_TOKEN": telegram_token,
                "CHAT_ID": chat_id
            }
            self.utils.write_config(config,config_path)
        
        

