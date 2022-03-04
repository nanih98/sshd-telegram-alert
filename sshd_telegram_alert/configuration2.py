# import logging
# import os
# from .logger import Logger
# import subprocess
# from .parser import parse_args
# import getpass
# from .utils import Utils
# import platform


# class Configuration():
#     """
#         Class for all the validations of the program
#     """

#     def __init__(self, dir: str) -> None:
#         self.dir = dir
#         self.log = Logger(debug_flag=True)

#     def check_getuid(self) -> None:
#         if platform.system() == "Darwin":
#             pass
#         else:
#             if os.getuid() != 0:
#                 self.log.error_and_exit("You are not root", OSError)

#     def write_env(self, dir: str, env: str, value: str) -> None:
#         """This functions store credentials inside .env file (CREDENTIALS_DIR variable)"""
#         with open(dir, "a+") as file:
#             self.log.info(f"Storing variable...")
#             file.writelines(f"{env}={value}" + "\n")
#             self.log.debug(f"🆗 - Variable {env} stored in {dir}")
#         subprocess.call(['chmod', '0700', dir])

#     def set_credentials(self, dir: str) -> None:
#         """This function get the credentials from cli argument and save to a .env file that only root can read"""
#         args = parse_args()

#         if args.interactive:
#             logging.info("Mode interactive")
#             telegram_token = getpass.getpass("Introduce your telegram token: ")
#             self.write_env(dir, "TELEGRAM_TOKEN", telegram_token)
#             chat_id = getpass.getpass("Introduce your chat id: ")
#             self.write_env(dir, "CHAT_ID", chat_id)
#             return dir
#         else:
#             if args.telegram_token and args.chat_id:
#                 logging.info("Mode non-interactive")
#                 self.write_env(dir, "TELEGRAM_TOKEN", args.telegram_token)
#                 self.write_env(dir, "CHAT_ID", args.chat_id)
#                 return dir
#             else:
#                 raise Exception("Credentials not provided. Consider use -i (interactive) or -c chat_id -t token")
    
#     def check_config(self):
#         self.log.info(f"You are using {platform.system()}")
#         try:
#             utils = Utils()
#             config = utils.config_exists()
#             return config
#         except:
#             exit(1)
#             #self.set_credentials(config)

#     def clean_config(self):
#         """
#             Clean .env file
#         """
#         pass
