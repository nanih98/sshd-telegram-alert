import os
import platform
import subprocess
from .logger import Logger

class Utils():
    def __init__(self) -> None:
        self.log = Logger(debug_flag=True)

    # def convert_path(self):
    #     """
    #         Convert path to force always end with slash "/"
    #     """
    #     if not self.dir.endswith("/"):
    #         self.dir = self.dir+"/"
    #     return self.dir

    # def get_env_path(self):
    #     """
    #         Get concatened path with .env file
    #     """
    #     env_path = self.convert_path(self.dir)+".env"

    #     return env_path

    # def create_dir(dir: str):
    #     new_dir = input(
    #         str("Enter the path where you want to create the dir to store .env: "))
    #     try:
    #         os.mkdir(dir)
    #         return new_dir
    #     except:
    #         raise Exception("Couldn't create the directory")

    def file_exists(self, file: str) -> None:
        if os.path.isfile(file):
            self.log.warning(f"File {file} exists.")
        else:
            self.log.info(f"File {file} don't exists")
    
    def write_config(self, dir: str, env: str, value: str) -> None:
        """This functions store credentials inside .env file (CREDENTIALS_DIR variable)"""
        directory = dir+"/sshd-telegram-alert"
        print(directory)
        # Create directory
        try:
            os.mkdir(directory)
        except:
            self.log.error_and_exit("Couldn't create the directory",FileExistsError)

        config = directory+"/.env"
        # Check if file exists
        self.file_exists(config)
        with open(config, "a+") as file:
            self.log.info(f"Storing variable...")
            file.writelines(f"{env}={value}" + "\n",)
            self.log.debug(f"🆗 - Variable {env} stored in {config}")
        subprocess.call(['chmod', '0700', config])

    # def dir_exists(self) -> None:
    #     """
    #         Validate if the directory where you are going to save credentials exists.
    #     """
    #     self.log.info("Check if exists /etc in the system")
    #     if platform.system() == "Darwin":
    #         new_dir = self.create_dir(self.dir)
    #     elif os.path.isdir("/etc/"):
    #         self.log.success("/etc directory exists ")
    #         return "/etc/"
    #     else:
    #         new_dir = self.create_dir(self.dir)

    #     return new_dir

    # def config_exists(self) -> str:
    #     """
    #         Check if file exists before create a new one. But first, check the directory exists.
    #     """
    #     path = self.convert_path(self.dir_exists(self.dir))
    #     config = self.get_event_path(path)
    #     if os.path.isfile(config):
    #         self.log.success("File .env exists")
    #     else:
    #         self.log.warning("File .env don't exists")
        
    #     return config
