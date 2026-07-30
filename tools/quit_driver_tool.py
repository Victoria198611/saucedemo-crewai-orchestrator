from crewai.tools import BaseTool
from tools.driver_manager import DriverManager

class QuitDriverTool(BaseTool):
    name: str = "quit_driver"
    description: str = "Closes the browser session."

    def _run(self):
        try:
            DriverManager.quit_driver()
            return "Browser closed successfully"
        except Exception as e:
            return f"Failed to close browser: {str(e)}"