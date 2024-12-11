# groceryapi-crud-python

### **DynamoDB Setup**

- Create a table named `GroceryItems` with:
    - **Primary Key**: `ItemID` (String)
###
### Create Lambda funcion for CRUD


### Create a REST API in API Gateway

1. **Open API Gateway Console**:
    - Go to the [Amazon API Gateway Console](https://console.aws.amazon.com/apigateway/).
2. **Create a New API**:
    - Click on **Create API**.
    - Choose **REST API**.
    - Select **New API** (not HTTP API).
    - Give your API a name (e.g., `GroceryShopAPI`).
3. **Create Resources**:
    - Click on **Actions** and then **Create Resource** to create a new resource (e.g., `/items`).
    - You can create sub-resources like `/items/{id}` for update and delete operations.
4. **Create Methods for Each CRUD Operation**:
    - Select the resource (e.g., `/items`) and click **Create Method**.
        - For **POST**: This will handle item creation > under `/items`
        - For **GET**: This will fetch all items > under `/items`
        - For **PUT**: This will update an existing item > under `/items/{id}`
        - For **DELETE**: This will delete an item > under `/items`
5. **Set Up Integration with Lambda**:
    - For each method (POST, GET, PUT, DELETE), set the integration type to **Lambda Function**.
    - Select the corresponding Lambda function for each method (e.g., `createItemLambda` for POST, `getItemsLambda` for GET, etc.).
    - Ensure that the Lambda execution role has the necessary permissions to invoke your Lambda function.
6. **Deploy the API**:
    - Click **Actions** and then **Deploy API**.
    - Choose an existing deployment stage (e.g., `prod`) or create a new one.
    - Click **Deploy**.
7. **Get the Invoke URL**:
8. **Enable CORS for all methods.**
###
### Create Grocery Shop Web UI with index.html and scripts.js and then upload to s3 bucket