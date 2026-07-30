import allure

from tools.invalid_login_flow_tool import InvalidLoginFlowTool


@allure.feature("Authentication")
@allure.story("Invalid Login")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("Verify that login fails with invalid credentials.")
def test_invalid_login():

    with allure.step("Execute invalid login flow"):
        result = InvalidLoginFlowTool().run()

    with allure.step("Verify login failure"):
        assert result["status"] == "success"