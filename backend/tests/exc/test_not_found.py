import unittest

from example_backend.app import app
from example_backend.exc.not_found import NotFound, handle_not_found

NOT_FOUND = NotFound("unit test message")


class NotFoundTestCase(unittest.TestCase):

    def setUp(self):
        self.app_context = app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_to_dict(self):
        self.assertEqual("unit test message", NOT_FOUND.message)
        self.assertEqual(404, NOT_FOUND.status_code)
        self.assertEqual({"message": "unit test message"}, NOT_FOUND.to_dict())

    def test_handle_not_found(self):
        response = handle_not_found(NOT_FOUND)
        self.assertEqual(NOT_FOUND.status_code, response.status_code)
        self.assertEqual({"message": "unit test message"}, response.json)
