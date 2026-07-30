import allure

from tools.valid_login_flow_tool import ValidLoginFlowTool
from tools.add_to_cart_flow_tool import AddToCartFlowTool


@allure.feature("Cart")
@allure.story("Add Product To Cart")
def test_add_to_cart():

    with allure.step("Login to SauceDemo"):
        login_result = ValidLoginFlowTool().run()

    assert login_result["status"] == "success"


    with allure.step("Add Sauce Labs Backpack to cart"):
        result = AddToCartFlowTool().run(
            "Sauce Labs Backpack"
        )


    with allure.step("Verify product was added"):
        assert result["status"] == "success"