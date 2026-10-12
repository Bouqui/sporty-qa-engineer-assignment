# Sporty QA Engineer Assignment

This repository contains automated QA tests for a sports betting web application. The project validates key betting workflows through both browser-based UI automation and API-level checks using Python, Selenium, and pytest.

## Overview

The assignment focuses on verifying that a user can successfully place a valid bet and that invalid requests are rejected appropriately.

The repository includes:

- UI end-to-end tests for placing a single bet
- API tests for validating request handling and authorization
- A Page Object Model (POM) implementation for cleaner, reusable UI automation

## Repository Structure

```text
.
├── pages/
│   └── betting_page.py
├── tests/
│   ├── api/
│   │   └── test_place_bet_api.py
│   ├── ui/
│   │   └── test_place_bet.py
│   └── conftest.py
├── utils/
│   └── config.py
├── .gitignore
├── pytest.ini
├── requirements.txt
├── README.md
└── .idea/
```

## Test Coverage

### UI Test

File: `tests/ui/test_place_bet.py`

This test verifies the main E2E bet placement flow:

- opens the app with a valid user session
- reads the initial balance
- selects a valid HOME odds selection
- enters a stake
- confirms the payout is calculated correctly
- clicks the place bet button
- validates the success receipt details
- confirms the balance updates after the stake is deducted

### API Test

File: `tests/api/test_place_bet_api.py`

This test validates the API contract:

- fetches an existing match using a valid user identity
- attempts to place a bet without the required `x-user-id` header
- expects a `401 Unauthorized` response

## Tech Stack

- Python
- pytest
- Selenium WebDriver
- requests

## Prerequisites

Before running the tests, make sure you have:

- Python 3 installed
- Google Chrome installed
- ChromeDriver available on your system PATH

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Bouqui/sporty-qa-engineer-assignment.git
cd sporty-qa-engineer-assignment
```

2. Create and activate a virtual environment (recommended):

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows:

```bash
.venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

The app URL and test user details are configured in `utils/config.py`:

```python
BASE_URL = "https://qae-assignment-tau.vercel.app"
USER_ID = "candidate-jNAjixEsnebd"
APP_URL = f"{BASE_URL}/?user-id={USER_ID}"
```

## Running Tests

Run the entire suite:

```bash
pytest
```

Run only UI tests:

```bash
pytest tests/ui
```

Run only API tests:

```bash
pytest tests/api
```

## Notes

This project uses a simple Page Object Model in `pages/betting_page.py` to encapsulate the UI behavior, making the tests easier to read and maintain. It is designed as a practical QA assignment focused on validating a sports betting workflow under realistic product conditions.
