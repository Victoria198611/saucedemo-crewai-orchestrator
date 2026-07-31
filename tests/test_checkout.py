import allure

from tools.full_checkout_flow_tool import FullCheckoutFlowTool


@allure.feature("Checkout")
@allure.story("Complete Order")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description(
    "Verify that user can add a product to cart and complete checkout successfully."
)
def test_checkout():

    result = FullCheckoutFlowTool().run(
        product_name="Sauce Labs Backpack",
        first_name="Test",
        last_name="User",
        postal_code="12345"
    )

    assert result["status"] == "success"