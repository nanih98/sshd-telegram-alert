import argparse

def parse_args():
    parser = argparse.ArgumentParser(
        description="""Python telegram bot requester""",
        add_help=True,
        #argument_default="-i",
        prog="python-telegram-bot"
    )
    parser.add_argument(
        "-l",
        "--level",
        choices=["INFO", "WARNING", "ERROR", "CRITICAL", "DEBUG"],
        required=False,
        dest="log_level",
        default="DEBUG",
        help="""level of logging""",
        type=str,
    )
    parser.add_argument(
        "-c",
        "--create-config",
        required=False,
        dest="create_config",
        action='store_true',
        help="""Interactive registration token and chat_id""",
    )
    # parser.add_argument(
    #     "-i",
    #     "--interactive",
    #     required=False,
    #     dest="interactive",
    #     action='store_true',
    #     help="""Interactive registration token and chat_id""",
    # )
    # parser.add_argument(
    #     "-t",
    #     "--telegram-token",
    #     required=False,
    #     dest="telegram_token",
    #     help="""Telegram token to store in .env""",
    #     type=str,
    # )
    # parser.add_argument(
    #     "-c",
    #     "--chat-id",
    #     required=False,
    #     dest="chat_id",
    #     help="""Telegram Chat id to store in .env""",
    #     type=str,
    # )

    return parser.parse_args()
