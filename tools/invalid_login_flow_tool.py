from crewai.tools import BaseTool
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InvalidLoginFlowTool(BaseTool):
    name: str = "invalid_login_flow"
    description: str = "Atomic flow: open site + invalid login + capture error + quit driver."

    def _run(self):
        driver = None
        try:
            # 1. Create driver
            driver = webdriver.Chrome()

            # 2. Open site
            driver.get("https://www.saucedemo.com/")

            # 3. Enter invalid credentials
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "user-name"))
            )
            driver.find_element(By.ID, "user-name").send_keys("invalid_user")
            driver.find_element(By.ID, "password").send_keys("invalid_pass")
            driver.find_element(By.ID, "login-button").click()

            # 4. Capture error message
            error_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "h3[data-test='error']"))
            )
            error_message = error_element.text

            return {
                "status": "success",
                "error_message": error_message
            }

        except Exception as e:
            return {
                "status": "error",
                "message": str(e)
            }

        finally:
            if driver:
                driver.quit()