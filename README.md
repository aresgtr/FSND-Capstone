# FSND-Capstone

Capstone project for Udacity Full Stack Nanodegree program

## The "Capstone Game Store"

"Capstone Game Store" is for game lovers, which sells games on different platforms including PlayStation, Xbox, Nintendo Switch, and PC. The project sets a database for internal operational use for the store. It allows staff members to insert, update, and delete game information, customer information, and transaction records.

This capstone project demonstrates the skills of:
- Coding in Python 3
- Relational Database Architecture
- One-to-many relationship between classes
- Modeling Data Objects with SQLAlchemy
- Internet Protocols and Communication
- Developing a Flask API
- Authentication and Access Control with Auth0 and Flask
- Role-Based Access Control (RBAC)
- Testing Flask Application with Python UnitTests
- Deploying Application with Heroku

## API Reference

### Base URL for this project

`http://qicapstone.herokuapp.com/`

Please note there is no frontend configured for this project. Please use `curl` or Postman to interact with the endpoints.

## Authentication

This project uses Auth0 for third-party authentication services. Please refer to this link to register accounts for authentication jwt tokens.

`https://zhangqi.auth0.com/authorize?audience=capstone&response_type=token&client_id=0ULSCgsC3dU8F9PsoRi7na3z4SW1AiLD&redirect_uri=http://127.0.0.1:8080/login-results`

Two roles are configured for this project: __manager__ and __sales__

## Error Handling

Errors are returned as JSON objects in the following format:

```python
{
    'success': False,
    'error': 400,
    'message': 'bad request'
}
```

The API will return the following error types when requests fail:
- 400: bad request
- 401 or 403: action not permitted or authentication fails
- 404: not found
- 422: unprocessable
- 500: internal server error

## Endpoints

### GET /games
- General:
    - Return a list of games in the database
- Authenticaiton:
    - No authentication required. Open to public.

Results:
```json
{
    "games": [
        {
            "developers": [
                "Rockstar North",
                "Rockstar Games"
            ],
            "genre": [
                "Action",
                "Adventure"
            ],
            "id": 1,
            "name": "Grand Theft Auto V",
            "platforms": [
                "Xbox 360",
                "PlayStation 3",
                "Playstation 4",
                "Xbox One",
                "PC",
                "PlayStation 5"
            ],
            "publishers": [
                "Rockstar Games"
            ],
            "release_date": "Tue, 17 Sep 2013 00:00:00 GMT",
            "review_score": 10.0
        },
        {
            "developers": null,
            "genre": [
                "Simulation"
            ],
            "id": 2,
            "name": "Animal Crossing: New Horizons",
            "platforms": [
                "Nintendo Switch"
            ],
            "publishers": [
                "Nintendo"
            ],
            "release_date": "Fri, 20 Mar 2020 00:00:00 GMT",
            "review_score": 9.0
        },
        {
            "developers": [
                "Turn 10 Studios",
                "Playground Games"
            ],
            "genre": [
                "Racing"
            ],
            "id": 3,
            "name": "Forza Horizon 4",
            "platforms": [
                "Xbox One",
                "PC"
            ],
            "publishers": [
                "Microsoft"
            ],
            "release_date": "Tue, 02 Oct 2018 00:00:00 GMT",
            "review_score": 9.6
        }
    ],
    "num_of_games": 3,
    "success": true
}
```

### POST /games
- General:
    - Insert a game into the database, return a list of games in the database after insertion
- Authenticaiton:
    - Bearer token required
    - Only __manager__ role is allowed for this endpoint

Request body example:
```json
{
    "name": "Forza Horizon 4",
    "developers": [
        "Turn 10 Studios",
        "Playground Games"
    ],
    "publishers": [
        "Microsoft"
    ],
    "release_date": "2018-10-02",
    "platforms": [
        "Xbox One",
        "PC"
    ],
    "review_score": 9.6,
    "genre": [
        "Racing"
    ]
}
```
Note that "name" field is required in the request body

### PATCH /games/{game_id}
- General:
    - Update certain fields of the game with the given ID, return a list of games in the database after the update
- Authentication:
    - Bearer token required
    - Only __manager__ role is allowed for this endpoint

Request body example:
```json
{
    "name": "Forza Horizon 4",
    "developers": [
        "Turn 10 Studios",
        "Playground Games"
    ],
    "publishers": [
        "Microsoft"
    ],
    "release_date": "2018-10-02",
    "platforms": [
        "Xbox One",
        "PC"
    ],
    "review_score": 9.6,
    "genre": [
        "Racing"
    ]
}
```

### DELETE /games/{game_id}
- General:
    - Delete the game of the given ID if it exists, return the list of games in the database after deletion
- Authentication:
    - Bearer token required
    - Only __manager__ role is allowed for this endpoint

### GET /customers
- General:
    - Return a list of customers in the database
- Authenticaiton:
    - Bearer token required
    - __sales__ and __manager__ roles are allowed for this endpoint

Results:
```json
{
    "customers": [
        {
            "country": "Canada",
            "email": "email@example.com",
            "first_name": "Tom",
            "id": 1,
            "last_name": "Jerry",
            "phone": "6543217890",
            "state": "British Columbia"
        },
        {
            "country": "China",
            "email": "ming@example.com",
            "first_name": "Ming",
            "id": 2,
            "last_name": "Li",
            "phone": "13000000000",
            "state": "Heilongjiang"
        }
    ],
    "num_of_customers": 2,
    "success": true
}
```

### POST /customers
- General:
    - Insert a customer into the database, return a list of customers in the database after insertion
- Authenticaiton:
    - Bearer token required
    - __sales__ and __manager__ roles are allowed for this endpoint

Request body example:
```json
{
    "customers": [
        {
            "country": "Canada",
            "email": "email@example.com",
            "first_name": "Tom",
            "id": 1,
            "last_name": "Jerry",
            "phone": "6543217890",
            "state": "British Columbia"
        }
    ],
    "num_of_customers": 1,
    "success": true
}
```
Note that "first_name" and "last_name" fields are required in the request body

### PATCH /customers/{customer_id}
- General:
    - Update certain fields of the customer with the given ID, return a list of customers in the database after the update
- Authentication:
    - Bearer token required
    - __sales__ and __manager__ roles are allowed for this endpoint

Request body example:
```json
{
    "customers": [
        {
            "country": "Canada",
            "email": "email@example.com",
            "first_name": "Tom",
            "id": 1,
            "last_name": "Jerry",
            "phone": "6543217890",
            "state": "British Columbia"
        }
    ],
    "num_of_customers": 1,
    "success": true
}
```

### DELETE /customers/{customer_id}
- General:
    - Delete the customer of the given ID if it exists, return the list of customers in the database after deletion
- Authentication:
    - Bearer token required
    - Only __manager__ role is allowed for this endpoint

### GET /transactions
- General:
    - Return a list of transactions in the database
- Authenticaiton:
    - Bearer token required
    - Only __manager__ role is allowed for this endpoint

Results:
```json
{
    "num_of_transactions": 1,
    "success": true,
    "transactions": [
        {
            "amount": 19.99,
            "customer_id": 1,
            "game_id": 2,
            "id": 1,
            "review": null,
            "time_of_transaction": "Thu, 18 Jun 2020 00:00:00 GMT"
        }
    ]
}
```

### POST /transactions
- General:
    - Insert a transaction into the database, return a list of transactions in the database after insertion
- Authenticaiton:
    - Bearer token required
    - __sales__ and __manager__ roles are allowed for this endpoint

Request body example:
```json
{
            "amount": 19.99,
            "customer_id": 1,
            "game_id": 2,
            "review": "This is a nice game!",
            "time_of_transaction": "2020-06-18"
            }
```
Note that "time_of_transaction", "amount", "game_id" and "customer_id" fields are required in the request body