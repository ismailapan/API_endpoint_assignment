# FLYRANK API

A lightweight Python backend server built with FastAPI featuring JSON endpoints for product data management. Developed for the **Backend AI Engineering - Week 1** assignment.

## FEATURES
- Facility fast test with integrated in-memory database
- Data models with Pydantic models
- Using a get endpoint with FastAPI

## ## ENDPOINTS & USAGE

The API provides two main endpoints to fetch product data in JSON format:

### 1. Get All Products
- **URL:** `/`
- **Method:** `GET`
- **Description:** Returns the complete list of all products available in the database.
- **Response Format:** JSON Array

### 2. Get Product by ID
- **URL:** `/product/{product_id}`
- **Method:** `GET`
- **Description:** Fetches the details of a specific product using its unique ID path parameter. Returns a `404 Not Found` error if the product does not exist.
- **Response Format:** JSON Object
