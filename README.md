# RESTful API Documentation

## Overview

This RESTful API is designed to manage a collection of items using Amazon Web Services (AWS). It provides basic operations for retrieving and adding items to a DynamoDB database. Each API endpoint uses a lambda function, as attached in this repository. The API is secured with an API key and includes rate limiting for usage control. Custom access logging is implemented using CloudWatch.

**Base URL**: `https://dyyhxsryhd.execute-api.us-east-2.amazonaws.com/prod`

## Authentication

All API endpoints require authentication using an API key. To include the API key in your request, set the `x-api-key` header with the value of your API key.

## Rate Limiting

The API has the following rate limits:
- Requests per second: 5000
- Burst limit: 1000
- Monthly quota: 1 million requests

## Endpoints

### 1. Retrieve All Items

- **Endpoint**: `/items`
- **Method**: GET
- **Description**: Retrieve a list of all items stored in the database.
- **Response (200 OK)**:
  ```json
  {
      "statusCode": 200,
      "body": "[{\"description\": \"This is a test item.\", \"id\": 3, \"name\": \"test\"}, {\"description\": \"This is a test item.\", \"id\": 2, \"name\": \"test\"}, {\"description\": \"This is a test item.\", \"id\": 4, \"name\": \"test\"}, {\"description\": \"This is a test item.\", \"id\": 1, \"name\": \"test\"}, {\"id\": 0, \"description\": \"item_description\", \"name\": \"item_name\"}, {\"description\": \"This is a test item from postman.\", \"id\": 5, \"name\": \"postman test\"}]"
  }
  ```

### 2. Retrieve Item by ID

- **Endpoint**: `/items/{id}`
- **Method**: GET
- **Description**: Retrieve details of a specific item by providing its ID. If the item is not found, an error message will be returned.
- **Request**: Replace `{id}` with the item ID as a number.
- **Response (200 OK)**:
  ```json
  {
      "statusCode": 200,
      "body": "{\"description\": \"This is a test item.\", \"id\": 4, \"name\": \"test\"}"
  }
  ```
- **Response (404 Not Found)** (Item not found):
  ```json
  {
      "statusCode": 404,
      "body": "{\"message\": \"Item not found.\"}"
  }
  ```

### 3. Add a New Item

- **Endpoint**: `/items`
- **Method**: POST
- **Description**: Add a new item to the database by sending a POST request with the item details in the request body.
- **Request Body**:
  ```json
  {
    "name": "example",
    "description": "this is an example post request."
  }
  ```
- **Response (200 OK)**:
  ```json
  {
      "statusCode": 200,
      "body": "{\"message\": \"Item added successfully\", \"item_id\": 7}"
  }
  ```

## Example cURL Requests

### Retrieve All Items
```bash
curl -X GET https://dyyhxsryhd.execute-api.us-east-2.amazonaws.com/prod/items -H "x-api-key: YOUR_API_KEY"
```

### Retrieve Item by ID
Replace `{id}` with the actual item ID.
```bash
curl -X GET https://dyyhxsryhd.execute-api.us-east-2.amazonaws.com/prod/items/{id} -H "x-api-key: YOUR_API_KEY"
```

### Add a New Item
```bash
curl -X POST https://dyyhxsryhd.execute-api.us-east-2.amazonaws.com/prod/items -H "x-api-key: 43AvV6Mvia74DxpB5yAYw1n0VIvIUxsq8Kt4bhdH" -d "{\"name\": \"example\", \"description\": \"this is an example post request.\"}"
```
