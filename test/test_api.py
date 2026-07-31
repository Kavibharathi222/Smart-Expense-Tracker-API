import os
import json
from fastapi.testclient import TestClient
from src.main import app, JSON_FILE

client = TestClient(app)


def setup_function():
    with open(JSON_FILE, "w") as file:
        json.dump([], file)


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == "Welcome to Personal Expense Tracker API"


def test_add_expense():

    payloads= [
        {
        "title": "Lunch",
        "amount": 250,
        "category": "Food",
        "date": "2026-07-31"
        },
        {
           "title": "Movie",
            "amount": 250,
            "category": "Entertainment",
            "date": "2026-07-31" 
        }
    ]

    # response = client.post("/post-expenses", json=payload)

    for payload in payloads:
        response = client.post("/post-expenses", json=payload)
        assert response.status_code == 200
        data = response.json()

        assert data["message"] == "Expense added successfully"
        assert data["expense"]["title"] == payload["title"]
        assert data["expense"]["amount"] == payload["amount"]
        assert data["expense"]["category"] == payload["category"]


def test_get_all_expenses():

    payload = {
        "title": "Bus",
        "amount": 50,
        "category": "Travel",
        "date": "2026-07-31"
    }

    client.post("/post-expenses", json=payload)

    response = client.get("/Get-expenses")

    assert response.status_code == 200

    data = response.json()

    assert data["count"] == 1
    assert data["expenses"][0]["title"] == "Bus"


def test_filter_category():

    client.post(
        "/post-expenses",
        json={
            "title": "Lunch",
            "amount": 250,
            "category": "Food",
            "date": "2026-07-31"
        }
    )

    response = client.get("/expenses/category/Food")

    assert response.status_code == 200

    data = response.json()

    assert data["category"] == "Food"
    assert data["count"] == 1


def test_filter_category_not_found():

    response = client.get("/expenses/category/Shopping")

    assert response.status_code == 404
    assert response.json()["detail"] == "No expenses found for this category."


def test_total_expenses():

    client.post(
        "/post-expenses",
        json={
            "title": "Lunch",
            "amount": 250,
            "category": "Food",
            "date": "2026-07-31"
        }
    )

    client.post(
        "/post-expenses",
        json={
            "title": "Bus",
            "amount": 50,
            "category": "Travel",
            "date": "2026-07-31"
        }
    )

    response = client.get("/expenses/total")

    assert response.status_code == 200
    assert response.json()["total_expenses"] == 300


def test_total_by_category():

    client.post(
        "/post-expenses",
        json={
            "title": "Lunch",
            "amount": 250,
            "category": "Food",
            "date": "2026-07-31"
        }
    )

    client.post(
        "/post-expenses",
        json={
            "title": "Dinner",
            "amount": 150,
            "category": "Food",
            "date": "2026-07-31"
        }
    )

    client.post(
            "/post-expenses",
            json={
                "title": "Movie",
                "amount": 200,
                "category": "Entertainment",
                "date": "2026-07-31"
            }
        )

    response = client.get("/expenses/total/Food")

    assert response.status_code == 200

    data = response.json()

    assert data["category"] == "Food"
    assert data["total"] == 400


def test_delete_expense():

    client.post(
        "/post-expenses",
        json={
            "title": "Lunch",
            "amount": 250,
            "category": "Food",
            "date": "2026-07-31"
        }
    )

    response = client.delete("/expenses/1")

    assert response.status_code == 200
    assert response.json()["message"] == "Expense deleted successfully."


def test_delete_invalid_expense():

    response = client.delete("/expenses/100")

    assert response.status_code == 404
    assert response.json()["detail"] == "Expense not found."


def test_validation_error():

    payload = {
        "title": "Lunch",
        "amount": "ABC",
        "category": "Food",
        "date": "2026-07-31"
    }

    response = client.post("/post-expenses", json=payload)

    assert response.status_code == 422

def test_missing_category():
   
    payload = {
        "title": "Lunch",
        "amount": 250,
        "date": "2026-07-31"
    }

    response = client.post("/post-expenses", json=payload)

    assert response.status_code == 422

def test_delete_invalid_id():
    
    response = client.delete("/expenses/100")

    assert response.status_code == 404
    assert response.json()["detail"] == "Expense not found."
    