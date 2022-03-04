import os
import platform
import subprocess
from .logger import Logger
import json

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

    # def file_exists(self, file: str) -> None:
    #     if os.path.isfile(file):
    #         self.log.warn(f"File {file} exists.")
    #         rewrite = input(str("Rewrite [y/n]?: "))
            
    #     else:
    #         self.log.info(f"File {file} don't exists.")
    
    def write_config(self, config) -> None:
        """This functions store credentials inside .env file (CREDENTIALS_DIR variable)"""
        # Serializing json
        json_object = json.dumps(config, indent=4)
        path = os.environ['HOME']+"/.sshd-telegram-alert.json"
        print(path)

        # Writing to sample.json
        with open(path, "a+") as file:
            self.log.info(f"Storing json credentials inside {path}")
            file.writelines(json_object)
            #subprocess.call(['chmod', '0700', file])

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
