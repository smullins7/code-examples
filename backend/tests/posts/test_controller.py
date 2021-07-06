import unittest

from example_backend.app import app, db
from example_backend.posts.controller import BadRequest, handle_invalid_usage

BAD_REQ = BadRequest("unit test message", status_code=401, payload={"k1": "v1"})


class PostsControllerTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        app.config["SERVER_NAME"] = "localhost:5000"
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://"
        cls.client = app.test_client()

    def setUp(self):
        db.create_all()
        self.app_context = app.app_context()
        self.app_context.push()

    def tearDown(self):
        db.drop_all()
        self.app_context.pop()

    def test_to_dict(self):
        self.assertEqual("unit test message", BAD_REQ.message)
        self.assertEqual(401, BAD_REQ.status_code)
        self.assertEqual({"k1": "v1", "message": "unit test message"}, BAD_REQ.to_dict())

    def test_to_dict_default_status_code_no_payload(self):
        bad_req = BadRequest("unit test message")
        self.assertEqual("unit test message", bad_req.message)
        self.assertEqual(400, bad_req.status_code)
        self.assertEqual({"message": "unit test message"}, bad_req.to_dict())

    def test_handle_invalid_usage(self):
        response = handle_invalid_usage(BAD_REQ)
        self.assertEqual(BAD_REQ.status_code, response.status_code)
        self.assertEqual({"k1": "v1", "message": "unit test message"}, response.json)

    def test_create_succeeds(self):
        with app.test_client() as c:
            response_json = c.post(
                "/posts/create", json={"title": "unit test title", "content": "unit test content"}
            ).get_json()
            self.assertEqual(1, response_json["id"])
            self.assertEqual("unit test title", response_json["title"])
            self.assertEqual("unit test content", response_json["content"])
            self.assertIsNotNone(response_json["created"])

    def test_create_no_title_error(self):
        with app.test_client() as c:
            response = c.post("/posts/create", json={"content": "unit test content"})
            self.assertEqual(400, response.status_code)
            self.assertEqual("Title is required", response.get_json()["message"])

    def test_get_post_not_found(self):
        with app.test_client() as c:
            pass

    def test_get_post(self):
        with app.test_client() as c:
            pass

    def test_edit_get(self):
        with app.test_client() as c:
            pass

    def test_edit_post_no_title(self):
        with app.test_client() as c:
            pass

    def test_edit_post(self):
        with app.test_client() as c:
            pass

    def test_delete(self):
        with app.test_client() as c:
            pass

    def test_delete_not_found(self):
        with app.test_client() as c:
            pass

    def test_index_empty(self):
        with app.test_client() as c:
            pass

    def test_index(self):
        with app.test_client() as c:
            pass
