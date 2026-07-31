import pytest

from utils.selenium_manager import SeleniumManager


@pytest.fixture(autouse=True)
def cleanup_driver():

    yield

    SeleniumManager.quit_driver()