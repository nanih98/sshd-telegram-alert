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

    def file_exists(self, file: str) -> None:
        if not os.path.isfile(file):
            self.log.error_and_exit(f"File {file} not found. Consider using -c flag to create new config file")
    
    def write_config(self, config, config_path) -> None:
        """This functions store credentials inside .env file (CREDENTIALS_DIR variable)"""
        # Serializing json
        json_object = json.dumps(config, indent=4)

        # Writing to sample.json
        with open(config_path, "w") as file:
            self.log.info(f"Storing json credentials inside {config_path}")
            file.writelines(json_object)
            subprocess.call(['chmod', '0700', config_path])
    
    def read_config(self, config_path):
        """
            Read file and return json object
        """
        self.file_exists(config_path)
        with open(config_path, "r") as file:
            self.log.info(f"Loading credentials from {config_path}")
            credentials = json.load(file)
            return credentials

    # def modify_pam(self):
    #     """
    #         Modify linux /etc/pam.d/sshd
    #     """
    #     with open('/etc/pam.d/sshd',"a+") as file:
    #         file.writelines(["\n#Login Telegram Notification",
    #                         "\nsession optional pam_exec.so /etc/ssh/login_notify.sh"])


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
