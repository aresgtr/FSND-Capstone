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

## Getting Started

### Installing Dependencies

Note that the project is now hosting on Heroku. Dependency installation is not required unless you want to test the project locally.

#### Python 3.8

#### PIP Dependencies
```
pip install -r requirements.txt
```
Depending on your python version, you might want to use pip3 instead of pip.

### PostgreSQL

To test locally, PostgreSQL should be installed and running. `capstone` database need to be created before running the project.

#### Running the server locally

In models.py, uncomment the first line below and comment out the second line, to define local database path.

```python
# database_path = 'postgresql://postgres:password@localhost:5432/capstone'
database_path = os.environ['DATABASE_URL']
```

To run the server, execute:

```
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

#### Running the tests locally

```
dropdb capstone_test
createdb capstone_test
psql capstone_test < capstone_test.psql
python test_app.py
```
Depending on your python version, you might want to use python3 instead of python.

## API Reference

### Base URL for this project

`http://qicapstone.herokuapp.com/`

Please note there is no frontend configured for this project. Please use `curl` or Postman to interact with the endpoints.

If you want to test APIs locally, use `http://localhost:5000/`

## Third-Party Authentication

This project uses Auth0 for third-party authentication services. Please refer to this link to register accounts for authentication jwt tokens.

`https://zhangqi.auth0.com/authorize?audience=capstone&response_type=token&client_id=0ULSCgsC3dU8F9PsoRi7na3z4SW1AiLD&redirect_uri=http://127.0.0.1:8080/login-results`

Two roles are configured for this project: __manager__ and __sales__

Please use the authentication tokens below for testing. Note that there is expiration time for both tokens, please contact https://aresgtr.github.io/ for most updated tokens.

### Manager Bearer Token:
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlBKOU1iQU1WRzZvRnlMUVVSdFB0cyJ9.eyJpc3MiOiJodHRwczovL3poYW5ncWkuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlZTFjMmQ0ZWUyYmU0MDAxM2ZjZGU3NiIsImF1ZCI6ImNhcHN0b25lIiwiaWF0IjoxNTkyNTk2MTg5LCJleHAiOjE1OTI2ODI1ODksImF6cCI6IjBVTFNDZ3NDM2RVOEY5UHNvUmk3bmEzejRTVzFBaUxEIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6Y3VzdG9tZXJzIiwiZGVsZXRlOmdhbWVzIiwiZ2V0OmN1c3RvbWVycyIsImdldDpnYW1lcyIsImdldDp0cmFuc2FjdGlvbnMiLCJwYXRjaDpjdXN0b21lcnMiLCJwYXRjaDpnYW1lcyIsInBvc3Q6Y3VzdG9tZXJzIiwicG9zdDpnYW1lcyIsInBvc3Q6dHJhbnNhY3Rpb25zIl19.JP93WeYyV-PvDSRkOPGmB0AkjE2LHcgAqb96dq-xcGJvIVgwb3VNWKcSGrapVyRtXTB11DhZF1zMcxiVLbUXKqh57HdyTd97JXi_RhXM2itH3ViI5jn6qrghhfaAl1pNo1MSSR8lAlIiocFatSIH5-Zh0-8Ouwk2CdstIShY45RTxLr-1FRW22yWjVxrFvbWAKGaOjMqFGfVsxlabzybRdNBk_oNySfQIKXOYiiJvNpE-wcDaQfpAUDfY3YP0IsjsBEe4YcEZIT0_zcoNicSi9M8eUrwJPwy01Kz39CQdH2kBJAvstlJIgA2doxkAZUWgDvPjvVT_0Ks7CbFZb7lsQ

### Sales Bearer Token:
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlBKOU1iQU1WRzZvRnlMUVVSdFB0cyJ9.eyJpc3MiOiJodHRwczovL3poYW5ncWkuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlZTJiMjkwNzZmNjY5MDAxMzYzOGE0YSIsImF1ZCI6ImNhcHN0b25lIiwiaWF0IjoxNTkyNTk2MjU3LCJleHAiOjE1OTI2ODI2NTcsImF6cCI6IjBVTFNDZ3NDM2RVOEY5UHNvUmk3bmEzejRTVzFBaUxEIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6Y3VzdG9tZXJzIiwiZ2V0OmdhbWVzIiwicGF0Y2g6Y3VzdG9tZXJzIiwicG9zdDpjdXN0b21lcnMiLCJwb3N0OnRyYW5zYWN0aW9ucyJdfQ.jUuw-ADVHrHBmBk2cQxKvDJ_qiGIthLWP_HesAGCdoVcAQx93SBeS4s6nNheNBDtcDmTyBZ3k-Ep7OW78JrnlWSdE9B5Pnmy3lCfmWIWs0bZWKZqcP2CCodIKFRSoLvxTKx68pULyxSjSJNwmiWAXiO51YF75rkji8gedSRf6U0KakouaOtYqa2mk_Kvd1l7SFZa8un-kFVlUDnpToVbQBV1-psqCBXEqP_BUdGmts0bT8Qmu3CMvidtkbf_mtTPEupD947KUTxzbAbHYebr6VA43_ZkSckDcLIHs7uOVZNoeuvx5PTv6ueX5tRygqwkvRSRJ2gEE0cwLnmM21QXZg

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