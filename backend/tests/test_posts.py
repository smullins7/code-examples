import unittest

from example_backend.posts import BadRequest


class BadRequestTestCase(unittest.TestCase):
    def test_to_dict(self):
        self.assertEqual({}, BadRequest("unit test message", status_code=401, payload={"k1": "v1"}))
