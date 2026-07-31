import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class SeleniumManager:
    _driver = None

    @classmethod
    def get_driver(cls):
        if cls._driver is None:
            options = Options()

            headless = os.getenv("HEADLESS", "true").lower() == "true"
            if headless:
                options.add_argument("--headless=new")

            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1920,1080")

            service = Service(ChromeDriverManager().install())

            cls._driver = webdriver.Chrome(
                service=service,
                options=options
            )

        return cls._driver

    @classmethod
    def quit_driver(cls):
        if cls._driver is not None:
            cls._driver.quit()
            cls._driver = None