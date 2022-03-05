import os
from .parser import parse_args
from .logger import Logger
from .configuration import Configuration
from .requester import Requester
import platform

def check_os_path():
    if platform.system() != "Linux":
        config_path = os.path.join(os.environ.get('HOME', ".sshd-telegram-credentials.json"))
        return config_path
    else:
        config_path = "/etc/ssh/.sshd-telegram-credentials.json"

def main() -> None:
    """Main function where the program start"""

    args = parse_args()
    config_path = check_os_path()

    log = Logger(debug_flag=True)
    log.success("Starting the program")

    config = Configuration()
    #config.check_os()
    config.create_config(args,config_path, platform.system())

    # Send message
    message = f"{platform.node()}:{os.environ.get('PAM_USER')}@{os.environ.get('PAM_RHOST')}: "
    if args.message:
        message += args.message
    requester = Requester()
    requester.requester(config_path, message, args, platform.system())

    # # Initzialize logger
    # logging.basicConfig(
    #     format="%(asctime)-5s %(name)-15s %(levelname)-8s %(message)s",
    #     level  = args.log_level,
    #     #filename='/tmp/python-telegram-bot.log',
    #     encoding='utf-8'
    # )

    # Start program


if __name__ == "__main__":
    main()
