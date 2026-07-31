# Smart Expense Tracker API

## Overview

The **Smart Expense Tracker API** is a RESTful web service developed using **FastAPI** that helps users manage their personal expenses efficiently. The application allows users to create, view, filter, calculate, and delete expense records while storing all data in a local JSON file. No external database is required, making the application lightweight, easy to set up, and suitable for learning REST API development.

This project demonstrates the implementation of RESTful API principles, request validation, automated testing, and JSON-based data persistence using Python.

---

# Features

The API provides the following functionalities:

- Add a new expense
- View all recorded expenses
- Filter expenses by category
- Calculate the total amount of all expenses
- Calculate category-wise expense totals
- Delete an expense by ID
- Automatic request validation using Pydantic
- JSON-based data storage (No database required)
- Interactive Swagger UI documentation
- Automated API testing using Pytest

---

# Technology Stack

The project was built using the following technologies:

- **Programming Language:** Python 3.10+
- **Framework:** FastAPI
- **ASGI Server:** Uvicorn
- **Data Validation:** Pydantic
- **Testing Framework:** Pytest
- **Storage:** Local JSON File

---

# Project Structure

```
your-repo/
│
├── README.md
├── AI_NOTES.md
├── requirements.txt
├── Dockerfile
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

# Installation

## Step 1: Clone the Repository

```bash
git clone <repository-url>
```

## Step 2: Navigate to the Project Directory

```bash
cd your-repo
```

## Step 3: Install the Required Dependencies

```bash
pip install -r requirements.txt
```

---

# Starting the Server

Start the FastAPI application using Uvicorn:

```bash
uvicorn src.main:app --reload
```

After the server starts successfully, the API will be available at:

```
http://127.0.0.1:8000
```

---

# API Documentation

FastAPI automatically generates interactive API documentation.

Swagger UI:

```
http://127.0.0.1:8000/docs
```

Alternative ReDoc documentation:

```
http://127.0.0.1:8000/redoc
```

These interfaces allow users to test every endpoint directly from the browser without requiring Postman.

---

# Running the Test Suite

This project includes automated API tests written using **Pytest**.

Run all tests:

```bash
pytest
```

Run tests with verbose output:

```bash
pytest -v
```


---

# Available API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | Welcome endpoint |
| POST | `/post-expenses` | Add a new expense |
| GET | `/Get-expenses` | Retrieve all expenses |
| GET | `/expenses/category/{category}` | Retrieve expenses by category |
| GET | `/expenses/total` | Calculate overall expenses |
| GET | `/expenses/total/{category}` | Calculate category-wise expenses |
| DELETE | `/expenses/{expense_id}` | Delete an expense using its ID |

---

# Data Storage

Expense records are stored inside a local JSON file named:

```
expenses.json
```

Each expense contains:

- Expense ID
- Title
- Amount
- Category
- Date

Example:

```json
{
    "id": 1,
    "title": "Lunch",
    "amount": 250,
    "category": "Food",
    "date": "2026-07-31"
}
```

---

# Request Validation

The application uses **Pydantic** models for automatic request validation.

The following validations are performed automatically:

- Required fields must be present.
- Amount must be a valid numeric value.
- Date must follow the `YYYY-MM-DD` format.
- Invalid request bodies return appropriate validation errors.

Example HTTP status codes:

| Status Code | Meaning |
|-------------|---------|
| 200 | Successful request |
| 404 | Resource not found |
| 422 | Invalid request or validation error |

---

# Testing

The project contains comprehensive automated tests covering both positive and negative scenarios.

### Positive Test Cases

- Home endpoint
- Add expense
- Retrieve all expenses
- Filter expenses by category
- Calculate total expenses
- Calculate category totals
- Delete an expense

### Negative Test Cases

- Missing required fields
- Invalid data types
- Invalid delete ID
- Invalid category
- Validation errors
- Non-existent resources

All tests were executed successfully using Pytest before submission.

---

# Design Decisions

- FastAPI was selected for its simplicity, performance, and automatic API documentation.
- A JSON file was used instead of a database because the assignment explicitly allowed local file storage.
- Pydantic models provide automatic validation without requiring manual input checks.
- Pytest and FastAPI's TestClient were used to create automated endpoint tests.

---

# Future Improvements

Possible enhancements include:

- Update Expense endpoint (PUT)
- Search expenses by title
- Monthly expense summary
- User authentication
- Database integration (SQLite/PostgreSQL)
- Docker containerization
- Expense analytics and visualization

---

# Author

Developed as part of the **Apprentice Assignment** using Python, FastAPI, and Pytest.

The project demonstrates REST API development, request validation, automated testing, JSON-based data management, and clean API design.
