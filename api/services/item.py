from app.logger.My_logger import get_logger
from app.scrappers.disco_store import HomeDisco
from app.scrappers.drivers.driver import get_chrome_driver_docker
import datetime


class ItemService:

    @classmethod
    def get_items(cls):
        return cls.get_items_from_scrapper()

    @staticmethod
    def get_items_from_scrapper():
        driver = get_chrome_driver_docker()
        try:
            items = HomeDisco().get_items_from_pages(driver=driver, page_number=4)
            return items
        except Exception as err:
            logger = get_logger(datetime.datetime.now().strftime("%d-%m-%Y") + "_Scraper_Disco")
            logger.error("Error during Scraping " + str(err))
            return []
