from crewai.tools import BaseTool

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from services.selenium_manager import SeleniumManager


class AddToCartFlowTool(BaseTool):

    name: str = "add_to_cart_flow"
    description: str = "Add product to cart after login."

    def _run(self, product_name: str = "Sauce Labs Backpack"):

        try:

            driver = SeleniumManager.get_driver()


            mapping = {
                "Sauce Labs Backpack": "add-to-cart-sauce-labs-backpack",
                "Sauce Labs Bike Light": "add-to-cart-sauce-labs-bike-light",
                "Sauce Labs Bolt T-Shirt": "add-to-cart-sauce-labs-bolt-t-shirt",
                "Sauce Labs Fleece Jacket": "add-to-cart-sauce-labs-fleece-jacket",
                "Sauce Labs Onesie": "add-to-cart-sauce-labs-onesie",
                "Test.allTheThings() T-Shirt (Red)": "add-to-cart-test.allthethings()-t-shirt-(red)"
            }


            normalized = product_name.strip("'\"").lower()

            button_id = None

            for key, value in mapping.items():

                if normalized in key.lower():
                    button_id = value
                    break


            if not button_id:

                return {
                    "status": "error",
                    "message": f"No matching product found for {product_name}"
                }



            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.ID, button_id)
                )
            ).click()



            cart_link = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.CLASS_NAME, "shopping_cart_link")
                )
            )

            cart_link.click()



            cart_item = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.CLASS_NAME, "cart_item")
                )
            )


            cart_product_name = cart_item.find_element(
                By.CLASS_NAME,
                "inventory_item_name"
            ).text



            return {
                "status": "success",
                "added_product": cart_product_name
            }


        except Exception as e:

            return {
                "status": "error",
                "message": str(e)
            }