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

    return parser.parse_args()
