from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


class SeleniumManager:

    _driver = None

    @classmethod
    def get_driver(cls):

        if cls._driver is None:

            options = Options()
            options.add_argument("--headless")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1920,1080")
            options.add_argument("--disable-extensions")
            options.add_argument("--disable-background-networking")

            last_error = None
            for attempt in range(4):
                try:
                    cls._driver = webdriver.Chrome(options=options)
                    break
                except Exception as e:
                    last_error = e
                    time.sleep(3 + attempt * 2)  # 3s, 5s, 7s, 9s
            else:
                raise last_error

        return cls._driver

    @classmethod
    def quit_driver(cls):
        if cls._driver:
            cls._driver.quit()
            cls._driver = None