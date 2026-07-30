from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class DriverManager:
    _driver = None

    @classmethod
    def get_driver(cls):
        if cls._driver is None:
            options = Options()
            options.add_argument("--start-maximized")
            options.add_argument("--disable-notifications")
            options.add_argument("--disable-popup-blocking")
            options.add_argument("--disable-infobars")

            # Dezactivează complet Password Manager-ul Chrome
            options.add_experimental_option("prefs", {
                "credentials_enable_service": False,
                "profile.password_manager_enabled": False
            })

            cls._driver = webdriver.Chrome(
                service=Service(ChromeDriverManager().install()),
                options=options
            )
        return cls._driver

    @classmethod
    def quit_driver(cls):
        if cls._driver is not None:
            cls._driver.quit()
            cls._driver = None