import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from example_backend.posts import dao
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class DAOTestCase(unittest.TestCase):
    engine = create_engine('sqlite:///:memory:')
    Session = sessionmaker(bind=engine)
    session = Session()

    def setUp(self):
        Base.metadata.create_all(self.engine)

    def tearDown(self):
        Base.metadata.drop_all(self.engine)

    def test_find(self):
        result = dao.find_all()
        self.assertEqual([], result)
