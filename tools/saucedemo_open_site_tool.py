from crewai.tools import BaseTool
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tools.driver_manager import DriverManager

class SauceDemoOpenSiteTool(BaseTool):
    name: str = "open_saucedemo_site"
    description: str = "Opens the SauceDemo site login page."

    def _run(self):
        try:
            driver = DriverManager.get_driver()
            driver.get("https://www.saucedemo.com/")

            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "user-name"))
            )
            return "Site deschis cu succes"
        except Exception as e:
            return f"Failed to open site: {str(e)}"