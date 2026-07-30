from qa_flow import SauceDemoFlow


if __name__ == "__main__":

    flow = SauceDemoFlow()

    flow.kickoff()

    print("\n========== FINAL QA REPORT ==========\n")

    print(flow.state.final_report)