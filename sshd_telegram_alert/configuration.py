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

    # def check_os(self) -> None:
    #     if platform.system() != "Linux":
    #         self.log.error_and_exit(
    #             "This program by the moment only works with linux system")
    #     else:
    #         self.info()
    
    def check_uid(self) -> None:
        """
            You must be root to set credentials
        """
        if os.getuid() != 0:
            self.log.error_and_exit("You must be root to store your credentials")

    def create_config(self, args, config_path, os) -> None:
        """
            Set configuration .env file
        """
        if os == "Linux":
            self.check_uid()
   
        if args.create_config:
            self.log.success("Interactive credentials creator :)")
            telegram_token = getpass.getpass("Introduce your telegram token: ")
            chat_id = getpass.getpass("Introduce your chat id: ")
            config = {
                "TELEGRAM_TOKEN": telegram_token,
                "CHAT_ID": chat_id
            }
            self.utils.write_config(config,config_path)
    
    def message(self, args) -> None:
        """
            Message type
        """
        if args.message:
            if args.sshd_pam_detection:
                pam_message = f"{platform.node()}:{os.environ.get('PAM_USER')}@{os.environ.get('PAM_RHOST')}: "
                message = pam_message + args.message
                return message
            else:
                return args.message
        else:
            self.log.error_and_exit("Message don't provided. Consider use -m flag")