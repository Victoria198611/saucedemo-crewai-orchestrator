import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class SeleniumManager:
    _driver = None

    @staticmethod
    def get_driver():
        if SeleniumManager._driver is None:
            options = Options()

            headless = os.getenv("HEADLESS", "true").lower() == "true"
            if headless:
                options.add_argument("--headless=new")

            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1920,1080")

            SeleniumManager._driver = webdriver.Chrome(
                ChromeDriverManager().install(),
                options=options
            )

        return SeleniumManager._driver