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

            wait = WebDriverWait(driver, 20)

            print("DEBUG: Starting full checkout flow")

            # =========================
            # LOGIN
            # =========================

            driver.get("https://www.saucedemo.com/")
            print("DEBUG: Opened saucedemo.com")

            wait.until(
                EC.presence_of_element_located((By.ID, "user-name"))
            )

            driver.find_element(By.ID, "user-name").send_keys(
                "standard_user"
            )

            driver.find_element(By.ID, "password").send_keys(
                "secret_sauce"
            )

            driver.find_element(By.ID, "login-button").click()

            print("DEBUG: Login submitted")


            wait.until(
                EC.presence_of_element_located(
                    (By.CLASS_NAME, "inventory_list")
                )
            )

            print("DEBUG: Inventory page loaded")


            # =========================
            # ADD TO CART
            # =========================

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
                raise Exception(
                    f"Product not found: {product_name}"
                )


            print(f"DEBUG: Using button_id = {button_id}")


            add_button = wait.until(
                EC.element_to_be_clickable(
                    (By.ID, button_id)
                )
            )

            add_button.click()

            print("DEBUG: Product added to cart")


            # =========================
            # CART
            # =========================

            cart_link = wait.until(
                EC.element_to_be_clickable(
                    (By.CLASS_NAME, "shopping_cart_link")
                )
            )

            cart_link.click()

            print("DEBUG: Cart opened")


            wait.until(
                EC.url_contains("cart.html")
            )

            print("DEBUG: Cart page loaded")


            # =========================
            # CHECKOUT START
            # =========================

            checkout_button = wait.until(
                EC.element_to_be_clickable(
                    (By.ID, "checkout")
                )
            )

            checkout_button.click()

            print("DEBUG: Checkout clicked")


            wait.until(
                EC.presence_of_element_located(
                    (By.ID, "first-name")
                )
            )

            print("DEBUG: Checkout info page loaded")


            # =========================
            # USER INFO
            # =========================

            driver.find_element(
                By.ID,
                "first-name"
            ).send_keys(first_name)

            driver.find_element(
                By.ID,
                "last-name"
            ).send_keys(last_name)

            driver.find_element(
                By.ID,
                "postal-code"
            ).send_keys(postal_code)


            print("DEBUG: User info filled")


            # =========================
            # CONTINUE
            # =========================

            continue_button = wait.until(
                EC.element_to_be_clickable(
                    (By.ID, "continue")
                )
            )

            driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                continue_button
            )

            continue_button.click()

            print("DEBUG: Continue clicked")


            wait.until(
                EC.url_contains(
                    "checkout-step-two.html"
                )
            )

            print("DEBUG: Step two page loaded")


            # =========================
            # FINISH
            # =========================

            finish_button = wait.until(
                EC.element_to_be_clickable(
                    (By.ID, "finish")
                )
            )

            finish_button.click()

            print("DEBUG: Finish clicked")


            confirmation = wait.until(
                EC.presence_of_element_located(
                    (By.CLASS_NAME, "complete-header")
                )
            ).text


            print(
                "DEBUG: Confirmation text:",
                confirmation
            )


            return {
                "status": "success",
                "product": product_name,
                "confirmation": confirmation
            }


        except Exception as e:

            print(
                "DEBUG ERROR:",
                str(e)
            )

            return {
                "status": "error",
                "message": str(e)
            }