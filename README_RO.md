# SauceDemo CrewAI Selenium Orchestrator

![QA Automation](https://github.com/Victoria198611/saucedemo-crewai-orchestrator/actions/workflows/qa.yml/badge.svg)
Proiect de automatizare QA asistat de AI folosind:

- Python
- Selenium WebDriver
- CrewAI
- Ollama Local LLM
- CI/CD
- Allure Reporting

---

# Descriere

Acest proiect implementează un orchestrator QA bazat pe CrewAI care execută automat un scenariu complet de cumpărare în aplicația SauceDemo.

Fluxul automatizat verifică întregul proces de shopping:

1. Login valid
2. Căutare produs
3. Adăugare produs în coș
4. Verificare produs în coș
5. Finalizare checkout
6. Generare rezultat QA

Aplicație testată:

https://www.saucedemo.com/

---
# Arhitectură

main.py
|
v
qa_flow.py
|
+--> agents.py
|
+--> tools/
| |
| +--> valid_login_flow_tool.py
| +--> search_product_flow_tool.py
| +--> add_to_cart_flow_tool.py
| +--> verify_cart_flow_tool.py
| +--> checkout_flow_tool.py
|
+--> services/
|
+--> selenium_manager.py

---
# Tehnologii utilizate

## Python

Limbaj principal pentru implementarea framework-ului de automatizare.

## Selenium WebDriver

Folosit pentru controlul browserului și executarea acțiunilor UI:

- deschidere aplicație
- login
- navigare produse
- coș cumpărături
- checkout

## CrewAI

Folosit pentru orchestrarea agenților și task-urilor QA.

Fluxul este împărțit în pași independenți:

- Login Agent
- Product Search Agent
- Cart Agent
- Checkout Agent

## Ollama

Model LLM local utilizat pentru rularea agenților AI fără dependență de servicii cloud.

---
# Scenariu automatizat

User:

username:
standard_user

password:
secret_sauce

Produs verificat:

Sauce Labs Backpack

Flux:
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

---
# Selenium Driver Management
Driver-ul browserului este gestionat centralizat prin:
services/selenium_manager.py

Acesta asigură:

- creare driver
- reutilizare sesiune Selenium
- închidere controlată

---
# CI/CD

Proiectul poate fi integrat într-un pipeline CI/CD folosind GitHub Actions.

Pipeline-ul execută automat:

1. Checkout cod sursă
2. Instalare dependințe Python
3. Configurare mediu de test
4. Executare QA Flow
5. Validare rezultat

Exemplu workflow:


.github/
|
+-- workflows/
|
+-- qa.yml

Pipeline-ul permite rularea automată la:

- push
- pull request
- manual trigger

---
# Allure Reporting
Proiectul suportă integrarea cu Allure pentru generarea rapoartelor QA.

Allure oferă:
- status teste
- pași executați
- atașamente
- rezultate vizuale

Flux:
Test Execution
|
v
Allure Results
|
v
Allure Report

Comenzi:
Generare rezultate:
pytest --alluredir=allure-results:

Pornire raport:
allure serve allure-results

---
# Instalare

Clone repository:
git clone <repository-url>

Instalare dependințe:

pip install -r requirements.txt
Pornire Ollama:
ollama run qwen2.5:14b-instruct

Rulare proiect:
python main.py

---
# Rezultat exemplu

```json
{
  "status": "success",
  "product": "Sauce Labs Backpack",
  "confirmation": "Thank you for your order!"
}
Scop proiect

Proiectul demonstrează integrarea dintre:

AI Agents
QA Automation
Selenium
Workflow orchestration
CI/CD concepts
Test Reporting

Autor

QA Automation Engineer | Java, Python, Selenium, CrewAI
GitHub: github.com/Victoria198611