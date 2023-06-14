import unittest
import json
from flaskr import create_app
from models import setup_db

class ResourceTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.database = 'test_db'
        self.database_path = f"postgres://_beast101_:admin@localhost:5432/{self.database}"
        setup_db(self.app, self.database_path)