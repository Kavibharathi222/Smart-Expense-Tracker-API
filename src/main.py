from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import date
import json
import os

app = FastAPI(
    title="Personal Expense Tracker API",
    description="A simple REST API to manage personal expenses using a JSON file.",
    version="1.0.0"
)

JSON_FILE = "expenses.json"



if not os.path.exists(JSON_FILE):
    with open(JSON_FILE, "w") as file:
        json.dump([], file, indent=4)



class Expense(BaseModel):
    title: str
    amount: float
    category: str
    date: date


def load_expenses():
    with open(JSON_FILE, "r") as file:
        return json.load(file)


def save_expenses(expenses):
    with open(JSON_FILE, "w") as file:
        json.dump(expenses, file, indent=4)


@app.get("/")
def home():
    return {"message": "Welcome to Personal Expense Tracker API"}



@app.post("/post-expenses")
def add_expense(expense: Expense):

    expenses = load_expenses()

    new_id = 1

    if expenses:
        for item in expenses:
            new_id = item["id"] + 1

    new_expense = {
        "id": new_id,
        "title": expense.title,
        "amount": expense.amount,
        "category": expense.category,
        "date": expense.date.isoformat()
    }

    expenses.append(new_expense)
    save_expenses(expenses)

    return {
        "message": "Expense added successfully",
        "expense": new_expense
    }



@app.get("/Get-expenses")
def get_all_expenses():

    expenses = load_expenses()
   
    return {
        "count": len(expenses),
        "expenses": expenses
    }



@app.get("/expenses/category/{category}")
def filter_by_category(category: str):

    expenses = load_expenses()
    filtered=[]
    for item in expenses:
        if item["category"].lower() == category.lower():
            filtered.append(item)
    # filtered = [
    #     expense
    #     for expense in expenses
    #     if expense["category"].lower() == category.lower()
    # ]

    if not filtered:
        raise HTTPException(
            status_code=404,
            detail="No expenses found for this category."
        )

    return {
        "category": category,
        "count": len(filtered),
        "expenses": filtered
    }


@app.get("/expenses/total")
def total_expenses():

    expenses = load_expenses()
    total=0
    for item in expenses:
        total+=item["amount"]
    # total = sum(expense["amount"] for expense in expenses)

    return {
        "total_expenses": total
    }


@app.get("/expenses/total/{category}")
def total_by_category(category: str):

    expenses = load_expenses()
    filtered=[]
    for item in expenses:
        if item["category"].lower() == category.lower():
            filtered.append(item)
    # filtered = [
    #     expense
    #     for expense in expenses
    #     if expense["category"].lower() == category.lower()
    # ]

    if not filtered:
        raise HTTPException(
            status_code=404,
            detail="Category not found."
        )
    total =0
    for totals in filtered:
        total+=totals["amount"]
    # total = sum(expense["amount"] for expense in filtered)

    return {
        "category": category,
        "total": total
    }



@app.delete("/expenses/{expense_id}")
def delete_expense(expense_id: int):

    expenses = load_expenses()
    
    for expense in expenses:
        if expense["id"] == expense_id:
            expenses.remove(expense)
            save_expenses(expenses)

            return {
                "message": "Expense deleted successfully."
            }

    raise HTTPException(
        status_code=404,
        detail="Expense not found."
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
