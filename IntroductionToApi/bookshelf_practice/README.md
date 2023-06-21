# API Documentation Practice

In this exercise, your task is to practice writing documentation for the bookstore app we created earlier.

You'll soon be writing documentation for your final project (the Trivia API), after which you'll get feedback from a reviewer. You can think of this as some rudimentary practice to prepare for that.

At each step, you can compare what you've written with our own version. Of course, **there isn't a single correct way to write a piece of documentation**, so your version may look quite different. However, there are principles and practices you should follow in order to produce quality documentation, and we'll point this out so you can check whether you've incorporated them in what you wrote.

## Getting started

Now, add a Getting Started section to your documentation. Remember, this should include at least your base URL and an explanation of authentication. Feel free to provide other information that is relevant for your API

### BookShelf API Introduction

Bookshelf API is built keeping in mind REST. This API can be used to add new books, search books, delete books and also change the ratings. This API accepts form-encoded requests and returns with JSON-encoded reponses using standard HTTP response codes and authentication.

Base URL:

- base URL: http://127.0.0.1:5000/
  At the moment, this can be only run locally since this is not hosted. This is set as a proxy in the frontend configuration.

Authentication:

- This version of the app doesn't require API keys or authentication.

### Error Handling

Now, add an Error Handling section to your documentation. It should include the format of the error responses the client can expect as well as which status codes you use.

- Response codes
- Messages
- Error types

Errors are returned as follows:
{
"success": False,
"error": 404,
"message": "Resource not found"
}

Error codes are as follows:

- 400 (Bad Request)
- 404 (Not Found)
- 405 (Method Not Allowed)
- 422 (unprocessable)

### Endpoint Library

Now, add an Endpoint Library section to your documentation. Make sure that endpoints, methods and returned data are all clear. Consider including sample requests for clarity

- Organized by resource
- Include each endpoint
- Sample request
- Arguments including data types
- Response object including status codes and data types

1. Show Books (list out all the books)
   endpoint: '/books'
   method: "GET"
   sample request: curl 'http://127.0.0.1/books'
   return: {
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

2. Update Rating (Change rating of a book)
   endpoint: '/books/<int:book_id>'
   method: "PATCH"
   sample request: curl http://127.0.0.1:5000/books/15 -X PATCH -H "Content-Type: application/json" -d '{"rating":"1"}'
   return: {
   "id": 15,
   "success": true
   }

3. Delete Book (Delete a particular book)
   endpoint: '/books/<int:book_id>'
   method: DELETE
   sample request: curl -X DELETE http://127.0.0.1:5000/books/16?page=2
   return: {
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

4. Create Book (Create a new book)
   endpoint: '/books'
   method: 'POST'
   sample request: curl http://127.0.0.1:5000/books?page=3 -X POST -H "Content-Type: application/json" -d '{"title":"Neverwhere", "author":"Neil Gaiman", "rating":"5"}'
   return: {
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
