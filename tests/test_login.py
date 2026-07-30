import allure

from tools.valid_login_flow_tool import ValidLoginFlowTool


@allure.feature("Login")
@allure.story("Valid user login")
def test_valid_login():

    with allure.step("Execute valid login flow"):

        result = ValidLoginFlowTool().run()

    assert result["status"] == "success"