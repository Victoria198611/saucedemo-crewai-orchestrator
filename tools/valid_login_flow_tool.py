from crewai.tools import BaseTool

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from services.selenium_manager import SeleniumManager


class ValidLoginFlowTool(BaseTool):

    name: str = "valid_login_flow"
    description: str = "Atomic flow: open site + valid login."

    def _run(self):

        driver = None

        try:
            driver = SeleniumManager.get_driver()

            driver.get("https://www.saucedemo.com/")

            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "user-name"))
            )

            driver.find_element(
                By.ID,
                "user-name"
            ).send_keys("standard_user")

            driver.find_element(
                By.ID,
                "password"
            ).send_keys("secret_sauce")

            driver.find_element(
                By.ID,
                "login-button"
            ).click()


            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.CLASS_NAME, "inventory_list")
                )
            )


            return {
                "status": "success",
                "message": "Login valid reușit."
            }


        except Exception as e:

            return {
                "status": "error",
                "message": str(e)
            }