# GroceryItems API - DynamoDB CRUD with Lambda and API Gateway

This project implements a simple RESTful API for managing grocery items using AWS DynamoDB, Lambda functions, and API Gateway REST API.

---

## DynamoDB Setup

1. **Create DynamoDB Table**

- Table Name: `GroceryItems`
- Primary Key: `ItemID` (String)

---

## Lambda Functions for CRUD

Create four Lambda functions for CRUD operations:

- `createItemLambda` - Create new item (POST)
- `getItemsLambda` - Get all items (GET)
- `updateItemLambda` - Update item by ID (PUT)
- `deleteItemLambda` - Delete item by ID (DELETE)

Each Lambda function should have an execution role with permission to access the DynamoDB `GroceryItems` table.

---

## API Gateway Setup (REST API)

### 1. Create New REST API

- Go to Amazon API Gateway Console
- Click **Create API**
- Select **REST API** (not HTTP API)
- Choose **New API**
- Enter API name, e.g., `GroceryShopAPI`
- Click **Create API**

### 2. Create Resources

- In your API, click **Actions** > **Create Resource**
- Resource Name: `items`
- Resource Path: `/items`
- Click **Create Resource**

- Create a sub-resource for item ID:
  - Select `/items`
  - Click **Actions** > **Create Resource**
  - Uncheck **Configure as proxy resource**
  - Resource Name: `{id}`
  - Resource Path: `/items/{id}`
  - Click **Create Resource**

### 3. Create Methods and Integrate with Lambda

For `/items`:

- Create **POST** method
  - Integration type: Lambda Function
  - Check **Use Lambda Proxy integration**
  - Choose your `createItemLambda` function
  - Save and grant API Gateway permission

- Create **GET** method
  - Integration type: Lambda Function
  - Use Lambda Proxy integration
  - Choose `getItemsLambda`

For `/items/{id}`:

- Create **PUT** method
  - Integration type: Lambda Function
  - Use Lambda Proxy integration
  - Choose `updateItemLambda`

- Create **DELETE** method
  - Integration type: Lambda Function
  - Use Lambda Proxy integration
  - Choose `deleteItemLambda`

---

### 4. Enable CORS (Optional but Recommended)

For each method (`GET`, `POST`, `PUT`, `DELETE`), enable CORS:

- Select the method (e.g., POST)
- Click **Actions** > **Enable CORS**
- Confirm the headers and methods
- Deploy API again

---

### 5. Deploy the API

- Click **Actions** > **Deploy API**
- Create a new stage (e.g., `uat`)
- Note the Invoke URL, e.g.:

https://{api-id}.execute-api.{region}.amazonaws.com/uat

---

## Sample API Endpoints

| HTTP Method | URL                                     | Description           |
|-------------|-----------------------------------------|-----------------------|
| GET         | `/uat/items`                            | Get all grocery items |
| POST        | `/uat/items`                            | Create a new item     |
| PUT         | `/uat/items/{id}`                       | Update item by id     |
| DELETE      | `/uat/items/{id}`                       | Delete item by id     |

---

## Sample JSON Payloads

### POST `/uat/items`

```json
{
  "itemid": "0001",
  "name": "Eggs",
  "price": 3.99,
  "category": "Dairy"
}
```

### PUT /uat/items/0001
```
{
  "name": "Eggs",
  "price": 4.99,
  "category": "Dairy"
}
```
Note: In PUT, the item id is passed in the URL path (not in the body).

Notes
All Lambda functions expect Lambda Proxy integration.

itemid is the primary key for DynamoDB and must be unique.

In PUT and DELETE, item ID is passed as a path parameter {id}.

POST body includes itemid since it creates a new item.

Enable proper IAM permissions for Lambda to access DynamoDB.

Enable CORS if you call APIs from browsers.


### Create Grocery Shop Web UI with index.html and scripts.js and then upload to s3 bucket
