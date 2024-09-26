import os
from dotenv import load_dotenv
from tag_map import *
import datetime
import re
import random
from pixiv_utils.pixiv_crawler import (
    KeywordCrawler,
    checkDir,
    displayAllConfig,
    download_config,
    network_config,
    ranking_config,
    user_config,
)

ARTWORK_URL = "https://www.phixiv.net/en/artworks/"

load_dotenv()
USER_ID = os.getenv("USER_ID")
COOKIE = os.getenv("COOKIE")

network_config.proxy["https"] = ""
user_config.user_id = USER_ID
user_config.cookie = COOKIE
download_config.with_tag = False
download_config.url_only = True
ranking_config.start_date = datetime.date(2024, 9, 23)
ranking_config.range = 2
ranking_config.mode = "weekly"
ranking_config.content_mode = "illust"
ranking_config.num_artwork = 20
displayAllConfig()
checkDir(download_config.store_path)

def fetch_url(tag):
    crawler = KeywordCrawler(
        keyword=TAG_DICT[tag],
        order=False,
        mode=["safe", "r18", "all"][0],
        n_images=50,
        capacity=200,
    )
    urls = crawler.run()
    urls = list(urls)
    url = urls[random.randrange(0, len(urls))]
    match = re.search(r'/(\d+)_p', url)
    if match:
        artwork_id = match.group(1)
        pixiv_url = f"{ARTWORK_URL}{artwork_id}"
        return pixiv_url