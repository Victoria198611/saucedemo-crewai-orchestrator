from crewai.tools import BaseTool

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from services.selenium_manager import SeleniumManager


class SearchProductFlowTool(BaseTool):

    name: str = "search_product_flow"
    description: str = "Search product in SauceDemo after login."

    def _run(self, product_name: str = "Sauce Labs Backpack"):

        try:
            driver = SeleniumManager.get_driver()

            normalized = product_name.strip("'\"").lower()

            WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located(
                    (By.CLASS_NAME, "inventory_item_name")
                )
            )

            products = driver.find_elements(
                By.CLASS_NAME,
                "inventory_item_name"
            )

            found_product = None

            for product in products:

                name = product.text.strip().lower()

                if normalized in name:
                    found_product = product.text
                    break


            if not found_product:

                return {
                    "status": "not_found",
                    "message": f"Product '{product_name}' not found."
                }


            return {
                "status": "success",
                "product_found": found_product
            }


        except Exception as e:

            return {
                "status": "error",
                "message": str(e)
            }