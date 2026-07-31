# Personal Expense Tracker API

## Overview

This project is a REST API built using **FastAPI** to manage personal expenses. It stores expense data in a local JSON file and supports basic CRUD operations.

## Features

- Add a new expense
- View all expenses
- Filter expenses by category
- Calculate total expenses
- Calculate total expenses by category
- Delete an expense
- Automatic request validation using Pydantic
- Automated API testing using Pytest

---

## Tech Stack

- Python 3.10+
- FastAPI
- Uvicorn
- Pydantic
- Pytest

---

## Project Structure

```
your-repo/
│
├── README.md
├── AI_NOTES.md
├── requirements.txt
│
├── src/
│   ├── __init__.py
│   └── main.py
│
└── tests/
    ├── __init__.py
    └── test_api.py
```

---

## Installation

Clone the repository

```bash
git clone <repository-url>
```

Navigate to the project directory

```bash
cd your-repo
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Start the Server

Run the FastAPI application using:

```bash
uvicorn src.main:app --reload or Python main.py
```

The application will be available at:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

---

## Run the Test Suite

Execute the following command:

```bash
pytest
```

or for detailed output:

```bash
pytest -v
```

---

## API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | Welcome API |
| POST | `/post-expenses` | Add Expense |
| GET | `/Get-expenses` | View All Expenses |
| GET | `/expenses/category/{category}` | Filter by Category |
| GET | `/expenses/total` | Total Expenses |
| GET | `/expenses/total/{category}` | Category Total |
| DELETE | `/expenses/{expense_id}` | Delete Expense |

---

## Validation

The API uses **Pydantic** for request validation.

Invalid requests automatically return:

- **422 Unprocessable Entity**

Examples include:

- Missing required fields
- Invalid data types
- Invalid date format

---

## Testing

The project includes automated tests for:

- Home Endpoint
- Add Expense
- Get All Expenses
- Filter by Category
- Total Expenses
- Category Total
- Delete Expense
- Validation Errors
- Invalid Category
- Invalid Delete ID

---

