import pytest

from services.selenium_manager import SeleniumManager

@pytest.fixture(autouse=True)
def cleanup_driver():

    yield

    SeleniumManager.quit_driver()