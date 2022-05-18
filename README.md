# Cashman Flask Project
A simple Flask CRUD backend example I'm creating studying Flask.
The porpuse here is to implement what I'm learning.
## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the project.
```bash
pip install -r requirements.txt
```
Export FLASK_APP environment variable.
```bash
export FLASK_APP=cashman
```
Initialize database.
```bash
flask init-db
```
Run the application.
```bash
flask run
```
## Endpoints
### Create a new income
#### Request
`POST /income/`

    curl -i -X POST http://localhost:5000/income -H 'Content-Type: application/json' -d '{"value": 123.45}'
#### Response
    HTTP/1.1 201 CREATED
    Server: Werkzeug/2.1.1 Python/3.8.10
    Date: Wed, 18 May 2022 14:46:29 GMT
    Content-Type: application/json
    Location: /income/1
    Content-Length: 0
### Get a list with all incomes
#### Request
`GET /incomes/`

    curl -i http://localhost:5000/incomes
#### Response
    HTTP/1.1 200 OK
    Server: Werkzeug/2.1.1 Python/3.8.10
    Date: Wed, 18 May 2022 14:48:44 GMT
    Content-Type: application/json
    Content-Length: 26

    [{"id":1,"value":123.45}]
### Get one income by ID
#### Request
`GET /income/{id}`

    curl -i http://localhost:5000/income/1
#### Response
    HTTP/1.1 200 OK
    Server: Werkzeug/2.1.1 Python/3.8.10
    Date: Wed, 18 May 2022 14:49:29 GMT
    Content-Type: application/json
    Content-Length: 24

    {"id":1,"value":123.45}
### Update one income by ID
#### Request
`PATCH /income/{id}`

    curl -i -X PATCH http://localhost:5000/income/1 -H 'Content-Type: application/json' -d '{"value": 10.23}'
#### Response
    HTTP/1.1 204 NO CONTENT
    Server: Werkzeug/2.1.1 Python/3.8.10
    Date: Wed, 18 May 2022 14:50:02 GMT
    Content-Type: application/json
    Transfer-Encoding: chunked
### Delete one income by ID
#### Request
`DELETE /income/{id}`

    curl -i -X DELETE http://localhost:5000/income/1
#### Response
    HTTP/1.1 204 NO CONTENT
    Server: Werkzeug/2.1.1 Python/3.8.10
    Date: Wed, 18 May 2022 14:50:29 GMT
    Content-Type: application/json
    Transfer-Encoding: chunked
### Get a list with all transactions
#### Request
`GET /transactions/`

    curl -i http://localhost:5000/transactions
#### Response
    HTTP/1.1 200 OK
    Server: Werkzeug/2.1.1 Python/3.8.10
    Date: Wed, 18 May 2022 14:47:53 GMT
    Content-Type: application/json
    Content-Length: 42

    [{"id":1,"type":"INCOME","value":123.45}]
### Create a new expense
#### Request
`POST /expense/`

    curl -i -X POST http://localhost:5000/expense -H 'Content-Type: application/json' -d '{"value": 123.45}'
#### Response
    HTTP/1.1 201 CREATED
    Server: Werkzeug/2.1.1 Python/3.8.10
    Date: Wed, 18 May 2022 14:51:34 GMT
    Content-Type: application/json
    Location: /expense/1
    Content-Length: 0
### Get a list with all expenses
#### Request
`GET /expenses/`

    curl -i http://localhost:5000/expenses
#### Response
    HTTP/1.1 200 OK
    Server: Werkzeug/2.1.1 Python/3.8.10
    Date: Wed, 18 May 2022 14:52:19 GMT
    Content-Type: application/json
    Content-Length: 26

    [{"id":1,"value":123.45}]
### Get one expense by ID
#### Request
`GET /expense/{id}`

    curl -i http://localhost:5000/expense/1
#### Response
    HTTP/1.1 200 OK
    Server: Werkzeug/2.1.1 Python/3.8.10
    Date: Wed, 18 May 2022 14:53:00 GMT
    Content-Type: application/json
    Content-Length: 24

    {"id":1,"value":123.45}
### Update one expense by ID
#### Request
`PATCH /expense/{id}`

    curl -i -X PATCH http://localhost:5000/expense/1 -H 'Content-Type: application/json' -d '{"value": 10.23}'
#### Response
    HTTP/1.1 204 NO CONTENT
    Server: Werkzeug/2.1.1 Python/3.8.10
    Date: Wed, 18 May 2022 14:54:05 GMT
    Content-Type: application/json
    Transfer-Encoding: chunked
### Delete one expense by ID
#### Request
`DELETE /expense/{id}`

    curl -i -X DELETE http://localhost:5000/expense/1
#### Response
    HTTP/1.1 204 NO CONTENT
    Server: Werkzeug/2.1.1 Python/3.8.10
    Date: Wed, 18 May 2022 14:54:50 GMT
    Content-Type: application/json
    Transfer-Encoding: chunked
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
## License
[MIT](https://choosealicense.com/licenses/mit/)
