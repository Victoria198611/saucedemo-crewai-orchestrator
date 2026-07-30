import allure

from tools.valid_login_flow_tool import ValidLoginFlowTool
from tools.add_to_cart_flow_tool import AddToCartFlowTool
from tools.checkout_flow_tool import CheckoutFlowTool


@allure.feature("Checkout")
@allure.story("Complete Order")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description(
    "Verify that user can add a product to cart and complete checkout successfully."
)
def test_checkout():

    login_result = ValidLoginFlowTool().run()

    assert login_result["status"] == "success"


    add_result = AddToCartFlowTool().run(
        "Sauce Labs Backpack"
    )

    assert add_result["status"] == "success"


    result = CheckoutFlowTool().run(
        product_name="Sauce Labs Backpack",
        first_name="Test",
        last_name="User",
        postal_code="12345"
    )


    assert result["status"] == "success"