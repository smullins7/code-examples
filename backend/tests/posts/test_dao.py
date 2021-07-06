import unittest

from sqlalchemy.ext.declarative import declarative_base

from example_backend.app import app, db
from example_backend.posts import dao

Base = declarative_base()


class DAOTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://"

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.drop_all()

    def test_find(self):
        result = dao.find_all()
        self.assertEqual([], result)
