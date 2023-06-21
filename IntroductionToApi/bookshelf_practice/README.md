# API Documentation Practice

## Getting started

## BookShelf API Introduction

Bookshelf API is built keeping in mind REST. This API can be used to add new books, search books, delete books and also change the ratings. This API accepts form-encoded requests and returns with JSON-encoded reponses using standard HTTP response codes and authentication.

Base URL:

- base URL: ```http://127.0.0.1:5000/```<br>
  At the moment, this can be only run locally since this is not hosted. This is set as a proxy in the frontend configuration.

Authentication:

- This version of the app doesn't require API keys or authentication.

## Error Handling

- Response codes
- Messages
- Error types

Errors are returned as follows:
```
{
"success": False,
"error": 404,
"message": "Resource not found"
}
```

Error codes are as follows:

- 400 (Bad Request)
- 404 (Not Found)
- 405 (Method Not Allowed)
- 422 (unprocessable)

## Endpoint Library

1. Show Books (list out all the books)<br>
   endpoint: '/books'<br>
   method: "GET"<br>
   sample request: ```curl 'http://127.0.0.1/books'```<br>
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

3. Update Rating (Change rating of a book)<br>
   endpoint: '/books/<int:book_id>'<br>
   method: "PATCH"<br>
   sample request: ```curl http://127.0.0.1:5000/books/15 -X PATCH -H "Content-Type: application/json" -d '{"rating":"1"}'```<br>
   return:
```
   {
   "id": 15,
   "success": true
   }
```

5. Delete Book (Delete a particular book)<br>
   endpoint: '/books/<int:book_id>'<br>
   method: DELETE<br>
   sample request: ```curl -X DELETE http://127.0.0.1:5000/books/16?page=2```<br>
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

7. Create Book (Create a new book)<br>
   endpoint: '/books'<br>
   method: 'POST'<br>
   sample request: ```curl http://127.0.0.1:5000/books?page=3 -X POST -H "Content-Type: application/json" -d '{"title":"Neverwhere", "author":"Neil Gaiman", "rating":"5"}'```<br>
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
