library-api
===========

Requirements
------------

If using `asdf` version manager, install the following by issuing `asdf install`
at the project root:

- Python 3
- PostgreSQL (use `pg_ctl start` to start)

Dependencies
------------

### API

- Flask
- Flask-API
- Flask-Migrate
- Flask-RESTful
- Flask-SQLAlchemy
- Flask-Script
- SQLAlchemy
- psycopg2

Setup
-----

Issue `bin/setup` from the project root to install dependencies. The setup
script assumes the minimal requirements above are installed and running and
will:

1. Create and activate a virtualenv at the project root
2. Install Python dependencies
3. Create a `.env` file to set development-mode config variables
4. Create and migrate the database
5. Start the development server at http://127.0.0.1:5000

To tear down setup, use `bin/setup --down`.

Endpoints
---------
```
GET    /                     api index (browseable API docs)
GET    /api/v1/request/      list requests
POST   /api/v1/request/      create a request
GET    /api/v1/request/:id   get a request by id
DELETE /api/v1/request/:id   delete a request by id
```
