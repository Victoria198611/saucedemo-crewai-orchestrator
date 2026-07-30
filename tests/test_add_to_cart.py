import allure

from tools.valid_login_flow_tool import ValidLoginFlowTool
from tools.add_to_cart_flow_tool import AddToCartFlowTool


@allure.feature("Cart")
@allure.story("Add Product To Cart")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description(
    "Verify that user can add a product to the shopping cart."
)
def test_add_to_cart():

    login_result = ValidLoginFlowTool().run()

    assert login_result["status"] == "success"


    result = AddToCartFlowTool().run(
        "Sauce Labs Backpack"
    )


    assert result["status"] == "success"