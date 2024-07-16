import os
import logging
import logging.config
from datetime import datetime
from dotenv import find_dotenv, load_dotenv
from src.example import square
from src.example import addition

env_file = find_dotenv()
load_dotenv()

CONFIG_DIR = "./config"
LOG_DIR = "./logs"


def setup_logging():
    """Load logging configuration"""
    log_configs = {"dev": "logging.dev.ini", "prod": "logging.prod.ini"}
    config = log_configs.get(os.environ["ENV"])
    config_path = "/".join([CONFIG_DIR, config])
    timestamp = datetime.now().strftime("%Y%m%d")

    logging.config.fileConfig(
        config_path,
        disable_existing_loggers=False,
        defaults={"log_file_name": f"{LOG_DIR}/{os.environ['ENV']}.{timestamp}.log"},
    )


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    setup_logging()
    logger = logging.getLogger(__name__)
    logger.info("Program started")
    print_hi('PyCharm')
    square(33)
    square('wsw')
    addition(33)
    addition('dwd')
    logger.info("Program finished")
