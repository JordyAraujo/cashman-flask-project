# Cashman Flask Project
___
A simple Flask CRUD backend example I'm creating studying Flask.
The porpuse here is to implement what I'm learning.
## Installation
___
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
### Get a list with all transactions
___

#### Request

`GET /transactions/`

    curl -i http://localhost:5000/transactions

#### Response

    HTTP/1.1 200 OK
    Server: Werkzeug/2.1.2 Python/3.8.10
    Date: Fri, 13 May 2022 13:03:53 GMT
    Content-Type: application/json
    Content-Length: 104
    Connection: close

    [{"id":1,"transaction_type":"INCOME","value":10.23},{"id":2,"transaction_type":"INCOME","value":12.34}]

### Get a list with all incomes
___
#### Request

`GET /incomes/`

    curl http://localhost:5000/incomes

#### Response

    HTTP/1.1 200 OK
    Server: Werkzeug/2.1.2 Python/3.8.10
    Date: Fri, 13 May 2022 13:04:25 GMT
    Content-Type: application/json
    Content-Length: 104
    Connection: close

    [{"id":1,"transaction_type":"INCOME","value":10.23},{"id":2,"transaction_type":"INCOME","value":12.34}]

### Create a new income
___
#### Request

`POST /income/`

    curl -i -X POST http://localhost:5000/income -H 'Content-Type: application/json' -d '{"value": 123.45}'

#### Response

    HTTP/1.1 201 CREATED
    Server: Werkzeug/2.1.2 Python/3.8.10
    Date: Fri, 13 May 2022 13:05:12 GMT
    Content-Type: application/json
    Location: /income/30
    Content-Length: 0
    Connection: close

### Get one income by ID
___
#### Request

`GET /income/{id}`

    curl http://localhost:5000/income/{id}

#### Response

    HTTP/1.1 200 OK
    Server: Werkzeug/2.1.2 Python/3.8.10
    Date: Fri, 13 May 2022 13:06:06 GMT
    Content-Type: application/json
    Content-Length: 51
    Connection: close

    {"id":1,"transaction_type":"INCOME","value":1.23}

### Update one income by ID
___
#### Request

`PATCH /income/{id}`

    curl -i -X PATCH http://localhost:5000/income/1 -H 'Content-Type: application/json' -d '{"value": 10.23}'

#### Response

    HTTP/1.1 204 NO CONTENT
    Server: Werkzeug/2.1.2 Python/3.8.10
    Date: Fri, 13 May 2022 13:07:24 GMT
    Content-Type: application/json
    Connection: close

### Delete one income by ID
___
#### Request

`DELETE /income/{id}`

    curl -i -X DELETE http://localhost:5000/income/{id}

#### Response

    HTTP/1.1 204 NO CONTENT
    Server: Werkzeug/2.1.2 Python/3.8.10
    Date: Fri, 13 May 2022 13:11:07 GMT
    Content-Type: application/json
    Connection: close

## Contributing
___
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
## License
___
[MIT](https://choosealicense.com/licenses/mit/)