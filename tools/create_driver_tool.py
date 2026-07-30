from crewai.tools import BaseTool
from tools.driver_manager import DriverManager

class CreateDriverTool(BaseTool):
    name: str = "create_driver"
    description: str = "Creates and returns a Selenium WebDriver using DriverManager."

    model_config = {
        "arbitrary_types_allowed": True
    }

    def _run(self):
        driver = DriverManager.get_driver()
        return driver