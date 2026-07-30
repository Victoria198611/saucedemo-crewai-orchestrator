import allure

from tools.valid_login_flow_tool import ValidLoginFlowTool
from tools.search_product_flow_tool import SearchProductFlowTool


@allure.feature("Product")
@allure.story("Search Product")
def test_search_product():

    with allure.step("Login to SauceDemo"):
        login_result = ValidLoginFlowTool().run()

    assert login_result["status"] == "success"


    with allure.step("Search Sauce Labs Backpack"):
        result = SearchProductFlowTool().run(
            "Sauce Labs Backpack"
        )


    with allure.step("Verify product exists"):
        assert result["status"] == "success"