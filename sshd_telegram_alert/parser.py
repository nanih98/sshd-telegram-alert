import argparse

def parse_args():
    parser = argparse.ArgumentParser(
        description="""Python telegram bot requester""",
        add_help=True,
        prog="sshd-telgram-alert"
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
    parser.add_argument(
        "-m",
        "--message",
        required=False,
        dest="message",
        help="""Custom message you want to send to telegram bot chat""",
        type=str,
    )

    return parser.parse_args()
