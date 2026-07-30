from crewai import Task
from agents import tester

from tools.valid_login_flow_tool import ValidLoginFlowTool
from tools.search_product_flow_tool import SearchProductFlowTool
from tools.add_to_cart_flow_tool import AddToCartFlowTool
from tools.verify_cart_flow_tool import VerifyCartFlowTool
from tools.checkout_flow_tool import CheckoutFlowTool


# =========================
# VALID LOGIN
# =========================

valid_login_flow_task = Task(
    description=(
        "Execută login valid în SauceDemo.\n"
        "Confirmă că autentificarea a fost realizată cu succes."
    ),
    agent=tester,
    tools=[
        ValidLoginFlowTool()
    ],
    expected_output="""
    JSON:
    {
        "status": "success|failed",
        "message": "login result"
    }
    """,
    output_json=True
)


# =========================
# SEARCH PRODUCT
# =========================

search_product_flow_task = Task(
    description=(
        "Caută produsul Sauce Labs Backpack.\n"
        "Nu folosi alte produse."
    ),
    agent=tester,
    tools=[
        SearchProductFlowTool()
    ],
    context=[
        valid_login_flow_task
    ],
    expected_output="""
    JSON:
    {
        "status": "success|failed",
        "product": "Sauce Labs Backpack"
    }
    """,
    output_json=True
)


# =========================
# ADD TO CART
# =========================

add_to_cart_flow_task = Task(
    description=(
        "Adaugă în coș exact produsul:\n"
        "Sauce Labs Backpack\n\n"
        "Nu inventa produse."
    ),
    agent=tester,
    tools=[
        AddToCartFlowTool()
    ],
    context=[
        valid_login_flow_task,
        search_product_flow_task
    ],
    expected_output="""
    JSON:
    {
        "status": "success|failed",
        "added_product": "Sauce Labs Backpack"
    }
    """,
    output_json=True
)


# =========================
# VERIFY CART
# =========================

verify_cart_flow_task = Task(
    description=(
        "Verifică existența produsului Sauce Labs Backpack în coș."
    ),
    agent=tester,
    tools=[
        VerifyCartFlowTool()
    ],
    context=[
        add_to_cart_flow_task
    ],
    expected_output="""
    JSON:
    {
        "status": "success|failed",
        "verified_product": "Sauce Labs Backpack"
    }
    """,
    output_json=True
)


# =========================
# CHECKOUT
# =========================

checkout_flow_task = Task(
    description=(
        "Finalizează checkout pentru produsul Sauce Labs Backpack.\n"
        "Completează datele necesare și verifică mesajul final."
    ),
    agent=tester,
    tools=[
        CheckoutFlowTool()
    ],
    context=[
        verify_cart_flow_task
    ],
    expected_output="""
    JSON:
    {
        "status": "success|failed",
        "product": "Sauce Labs Backpack",
        "confirmation": "message"
    }
    """,
    output_json=True
)