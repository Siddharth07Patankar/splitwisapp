# Expense Sharing System Readme

## System Architecture

### Components
- **Flask Application**: The core of the system built using the Flask web framework.
- **MongoDB**: Used for storing user data, group data, expenses, and balances.
- **API Endpoints**: Exposed via the Flask application to interact with the system.
- **Classes**: Implemented in Python to represent Users, UserGroups, and Expenses.

### Architecture Diagram


## API Contracts

## Create User
**Endpoint**:  `/users`
**Method**: POST
**Request Body**:
```json
{
    "name": "User Name",
    "email": "user@example.com",
    "mobile": "1234567890"
} ```
```
**Response:**
```json
{
    "message": "User created successfully"
}
```

### Create User Group
- **Endpoint:** `/groups`
- **Method:** POST
- **Request Body:**
    ```json
    {
        "group_name": "Group Name",
        "members": ["u1", "u2", ...]
    }
    ```
- **Response:**
    ```json
    {
        "message": "User group created successfully",
        "group_id": "group_id"
    }
    ```

## Create Equal Expense
- **Endpoint:** `/expenses/equal/<group_id>`
- **Method:** POST
- **Request Body:**
    ```json
    {
        "payer": "user_id",
        "amount": 100.0,
        "participants": ["u1", "u2", ...],
        "description": "Expense description"
    }
    ```
- **Response:**
    ```json
    {
        "message": "Expense created successfully"
    }
    ```
## Create UnEqual Expense
- **Endpoint:** `/expenses/unequal/<group_id>`
- **Method:** POST
- **Request Body:**
    ```json
    {
    "payer": "u1",
    "amount": 150.0,
    "shares": [
        {"user": "u1", "amount": 50.0},
        {"user": "u2", "amount": 60.0},
        {"user": "u3", "amount": 40.0}
    ],
    "description": "Unequal Expense Description"}
    ```
- **Response:**
    ```json
    {
        "message": "Expense created successfully"
    }
    ```

## Create percentage Expense
- **Endpoint:** `/expenses/percentage/<group_id>`
- **Method:** POST
- **Request Body:**
    ```json
    {
    "payer": "u3",
    "amount": 200.0,
    "percentages": [30, 40, 30],
    "participants": ["u1", "u2", "u3", "u4"],
    "description": "Percentage Expense Description"}
    ```
- **Response:**
    ```json
    {
        "message": "Expense created successfully"
    }
    ```
## Balances
**Endpoint**:  `/group/balances/<group_id>`
**Method**: POST
**Request Body**:
null

**Response:**
```json
{
  "u1": -200.0,
  "u2": 173.33333333333334,
  "u3": -6.666666666666657,
  "u4": 33.333333333333336
}
```
## group owes
**Endpoint**:  `/group/owes/<group_id>`
**Method**: POST
**Request Body**:
null

**Response:**
```json
[
  {
    "amount": 200.0,
    "from_user_id": "u1",
    "to_user_id": "u2"
  },
  {
    "amount": 200.0,
    "from_user_id": "u1",
    "to_user_id": "u4"
  },
  {
    "amount": 6.666666666666657,
    "from_user_id": "u3",
    "to_user_id": "u2"
  },
  {
    "amount": 6.666666666666657,
    "from_user_id": "u3",
    "to_user_id": "u4"
  }
]
```
## get balances
**Endpoint**:  `/balances/<group_id>`
**Method**: POST
**Request Body**:
null 

**Response:**
```json
{
  "u1": -200.0,
  "u2": 173.33333333333334,
  "u3": -6.666666666666657,
  "u4": 33.333333333333336
}
```
## Classes

### User
- Represents user information.
- Properties: `name`, `email`, `mobile`, `user_id`

### UserGroup
- Represents a group of users.
- Properties: `group_name`, `members`, `group_id`

### Expense
- Represents an expense within a group.
- Properties: `description`, `amount`, `payer`, `participants`, `expense_type`, `shares`