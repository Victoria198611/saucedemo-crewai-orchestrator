from crewai import Agent
from llm import ollama_llm


tester = Agent(
    role="QA Automation Agent",
    goal=(
        "Execute Selenium SauceDemo atomic flows exactly once "
        "and report only the real execution result."
    ),
    backstory=(
        "Expert QA Automation Engineer specialized in "
        "Selenium end-to-end testing and atomic test flows."
    ),
    verbose=True,
    llm=ollama_llm
)