import requests
import logging

logger = logging.getLogger(__name__)


def send_message(text, chat_id, token):
    try:
        res = requests.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}").json()
        logger.info(f"Message sent: {res}")
    except Exception as e:
        logger.error(f"Failed to send message: {e}")
