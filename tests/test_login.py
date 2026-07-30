import allure

from tools.valid_login_flow_tool import ValidLoginFlowTool


@allure.feature("Authentication")
@allure.story("Valid user login")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Verify that valid user can login into SauceDemo.")
def test_valid_login():

    with allure.step("Execute valid login flow"):
        result = ValidLoginFlowTool().run()

    with allure.step("Verify login status"):
        assert result["status"] == "success"