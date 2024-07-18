import sys
import logging


logging.basicConfig(level=logging.INFO, stream=sys.stdout)


def get_log(msg: str = None) -> None:
    logging.log(level=logging.INFO, msg=msg)