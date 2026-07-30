# SauceDemo CrewAI Selenium Orchestrator

![QA Automation](https://github.com/Victoria198611/saucedemo-crewai-orchestrator/actions/workflows/qa.yml/badge.svg)

AI-assisted QA automation project using:

- Python
- Selenium WebDriver
- CrewAI
- CrewAI Flow
- Ollama Local LLM (Qwen 2.5)

---

# Description

This project implements an AI-assisted QA automation workflow using CrewAI orchestration and Selenium WebDriver.

The execution flow is managed by CrewAI Flow, while Selenium performs browser automation actions against the SauceDemo web application.

The automated workflow validates a complete shopping scenario:

1. Valid login
2. Product search
3. Add product to cart
4. Cart verification
5. Checkout completion
6. Final QA execution report

Application under test:

```text
https://www.saucedemo.com/
```

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
├── tools/
│   ├── valid_login_flow_tool.py
│   ├── search_product_flow_tool.py
│   ├── add_to_cart_flow_tool.py
│   ├── verify_cart_flow_tool.py
│   └── checkout_flow_tool.py
│
└── .github/
    └── workflows/
        └── qa.yml
```

---

# Automated Scenario

## Application

```text
SauceDemo
https://www.saucedemo.com/
```

## Test Credentials

```text
username: standard_user
password: secret_sauce
```

## Test Product

```text
Sauce Labs Backpack
```

## Execution Flow

```text
LOGIN
  |
  v
SEARCH PRODUCT
  |
  v
ADD TO CART
  |
  v
VERIFY CART
  |
  v
CHECKOUT
  |
  v
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

The project uses centralized Selenium driver management:

```text
services/
    selenium_manager.py
```

Responsibilities:

- Browser driver creation
- Browser lifecycle management
- Driver cleanup
- Selenium session reuse

---

# CrewAI Workflow

The QA execution is divided into atomic automation tools.

## Valid Login Tool

Responsibilities:

- Open SauceDemo application
- Enter valid credentials
- Validate successful authentication


## Search Product Tool

Responsibilities:

- Load available products
- Search requested product
- Validate product existence


## Add To Cart Tool

Responsibilities:

- Select exact product
- Add product to shopping cart


## Verify Cart Tool

Responsibilities:

- Open shopping cart
- Confirm product presence


## Checkout Tool

Responsibilities:

- Complete checkout information
- Finish order process
- Validate confirmation message

---

# Running The Project

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

The project includes GitHub Actions CI integration.

Workflow location:

```text
.github/
└── workflows/
    └── qa.yml
```

The pipeline executes automatically on:

- push to main branch
- pull requests

Pipeline steps:

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
Checkout Source Code
        |
        v
Install Python Dependencies
        |
        v
Configure Test Environment
        |
        v
Execute QA Automation Flow
        |
        v
Validate Execution Result
```

CI/CD technologies:

- GitHub Actions
- Jenkins (future integration)
- GitLab CI (future integration)

---

# Test Reporting - Allure

The project architecture allows future integration with Allure Reporting.

Planned reporting flow:

```text
QA Execution
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

Allure integration can provide:

- Test execution history
- Step-by-step execution details
- Screenshots on failures
- Error information
- Execution statistics

Recommended stack:

- pytest
- allure-pytest
- GitHub Actions artifacts

---

# Future Improvements

Possible improvements:

- Add pytest test layer
- Add Allure reporting integration
- Add screenshots on Selenium failures
- Add advanced CI/CD stages
- Add environment configuration
- Add parallel browser execution
- Add Docker execution environment

---

# Notes

This project demonstrates an AI-assisted QA automation workflow combining:

- Browser automation with Selenium
- AI agent orchestration with CrewAI
- Local LLM execution with Ollama
- Structured QA workflow management
- Continuous Integration concepts

The final result is an automated end-to-end shopping validation flow for SauceDemo.

---

# Author

QA Automation Project

Built with:

- Python
- Selenium
- CrewAI
- Ollama
- GitHub Actions