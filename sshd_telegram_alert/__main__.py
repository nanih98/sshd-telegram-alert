import os
from .parser import parse_args
from .logger import Logger
from .configuration import Configuration
#from .requester import Requester


def main() -> None:
    """Main function where the program start"""
    config_path = os.getenv('HOME')

    args = parse_args()

    log = Logger(debug_flag=True)

    log.success("Starting the program")

    config = Configuration()

    config.check_os()

    config.get_config(config_path,args)

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
