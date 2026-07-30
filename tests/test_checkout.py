import allure

from tools.valid_login_flow_tool import ValidLoginFlowTool
from tools.add_to_cart_flow_tool import AddToCartFlowTool
from tools.checkout_flow_tool import CheckoutFlowTool


@allure.feature("Checkout")
@allure.story("Complete Order")
def test_checkout():

    with allure.step("Login to SauceDemo"):
        login_result = ValidLoginFlowTool().run()

    assert login_result["status"] == "success"


    with allure.step("Add product to cart"):
        add_result = AddToCartFlowTool().run(
            "Sauce Labs Backpack"
        )

    assert add_result["status"] == "success"


    with allure.step("Complete checkout"):
        result = CheckoutFlowTool().run(
            product_name="Sauce Labs Backpack",
            first_name="Test",
            last_name="User",
            postal_code="12345"
        )


    with allure.step("Verify order confirmation"):
        assert result["status"] == "success"