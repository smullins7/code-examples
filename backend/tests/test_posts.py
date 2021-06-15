import unittest

from example_backend.posts import BadRequest


class BadRequestTestCase(unittest.TestCase):
    def test_to_dict(self):
        bad_request = BadRequest("unit test message", status_code=401, payload={"k1": "v1"})
        self.assertEqual("unit test message", bad_request.message)
        self.assertEqual(401, bad_request.status_code)
        self.assertEqual({"k1": "v1", "message": "unit test message"}, bad_request.to_dict())
