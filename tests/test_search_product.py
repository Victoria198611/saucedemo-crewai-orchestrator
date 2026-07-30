import allure

from tools.valid_login_flow_tool import ValidLoginFlowTool


@allure.feature("Authentication")
@allure.story("Valid user login")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description(
    "Verify that valid user can login successfully into SauceDemo."
)
def test_valid_login():

    result = ValidLoginFlowTool().run()

    assert result["status"] == "success"