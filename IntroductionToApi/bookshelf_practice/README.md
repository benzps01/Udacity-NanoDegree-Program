# Benson's Bookshelf

This is a bookshelf application created for those users who want to create a database of all their favourite books with the ability to rate them as they see fit.

## Pre-requisites and Local Development

Here we have used postgres as a database, so postgres must be installed beforehand with database bookshelf.

To start postgres server run `pg_ctl -D file_path(eg.C:\postgres\data) start`

There are also 2 files to create table and populate the table

- setup.sql
- books.psql

on a bash terminal you can run the following files using the commands:

```
psql -U postgres -d bookshelf -h localhost -p 5432 -f setup.sql
psql -U postgres -d bookshelf -h localhost -p 5432 -f books.psql
```

## Note: you need to be in the same folder as the files above to run the scripts

### Backend

The backend server is built on flask framework.<br>
You Need to install all the packages from the requirements.txt file

```
pip install -r requirements.txt
```

Next, to start flask app run:

### Note node.js needs to be installed first

```
With debug mode:
npm run start-flask-server-debug

without debug mode:
npm run start-flask-server
```

The application is run on `http://127.0.0.1:5000/` by default and is a proxy in the frontend configuration

### Frontend

The frontend is built using React.js framework.<br>
All the packages required are already mentioned in the packages.json file<br>
First install all the required packages for react:

### Note node.js needs to be installed first

`npm install`

Start the react application using:
`npm start`

By default the frontend will run on `localhost:3000`

### Tests

Navigate to the backend folder to run the tests using the commands:

```
dropdb bookshelf_test
createdb bookshelf_test
psql bookshelf_test < books.psql
python test_flaskr.py
```

The first time you run the tests, omit the dropdb command

## API Reference

### Getting Started

Bookshelf API is built keeping in mind REST. This API can be used to add new books, search books, delete books and also change the ratings. This API accepts form-encoded requests and returns with JSON-encoded reponses using standard HTTP response codes and authentication.

Base URL:

- base URL: `http://127.0.0.1:5000/`
  At the moment, this can be only run locally since this is not hosted. This is set as a proxy in the frontend configuration.

Authentication:

- This version of the app doesn't require API keys or authentication.

### Error Handling

Errors are returned as follows:

```
{
"success": False,
"error": 404,
"message": "Resource not found"
}
```

Error codes returned are as follows:

```
- 400 (Bad Request)
- 404 (Not Found)
- 405 (Method Not Allowed)
- 422 (unprocessable)
```

### Endpoints

1. Show Books (list out all the books)
   endpoint: `'/books'`
   method: `"GET"`
   sample request: `curl 'http://127.0.0.1/books'`
   return:

   ```
   {
   "books": [
   {
   "author": "Stephen King",
   "id": 1,
   "rating": 5,
   "title": "The Outsider: A Novel"
   },
   {
   "author": "Madeline Miller",
   "id": 8,
   "rating": 5,
   "title": "CIRCE"
   }
   ],
   "success": true,
   "total_books": 2
   }
   ```

2. Update Rating (Change rating of a book)
   endpoint: `'/books/<int:book_id>'`
   method: `"PATCH"`
   sample request: `curl http://127.0.0.1:5000/books/15 -X PATCH -H "Content-Type: application/json" -d '{"rating":"1"}'`
   return:

   ```
   {
   "id": 15,
   "success": true
   }
   ```

3. Delete Book (Delete a particular book)
   endpoint: `'/books/<int:book_id>'`
   method: `"DELETE"`
   sample request: `curl -X DELETE http://127.0.0.1:5000/books/16?page=2`
   return:

   ```
   {
   "books": [
   {
   "author": "Gina Apostol",
   "id": 9,
   "rating": 5,
   "title": "Insurrecto: A Novel"
   },
   {
   "author": "Tayari Jones",
   "id": 10,
   "rating": 5,
   "title": "An American Marriage"
   },
   ],
   "deleted": 16,
   "success": true,
   "total_books": 2
   }
   ```

4. Create Book (Create a new book)
   endpoint: ` '/books'``
method:  `"POST"`sample request:`curl http://127.0.0.1:5000/books?page=3 -X POST -H "Content-Type: application/json" -d '{"title":"Neverwhere", "author":"Neil Gaiman", "rating":"5"}'```
   return:
   ```
   {
   "books": [
   {
   "author": "Neil Gaiman",
   "id": 24,
   "rating": 5,
   "title": "Neverwhere"
   }
   ],
   "created": 24,
   "success": true,
   "total_books": 3
   }
   ```

## Authors

Benson Sabu Pallivathukkal
