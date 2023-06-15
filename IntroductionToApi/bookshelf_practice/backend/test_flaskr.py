import unittest
import os
import json
from flaskr import create_app
from models import setup_db, Book, db


class BookTestCase(unittest.TestCase):
    """This class represents the trivia test case"""
    
    def setUp(self):
        """Define test variables and initialize app."""
        self.database_path = "postgresql://_beast101_:admin@localhost:5432/test_db"
        self.app = create_app(self.database_path)
        self.client = self.app.test_client
        
        self.new_book = {"title": "Anansi Boys", "author": "Neil Gaiman", "rating": 5}
        
    
    def tearDown(self):
        """Executed after reach test"""
        pass
    
# @TODO: Write at least two tests for each endpoint - one each for success and error behavior.
#        You can feel free to write additional tests for nuanced functionality,
#        Such as adding a book without a rating, etc.
#        Since there are four routes currently, you should have at least eight tests.
# Optional: Update the book information in setUp to make the test database your own!

    def test_paginate_books(self):
        res = self.client().get('/books')
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['books'])
        self.assertTrue(data['total_books'])
        
    def test_404_beyond_value_page(self):
        res = self.client().get('/books?page=100', json={'rating': 1})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code,404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found')
        
    def test_change_rating(self):
        res = self.client().patch('/books/5', json={'rating': 1})
        data = json.loads(res.data)
        with self.app.app_context():
            book = Book.query.filter(Book.id == 5).one_or_none()
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(book.format()['rating'], 1)
        
    def test_400_change_rating(self):
        res = self.client().patch('/books/5')
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Bad Request')
        
    def test_delete_book(self):
        with self.app.app_context():
            book_to_delete = Book(id=2, title='Asymmetry: A Novel', author='Lisa Halliday', rating=4)
            db.session.add(book_to_delete)
            db.session.commit()
        res = self.client().delete('/books/2')
        data = json.loads(res.data)
        with self.app.app_context():
            book = Book.query.filter(Book.id == 2).one_or_none()
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 2)
        self.assertTrue(len(data['books']))
        self.assertTrue(data['total_books'])
        self.assertEqual(book, None)
        
    def test_422_if_book_doesnot_exist(self):
        res = self.client().delete('/books/1000')
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')
        
    def test_create_book(self):
        res = self.client().post('/books', json=self.new_book)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])
        self.assertTrue(data['total_books'])
        self.assertTrue(len(data['books']))
    
    def test_405_if_book_creation_not_allowed(self):
        res = self.client().post('/books/45', json=self.new_book)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['error'], 405)
        self.assertEqual(data['message'], 'Method not Allowed')
        

# Make the tests conveniently executable    
    
if __name__ == "__main__":
    unittest.main()
            