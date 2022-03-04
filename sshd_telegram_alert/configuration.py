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
            raise Exception("This programm only works with linux system")
        else:
            self.info()

    def config(self, dir: str, args) -> None:
        """
            Set configuration .env file
        """
        config_path = dir+"/sshd-telegram-alert"
        print(config_path)

        try:
            os.mkdir(config_path, mode=0o700)
        except:
            raise Exception(f"No puedo crear el directorio {config_path}")

        if args.interactive:
            self.log.info("Mode interactive")
            telegram_token = getpass.getpass("Introduce your telegram token: ")
            self.utils.write_config(
                config_path, "TELEGRAM_TOKEN", telegram_token)
            chat_id = getpass.getpass("Introduce your chat id: ")
            self.utils.write_config(config_path, "CHAT_ID", chat_id)
        else:
            if args.telegram_token and args.chat_id:
                self.log.info("Mode non-interactive")
                self.utils.write_config(
                    config_path, "TELEGRAM_TOKEN", args.telegram_token)
                self.utils.write_config(config_path, "CHAT_ID", args.chat_id)
            else:
                os.rmdir(config_path)
                raise Exception(
                    "Credentials not provided. Consider use -i (interactive) or -c chat_id -t token")
