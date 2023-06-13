import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy  # , or_
from flask_cors import CORS
import random

from models import setup_db, Book, db

BOOKS_PER_SHELF = 8

# @TODO: General Instructions
#   - As you're creating endpoints, define them and then search for 'TODO' within the frontend to update the endpoints there.
#     If you do not update the endpoints, the lab will not work - of no fault of your API code!
#   - Make sure for each route that you're thinking through when to abort and with which kind of error
#   - If you change any of the response body keys, make sure you update the frontend to correspond.

def paginate_books(request):
    page = request.args.get('page', 1, type=int)
    books = Book.query.order_by(Book.id).paginate(page=page, per_page=BOOKS_PER_SHELF)
    books_array = [book.format() for book in books.items]
    return books_array

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    # CORS Headers
    @app.after_request
    def after_request(response):
        response.headers.add(
            "Access-Control-Allow-Headers", "Content-Type,Authorization,true"
        )
        response.headers.add(
            "Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS"
        )
        return response

    # @TODO: Write a route that retrivies all books, paginated.
    #         You can use the constant above to paginate by eight books.
    #         If you decide to change the number of books per page,
    #         update the frontend to handle additional books in the styling and pagination
    #         Response body keys: 'success', 'books' and 'total_books'
    # TEST: When completed, the webpage will display books including title, author, and rating shown as stars
    # completed
    
    @app.route('/books', methods=['GET'])
    def show_books():
        # page = request.args.get('page', 1, type=int)
        # books = Book.query.paginate(page=page, per_page=BOOKS_PER_SHELF)
        # books_array = [book.format() for book in books.items]
        current_selection = paginate_books(request)
        
        if len(current_selection) == 0:
            abort(404)
            
        return jsonify({
            'success': True,
            'books': current_selection,
            'total_books': len(Book.query.all())
        })
        

    # @TODO: Write a route that will update a single book's rating.
    #         It should only be able to update the rating, not the entire representation
    #         and should follow API design principles regarding method and route.
    #         Response body keys: 'success'
    # TEST: When completed, you will be able to click on stars to update a book's rating and it will persist after refresh
    #completed
    @app.route('/books/<int:book_id>', methods=['PATCH'])
    def update_rating(book_id):
        rating = int(request.get_json()['rating'])
        try:
            edit_book = Book.query.filter(Book.id==book_id).one_or_none()
            if edit_book is None:
                abort(404)
                
            edit_book.rating = rating
            # db.session.add(edit_book)
            # db.session.commit()
            edit_book.update()  # will work just as the above two statements
            return jsonify({
                'success': True,
                'id': edit_book.id
            })
        except:
            abort(400)
        
    # @TODO: Write a route that will delete a single book.
    #        Response body keys: 'success', 'deleted'(id of deleted book), 'books' and 'total_books'
    #        Response body keys: 'success', 'books' and 'total_books'
    @app.route('/books/<int:book_id>', methods=['DELETE'])
    def delete_book(book_id):
        try:
            book_to_delete = Book.query.filter(Book.id==book_id).one_or_none()
            
            if book_to_delete == None:
                abort(404)
                
            # db.session.delete(book_to_delete)
            # db.session.commit()
            book_to_delete.delete()
            new_list = paginate_books(request)
            return jsonify({
                'success': True,
                'deleted': book_id,
                'books': new_list,
                'total_books': len(Book.query.all())
            })
        except:
            abort(422)
    # TEST: When completed, you will be able to delete a single book by clicking on the trashcan.
    #completed
    
    # @TODO: Write a route that create a new book.
    #        Response body keys: 'success', 'created'(id of created book), 'books' and 'total_books'
    # TEST: When completed, you will be able to a new book using the form. Try doing so from the last page of books.
    #       Your new book should show up immediately after you submit it at the end of the page.
    @app.route('/books', methods=['POST'])
    def create_book():
        book_title = request.get_json()['title']
        book_author = request.get_json()['author']
        book_rating = request.get_json()['rating']
        
        try:
            new_book = Book(title=book_title, author=book_author, rating=book_rating)
            # db.session.add(new_book)
            # db.session.commit()
            new_book.insert()
            
            current_books = paginate_books(request)
            return jsonify({
                'success': True,
                'created': new_book.id,
                'books': current_books,
                'total_books': len(Book.query.all())
            })

        except:
            abort(422)
           
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            'success': False,
            'error': 400,
            'message': 'Bad Request'
        }), 400      
            
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': 'Resource not found'
        }), 404
        
    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            'success': False,
            'error': 422,
            'message': 'unprocessable'
        }), 422
        
    @app.errorhandler(405)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 405,
            'message': 'Method not Allowed'
        })
    
    
    return app