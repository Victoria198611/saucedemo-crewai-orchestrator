from crewai.tools import BaseTool

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from services.selenium_manager import SeleniumManager


class VerifyCartFlowTool(BaseTool):

    name: str = "verify_cart_flow"
    description: str = "Verify product exists in cart."

    def _run(self, product_name: str = "Sauce Labs Backpack"):

        try:

            driver = SeleniumManager.get_driver()

            normalized = product_name.strip("'\"").lower()


            cart_items = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located(
                    (By.CLASS_NAME, "cart_item")
                )
            )


            found = None

            for item in cart_items:

                name = item.find_element(
                    By.CLASS_NAME,
                    "inventory_item_name"
                ).text


                if normalized in name.lower():
                    found = name
                    break


            if not found:

                return {
                    "status": "error",
                    "message": f"Product '{product_name}' NOT found in cart."
                }


            return {
                "status": "success",
                "product_in_cart": found
            }


        except Exception as e:

            return {
                "status": "error",
                "message": str(e)
            }