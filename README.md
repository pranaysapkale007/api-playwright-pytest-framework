# Playwright + Python API Automation Framework

## 📌 Overview
This project is a **mini API automation framework** built with **Playwright + Python + Pytest**.  
It demonstrates framework design concepts like fixtures, reusable utilities, validators, test data management, reporting, logging, retry logic, and schema validation.

The framework tests the **ReqRes API** (https://reqres.in), a free REST API for practice.

---

## 🏗 Project Structure
api_framework/
├── config/             # Config & test data
│   ├── config.json
│   └── test_data.json
├── reports/            # HTML reports & logs
│   └── logs/framework.log
├── tests/              # Test cases organized by modules
│   ├── users/
│   └── auth/
├── utils/              # Utilities (API client, validators, logger, etc.)
├── conftest.py         # Pytest fixtures
├── requirements.txt    # Dependencies
└── README.md           # Project documentation


---

## 🚀 How to Run
1. Clone the repo:
   ```bash
   git clone https://github.com/<your-username>/api-framework.git
   cd api-framework

2. Create virtual environment:
    python -m venv venv
    source venv/bin/activate   # Mac/Linux
    venv\Scripts\activate      # Windows

3. Install dependencies:
    pip install -r requirements.txt
    playwright install

4. Run Tests:
    pytest -v

5. Generate HTML report:
    pytest --html=reports/report.html --self-contained-html

🧩 Features
✅ Configurable base URL & headers

✅ Reusable API client (GET, POST, PUT, DELETE)

✅ Validators for assertions

✅ Test data management (JSON + parameterization)

✅ Reporting with pytest-html

✅ Logging to console + file

✅ Retry logic for flaky APIs

✅ Schema validation with jsonschema

✅ Organized test modules

📊 Sample Test Cases
GET Users → Validate response list

POST Create User → Validate creation response

PUT Update User → Validate update response

DELETE User → Validate deletion response

Login → Positive & negative scenarios