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

            # GitHub Actions trebuie să ruleze headless
            headless = os.getenv("HEADLESS", "true").lower() == "true"

            if headless:
                options.add_argument("--headless=new")

            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-gpu")
            options.add_argument("--disable-extensions")
            options.add_argument("--disable-software-rasterizer")
            options.add_argument("--remote-debugging-port=9222")
            options.add_argument("--disable-popup-blocking")
            options.add_argument("--disable-notifications")
            options.add_argument("--window-size=1920,1080")
            service = Service(
                ChromeDriverManager().install()
            )

            cls._driver = webdriver.Chrome(
                service=service,
                options=options
            )

        return cls._driver


    @classmethod
    def quit_driver(cls):
        if cls._driver:
            cls._driver.quit()
            cls._driver = None