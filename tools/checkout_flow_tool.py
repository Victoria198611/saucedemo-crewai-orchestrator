from crewai.tools import BaseTool
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from services.selenium_manager import SeleniumManager

class FullCheckoutFlowTool(BaseTool):

    name: str = "full_checkout_flow"
    description: str = "Login + add to cart + checkout in one flow."

    def _run(
            self,
            product_name: str = "Sauce Labs Backpack",
            first_name: str = "Test",
            last_name: str = "User",
            postal_code: str = "12345"
    ):
        try:
            driver = SeleniumManager.get_driver()

            # LOGIN
            driver.get("https://www.saucedemo.com/")
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "user-name")))
            driver.find_element(By.ID, "user-name").send_keys("standard_user")
            driver.find_element(By.ID, "password").send_keys("secret_sauce")
            driver.find_element(By.ID, "login-button").click()

            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))

            # ADD TO CART
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

            add_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, button_id))
            )
            driver.execute_script("arguments[0].click();", add_button)

            cart_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
            )
            driver.execute_script("arguments[0].click();", cart_link)

            WebDriverWait(driver, 20).until(EC.url_contains("cart.html"))

            # CHECKOUT
            checkout_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "checkout"))
            )
            checkout_button.click()

            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "first-name")))
            driver.find_element(By.ID, "first-name").send_keys(first_name)
            driver.find_element(By.ID, "last-name").send_keys(last_name)
            driver.find_element(By.ID, "postal-code").send_keys(postal_code)

            driver.find_element(By.ID, "continue").click()

            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "finish"))
            ).click()

            confirmation = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "complete-header"))
            ).text

            return {
                "status": "success",
                "product": product_name,
                "confirmation": confirmation
            }

        except Exception as e:
            return {
                "status": "error",
                "message": str(e)
            }