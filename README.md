# SauceDemo CrewAI Selenium Orchestrator

AI-assisted QA automation project using:

- Python
- Selenium WebDriver
- CrewAI
- CrewAI Flow
- Ollama local LLM (Qwen 2.5)

---

# Description

This project automates a complete shopping workflow on SauceDemo using an AI-assisted QA orchestration approach.

The execution flow is managed by CrewAI Flow, while Selenium WebDriver performs browser automation actions.

The workflow covers:

1. Valid login
2. Product search
3. Add product to cart
4. Cart verification
5. Checkout completion
6. Final QA execution report

---

# Architecture

```text
main.py
   |
   v
qa_flow.py
   |
   +--> agents.py
   |
   +--> llm.py
   |
   +--> tasks.py
   |
   +--> tools/
   |
   +--> services/
```

---

# Project Structure

```text
saucedemo-crewai-orchestrator

├── main.py
├── qa_flow.py
├── agents.py
├── llm.py
├── tasks.py
├── requirements.txt
├── README.md
│
├── services/
│   └── selenium_manager.py
│
└── tools/
    ├── valid_login_flow_tool.py
    ├── search_product_flow_tool.py
    ├── add_to_cart_flow_tool.py
    ├── verify_cart_flow_tool.py
    └── checkout_flow_tool.py
```

---

# Automated Scenario

Application:

```text
https://www.saucedemo.com/
```

Test credentials:

```text
username: standard_user
password: secret_sauce
```

Test product:

```text
Sauce Labs Backpack
```

Execution flow:

```text
LOGIN
  |
SEARCH PRODUCT
  |
ADD TO CART
  |
VERIFY CART
  |
CHECKOUT
  |
FINAL QA REPORT
```

---

# Technologies

## Automation

- Python 3.x
- Selenium WebDriver
- Google Chrome
- ChromeDriver

## AI Orchestration

- CrewAI Agents
- CrewAI Flow
- CrewAI Tools

## Local LLM

- Ollama
- Qwen 2.5 14B Instruct

---

# Selenium Management

The project uses a centralized Selenium manager:

```text
services/
    selenium_manager.py
```

Responsibilities:

- Browser lifecycle management
- Driver creation
- Driver cleanup

---

# CrewAI Workflow

The QA agent executes atomic automation tools:

## Valid Login Tool

Responsible for:

- Opening SauceDemo
- Entering credentials
- Validating successful authentication


## Search Product Tool

Responsible for:

- Loading products
- Searching requested product
- Validating product existence


## Add To Cart Tool

Responsible for:

- Selecting exact product
- Adding item to cart


## Verify Cart Tool

Responsible for:

- Opening cart
- Confirming product presence


## Checkout Tool

Responsible for:

- Completing checkout form
- Finishing order
- Validating confirmation message

---

# Run

## Install dependencies

```bash
pip install -r requirements.txt
```

---

## Start Ollama model

```bash
ollama run qwen2.5:14b-instruct
```

---

## Execute QA Flow

```bash
python main.py
```

---

# Execution Result

Successful execution example:

```json
{
  "status": "success",
  "product": "Sauce Labs Backpack",
  "confirmation": "Thank you for your order!"
}
```

---

# CI/CD Integration

The project is designed to be integrated into a CI/CD pipeline.

Recommended pipeline:

```text
Developer Commit
        |
        v
GitHub Repository
        |
        v
GitHub Actions
        |
        v
Install Dependencies
        |
        v
Start Test Environment
        |
        v
Execute QA Automation Flow
        |
        v
Generate Test Reports
```

Possible CI/CD technologies:

- GitHub Actions
- Jenkins
- GitLab CI

Future pipeline steps:

- Automated execution on every commit
- Dependency validation
- Browser automation execution
- Test artifact collection
- Report publishing

---

# Test Reporting - Allure

The project can be extended with Allure Reporting for detailed QA visibility.

Planned integration:

```text
Selenium Execution
        |
        v
Test Results
        |
        v
Allure Report
        |
        v
QA Dashboard
```

Allure reports can provide:

- Test execution history
- Step-by-step actions
- Execution timeline
- Screenshots on failures
- Error details
- Automation statistics

Recommended stack:

- pytest
- allure-pytest
- GitHub Actions

---

# Future Improvements

Possible improvements:

- Add pytest test layer
- Add Allure reporting
- Add GitHub Actions workflow
- Add screenshots on Selenium failures
- Add environment configuration
- Add parallel browser execution
- Add Docker execution environment

---

# Notes

This project demonstrates an AI-assisted QA automation workflow combining:

- Traditional browser automation
- AI agent orchestration
- Local LLM execution
- Structured QA reporting

The final result is an automated end-to-end shopping validation flow for SauceDemo.