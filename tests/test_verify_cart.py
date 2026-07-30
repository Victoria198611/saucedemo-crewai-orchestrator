import allure

from tools.valid_login_flow_tool import ValidLoginFlowTool
from tools.add_to_cart_flow_tool import AddToCartFlowTool
from tools.verify_cart_flow_tool import VerifyCartFlowTool


@allure.feature("Cart")
@allure.story("Verify Product In Cart")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description(
    "Verify that added product is displayed correctly in the shopping cart."
)
def test_verify_cart():

    login_result = ValidLoginFlowTool().run()

    assert login_result["status"] == "success"


    add_result = AddToCartFlowTool().run(
        "Sauce Labs Backpack"
    )

    assert add_result["status"] == "success"


    result = VerifyCartFlowTool().run(
        "Sauce Labs Backpack"
    )

    assert result["status"] == "success"