# Automation Exercise – Pytest + Playwright

This repository contains a test automation project built with **Python**, **pytest**, and **Playwright**. It covers both **UI** and **API** testing for the public demo application [**automationexercise.com**](https://automationexercise.com/) and demonstrates modern automation practices used in real-world projects.

---

## 📌 Project Goals

- Demonstrate practical experience with **Playwright (Python)**
- Use **pytest** as the main test runner
- Apply **Page Object Model (POM)** for UI tests
- Combine **UI and API automation** in a single test suite
- Showcase best practices: fixtures, markers, parallel runs, traces, screenshots, CI readiness

---

## 🧪 Test Coverage

### UI Tests (Playwright)

- User registration
- Login (positive and negative scenarios)
- Contact Us form
- Navigation and content validation
- Subscription

### API Tests (Requests)

- Get all products list
- Search products by text
- Validate response schema and business rules
- Verify negative cases (unsupported HTTP methods, missing params)
- Login (positive and negative scenarios)

---

## 🛠️ Tech Stack

- **Python 3.14+**
- **pytest** – test framework
- **Playwright (sync API)** – UI automation
- **requests** – API testing
- **pytest-xdist** – parallel execution
- **pytest-html** – HTML reports
- **Allure Report** – rich execution reports and history
- **Ruff** – static analysis / linting
- **uv** – dependency management
- **Docker** – containerized execution

---

## 📁 Project Structure

```
automation_exercise_via_pytest-playwright/
│
├── config/              # Paths, constants, configuration
├── endpoints/           # API endpoint abstractions
├── fixtures/            # Reusable pytest fixtures (users, data)
├── pages/               # Page Object Model (Playwright pages)
├── tests/
│   ├── ui/              # UI tests
│   └── api/             # API tests
│
├── reports/             # Screenshots, traces, HTML reports
├── pyproject.toml       # pytest & tool configuration
├── Dockerfile           # Docker image for test execution
└── README.md
```

---

## ▶️ How to Run Tests Locally

### 1. Install dependencies

```bash
uv sync
```

### 2. Run all tests

```bash
pytest
```

### 3. Run UI tests only

```bash
pytest -m ui
```

### 4. Run API tests only

```bash
pytest -m api
```

### 5. Run Smoke tests only

```bash
pytest -m smoke
```

### 6. Run tests in parallel

```bash
pytest -n auto
```

---

## � Allure Reporting

This project can generate rich Allure reports for both UI and API suites.

### Generate a local Allure report

```bash
pytest --alluredir=allure-results
allure generate allure-results -o allure-report --clean
allure open allure-report
```

### CI / GitHub Actions

The workflow uploads:

- raw Allure result files as artifacts
- a generated HTML Allure report for each suite
- a merged Allure report that combines UI and API execution results

You can inspect the generated report from the workflow artifacts after a run.

---

## �📸 Diagnostics on Failures

- **Screenshots** are captured automatically for failed UI tests
- **Playwright traces** can be enabled to debug failures
- HTML report is generated after test execution

Artifacts are stored under:

```
reports/
├── screenshots/
├── traces/
└── html/
```

---

## 🧷 Pytest Markers

Defined markers:

- `@pytest.mark.ui` – UI tests
- `@pytest.mark.api` – API tests
- `@pytest.mark.smoke` – critical smoke tests

Markers are validated using `--strict-markers`.

---

## 🐳 Docker Support

The project can be executed inside a Docker container based on the official Playwright Python image.

### Build image

```bash
docker build -t automation-tests .
```

### Run tests

```bash
docker run --rm automation-tests
```

---

## 🔄 CI / GitHub Actions

The project structure and configuration are suitable for CI pipelines:

- Headless execution
- Parallel runs
- Artifacts (reports, screenshots)
- Deterministic dependency installs

---

## 🎯 What This Project Demonstrates

- Real Playwright automation experience with Python
- UI & API test design
- Test scalability and maintainability
- Clean architecture (fixtures, POM, endpoints)
- Debugging strategies (traces, screenshots)
- CI/CD awareness and Dockerization

---

## 📌 Notes

This project uses **automationexercise.com** as a public demo application. All tests are written for educational and portfolio purposes.
