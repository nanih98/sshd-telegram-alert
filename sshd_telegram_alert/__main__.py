import os
from .parser import parse_args
from .logger import Logger
from .configuration import Configuration
from .requester import Requester
import platform


def main() -> None:
    """Main function where the program start"""

    args = parse_args()
    config_path = "/etc/ssh/.sshd-telegram-credentials.json"

    log = Logger(debug_flag=True)
    log.success("Starting the program")

    config = Configuration()
    config.check_os()
    config.create_config(args,config_path)

    # Send message
    message = f"{platform.node()}:{os.environ.get('PAM_USER')}@{os.environ.get('PAM_RHOST')}: "
    if args.message:
        message += args.message
    requester = Requester()
    requester.send_message(config_path,message)

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
