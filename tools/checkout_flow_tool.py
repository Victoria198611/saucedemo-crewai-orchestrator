class CheckoutFlowTool(BaseTool):

    name: str = "checkout_flow"
    description: str = "Complete checkout after product was verified in cart."

    def _run(
            self,
            product_name: str = "Sauce Labs Backpack",
            first_name: str = "Test",
            last_name: str = "User",
            postal_code: str = "12345"
    ):

        try:
            driver = SeleniumManager.get_driver()

            # go checkout
            checkout_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "checkout"))
            )
            checkout_button.click()

            # customer info
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "first-name"))
            )

            driver.find_element(By.ID, "first-name").send_keys(first_name)
            driver.find_element(By.ID, "last-name").send_keys(last_name)
            driver.find_element(By.ID, "postal-code").send_keys(postal_code)

            driver.find_element(By.ID, "continue").click()

            # wait for finish button
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