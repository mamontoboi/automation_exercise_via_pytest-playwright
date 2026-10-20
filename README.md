# Automation Exercise – Pytest + Playwright

[![UI & API Tests](https://github.com/mamontoboi/automation_exercise_via_pytest-playwright/actions/workflows/tests.yml/badge.svg)](https://github.com/mamontoboi/automation_exercise_via_pytest-playwright/actions/workflows/tests.yml)

[![Latest Allure Report](https://img.shields.io/badge/Allure-Latest%20Report-green)](https://mamontoboi.github.io/automation_exercise_via_pytest-playwright/)

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

The image contains the code and dependencies but **not** `.env` (see `.dockerignore`), so credentials are passed at runtime:

```bash
docker run --rm --env-file .env automation-tests
```

`.env` format for `--env-file`: plain `KEY=value` lines, **no quotes** and no `export` (Docker keeps quotes literally). Spaces inside a value are fine, e.g. `NAME=John Doe`.

Without a `.env` file, pass the values explicitly and quote any value containing spaces:

```bash
docker run --rm -e NAME="John Doe" -e EMAIL=john@test.com -e PASSWORD=secret automation-tests
```

### Run a subset

Anything after the image name replaces the default command (`uv run pytest`):

```bash
docker run --rm --env-file .env automation-tests uv run pytest -m api -n auto
docker run --rm --env-file .env automation-tests uv run pytest -m "smoke or ui"
```

### Get reports out of the container

Mount the output folders, then open the report on the host with `allure generate` / `allure open`:

```bash
docker run --rm --env-file .env \
  -v "$(pwd)/reports:/app/reports" \
  -v "$(pwd)/allure-results:/app/allure-results" \
  automation-tests uv run pytest --alluredir=/app/allure-results
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
