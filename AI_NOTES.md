# AI Usage Notes

## 1. Which parts of the code were AI-generated vs. written by me?

I used ChatGPT as a development assistant during this assignment.

AI helped me with:

- Setting up the initial FastAPI application.
- Explaining FastAPI concepts such as Pydantic, HTTPException, and TestClient.
- Providing an initial structure for the REST API endpoints.
- Generating example pytest test cases.
- Explaining project organization and documentation.

I wrote or significantly modified:

- JSON file handling logic.
- Expense CRUD operations.
- Expense ID generation logic.
- Category filtering logic.
- Total expense calculations.
- Project structure.
- Additional positive and negative test cases.
- Final debugging and verification.

---

## 2. What did I validate, test, or change?

I reviewed every AI suggestion before including it in the project.

The main changes I made were:

- Replaced several AI-generated list comprehensions with standard for-loops to improve readability.
- Modified the expense ID generation logic.
- Corrected the category-wise total calculation.
- Added multiple positive and negative API test cases.
- Verified all API endpoints using Swagger UI.
- Executed the complete pytest suite to ensure all tests passed successfully.

---

## 3. AI suggestions I decided not to use

I chose not to use several AI suggestions because they were unnecessary for this assignment.

These included:

- Splitting the project into multiple router and service files.
- Using a database instead of a JSON file.
- Using more compact list comprehensions instead of explicit loops.
- Adding Docker support and authentication, which were outside the required scope.

I preferred a simpler implementation that matches the assignment requirements and is easy to understand and maintain.