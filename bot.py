import logging
import os
import pandas as pd
from telegram_api import send_message
from status_checker import get_channel_status
from logger import setup_logging
import time

setup_logging()
logger = logging.getLogger(__name__)


def main():
    token = os.getenv('TELEGRAM_TOKEN')
    chat_id = os.getenv('CHAT_ID')

    if not token:
        logger.error("TELEGRAM_TOKEN environment variable not set")
        exit(1)

    try:
        usernames_df = pd.read_csv(
            "https://docs.google.com/spreadsheets/d/114F5zzunFfeBgjSMq_yXVaKIIfuznX2eqzuNCxzJ0OE/export?gid=1209421708&format=csv")
    except Exception as e:
        logger.error(f"Failed to read CSV: {e}")
        exit(1)

    for name in usernames_df["название"]:
        try:
            status = get_channel_status(name.replace(" ", ""))
            logger.info(f"Checked status for {name}: {status}")
            if status == "On auction":
                send_message(name + "-" + status, chat_id, token)
        except Exception as e:
            logger.error(f"Error processing {name}: {e}")


if __name__ == "__main__":
    while True:
        main()
        logger.info("Checked, now gonna sleep")
        time.sleep(24 * 60 * 60)
