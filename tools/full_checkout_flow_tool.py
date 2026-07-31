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

            print("DEBUG: Starting full checkout flow")

            # LOGIN
            driver.get("https://www.saucedemo.com/")
            print("DEBUG: Opened saucedemo.com")

            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "user-name"))
            )
            driver.find_element(By.ID, "user-name").send_keys("standard_user")
            driver.find_element(By.ID, "password").send_keys("secret_sauce")
            driver.find_element(By.ID, "login-button").click()
            print("DEBUG: Login submitted")

            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
            )
            print("DEBUG: Inventory page loaded")

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

            print(f"DEBUG: Using button_id = {button_id}")

            add_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, button_id))
            )
            driver.execute_script("arguments[0].click();", add_button)
            print("DEBUG: Product added to cart")

            cart_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
            )
            driver.execute_script("arguments[0].click();", cart_link)
            print("DEBUG: Cart opened")

            WebDriverWait(driver, 20).until(EC.url_contains("cart.html"))
            print("DEBUG: Cart page loaded")

            # CHECKOUT
            checkout_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "checkout"))
            )
            print("DEBUG: Checkout button found")

            driver.execute_script("arguments[0].scrollIntoView(true);", checkout_button)
            driver.execute_script("arguments[0].click();", checkout_button)
            print("DEBUG: Checkout clicked via JS")

            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "first-name"))
            )
            print("DEBUG: Checkout info page loaded")

            driver.find_element(By.ID, "first-name").send_keys(first_name)
            driver.find_element(By.ID, "last-name").send_keys(last_name)
            driver.find_element(By.ID, "postal-code").send_keys(postal_code)
            print("DEBUG: User info filled")

            #  FIX: scroll + JS click pe Continue
            continue_button = driver.find_element(By.ID, "continue")
            driver.execute_script("arguments[0].scrollIntoView(true);", continue_button)
            driver.execute_script("arguments[0].click();", continue_button)
            print("DEBUG: Continue clicked via JS")

            #  FIX: așteaptă pagina overview
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "finish"))
            )
            print("DEBUG: Finish button found")

            #  FIX: scroll + JS click pe Finish
            finish_button = driver.find_element(By.ID, "finish")
            driver.execute_script("arguments[0].scrollIntoView(true);", finish_button)
            driver.execute_script("arguments[0].click();", finish_button)
            print("DEBUG: Finish clicked via JS")

            confirmation = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "complete-header"))
            ).text

            print("DEBUG: Confirmation text:", confirmation)

            return {
                "status": "success",
                "product": product_name,
                "confirmation": confirmation
            }

        except Exception as e:
            print("DEBUG ERROR:", str(e))
            return {
                "status": "error",
                "message": str(e)
            }