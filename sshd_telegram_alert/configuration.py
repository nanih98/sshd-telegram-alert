import logging
import os
from logger import Logger
import subprocess
from .parser import parse_args
import getpass
from utils import get_env_path


class Configuration():
    """
        Class for all the validations of the program
    """

    def __init__(self, dir: str) -> None:
        self.dir = dir
        self.log = Logger(debug_flag=True)

    # def dir_exists(self) -> bool:
    #     """
    #         Validate if the directory where you are going to save credentials exists.
    #     """
    #     self.log.info("Validating if directory exists or could be created")
    #     if not os.path.isdir(self.dir):
    #         self.log.error_and_exit(f'{self.dir} not found')
    #         return False
    #     else:
    #         logging.info("Directory exists")
    #         return True

    def config_exists(self) -> None:
        """
            Check if file exists before create a new one. But first, check the directory exists.
        """
        #self.dir = convert_path(self.dir)

        self.log.info("Validating if .env exists")
        if os.path.isfile(get_env_path(self.dir)):
            self.log.info("File .env exists")
        else:
            self.log.warn("File don't exists")
            self.set_credentials()

    def write_env(self, env: str, value: str) -> None:
        """This functions store credentials inside .env file (CREDENTIALS_DIR variable)"""
        with open(get_env_path(self.dir), "a+") as file:
            self.log.info(f"Storing variable...")
            file.writelines(f"{env}={value}" + "\n")
            self.log.debug(
                f"🆗 - Variable {env} stored in {get_env_path(self.dir)}")
        subprocess.call(['chmod', '0700', '/tmp/python-telegram-bot/.env'])

    def set_credentials(self) -> None:
        """This function get the credentials from cli argument and save to a .env file that only root can read"""
        args = parse_args()

        if args.interactive:
            logging.info("Mode interactive")
            telegram_token = getpass.getpass("Introduce your telegram token: ")
            self.write_env("TELEGRAM_TOKEN", telegram_token)
            chat_id = getpass.getpass("Introduce your chat id: ")
            self.write_env("CHAT_ID", chat_id)
        else:
            if args.telegram_token and args.chat_id:
                logging.info("Mode non-interactive")
                self.write_env("TELEGRAM_TOKEN", args.telegram_token)
                self.write_env("CHAT_ID", args.chat_id)
            else:
                raise Exception("Credentials not provided")

    def clean_config(self):
        pass


# def run(log: Logger):
#     log.success('Scan finished successfully.')
#     validations = Configuration("/tmp/testing")
#     # validations.dir_exists()
#     validations.config_exists()


# def main():
#     log = Logger(debug_flag=True)
#     run(log)


# if __name__ == "__main__":
#     main()
