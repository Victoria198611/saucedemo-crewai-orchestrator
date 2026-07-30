from pydantic import BaseModel

from crewai.flow.flow import Flow, start, listen

from tools.valid_login_flow_tool import ValidLoginFlowTool
from tools.search_product_flow_tool import SearchProductFlowTool
from tools.add_to_cart_flow_tool import AddToCartFlowTool
from tools.verify_cart_flow_tool import VerifyCartFlowTool
from tools.checkout_flow_tool import CheckoutFlowTool


class SauceDemoState(BaseModel):

    login: dict = {}
    search: dict = {}
    cart: dict = {}
    verify: dict = {}
    final_report: dict = {}



class SauceDemoFlow(Flow[SauceDemoState]):


    @start()
    def login(self):

        print("STEP 1: LOGIN")

        result = ValidLoginFlowTool().run()

        self.state.login = result

        return result



    @listen(login)
    def search_product(self, login_result):

        print("STEP 2: SEARCH PRODUCT")


        if login_result["status"] != "success":

            self.state.search = {
                "status": "failed",
                "message": "Login failed"
            }

            return self.state.search



        result = SearchProductFlowTool().run(
            product_name="Sauce Labs Backpack"
        )


        self.state.search = result

        return result




    @listen(search_product)
    def add_to_cart(self, search_result):

        print("STEP 3: ADD CART")


        if search_result["status"] != "success":

            self.state.cart = {
                "status": "failed"
            }

            return self.state.cart



        result = AddToCartFlowTool().run(
            product_name="Sauce Labs Backpack"
        )


        self.state.cart = result

        return result




    @listen(add_to_cart)
    def verify_cart(self, cart_result):

        print("STEP 4: VERIFY CART")


        result = VerifyCartFlowTool().run(
            product_name="Sauce Labs Backpack"
        )


        self.state.verify = result

        return result




    @listen(verify_cart)
    def checkout(self, verify_result):

        print("STEP 5: CHECKOUT")


        if verify_result["status"] != "success":

            self.state.final_report = {
                "status": "failed",
                "message": "Product not in cart"
            }

            return self.state.final_report



        result = CheckoutFlowTool().run(
            product_name="Sauce Labs Backpack",
            first_name="Test",
            last_name="User",
            postal_code="12345"
        )


        self.state.final_report = result

        return result