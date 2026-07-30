import allure

from tools.valid_login_flow_tool import ValidLoginFlowTool
from tools.add_to_cart_flow_tool import AddToCartFlowTool
from tools.verify_cart_flow_tool import VerifyCartFlowTool


@allure.feature("Cart")
@allure.story("Verify Product In Cart")
def test_verify_cart():

    with allure.step("Login to SauceDemo"):
        login_result = ValidLoginFlowTool().run()

    assert login_result["status"] == "success"


    with allure.step("Add product to cart"):
        add_result = AddToCartFlowTool().run(
            "Sauce Labs Backpack"
        )

    assert add_result["status"] == "success"


    with allure.step("Verify product exists in cart"):
        result = VerifyCartFlowTool().run(
            "Sauce Labs Backpack"
        )


    with allure.step("Validate cart content"):
        assert result["status"] == "success"