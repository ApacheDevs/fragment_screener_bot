import cloudscraper
from bs4 import BeautifulSoup
import re
import logging

logger = logging.getLogger(__name__)


def get_channel_status(channel_name):
    try:
        scraper = cloudscraper.create_scraper()
        url = f'https://fragment.com/?query={channel_name}'
        response = scraper.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        div = soup.find('div', class_=re.compile(r'^table-cell-status-thin'))
        if div:
            return div.text
        else:
            return 'Auctions not found'
    except Exception as e:
        logger.error(f"Failed to get status for {channel_name}: {e}")
        return 'Error'
