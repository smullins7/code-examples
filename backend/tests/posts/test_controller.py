import unittest

from example_backend.app import app, db


def insert_test_post():
    db.engine.execute(
        "INSERT INTO Posts (id, title, content) VALUES (:post_id, :title, :content)",
        [{"post_id": 1, "title": "title-1", "content": "content-1"}],
    )


# TODO see if this is actually working
def insert_test_comment():
    db.engine.execute(
        "INSERT INTO Comments (id, post_id, content) VALUES (:comment_id, :post_id, :content)",
        [{"comment_id": 1, "post_id": 1, "content": "comment-content-1"}],
    )


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

    def test_create_succeeds(self):
        with app.test_client() as c:
            response_json = c.post(
                "/posts", json={"title": "unit test title", "content": "unit test content"}
            ).get_json()
            self.assertEqual(1, response_json["id"])
            self.assertEqual("unit test title", response_json["title"])
            self.assertEqual("unit test content", response_json["content"])
            self.assertIsNotNone(response_json["created"])

    def test_create_no_title_error(self):
        with app.test_client() as c:
            response = c.post("/posts", json={"content": "unit test content"})
            self.assertEqual(400, response.status_code)
            self.assertEqual("Title is required", response.get_json()["message"])

    def test_get_post_not_found(self):
        with app.test_client() as c:
            response = c.get("/posts/99")
            self.assertEqual(404, response.status_code)
            self.assertEqual("No post found with id 99", response.get_json()["message"])

    def test_get_post(self):
        insert_test_post()
        with app.test_client() as c:
            response = c.get("/posts/1")
            self.assertEqual(200, response.status_code)
            response_json = response.get_json()
            self.assertEqual(1, response_json["id"])
            self.assertEqual("title-1", response_json["title"])
            self.assertEqual("content-1", response_json["content"])
            self.assertIsNotNone(response_json.get("created"))

    def test_edit_post_no_title(self):
        insert_test_post()
        with app.test_client() as c:
            response = c.put("/posts/1", json={"content": "unit test content"})
            self.assertEqual(400, response.status_code)
            self.assertEqual("Title is required", response.get_json()["message"])

    def test_edit_post(self):
        insert_test_post()
        with app.test_client() as c:
            response = c.put("/posts/1", json={"title": "updated-title", "content": "updated-content"})
            self.assertEqual(200, response.status_code)
            response_json = response.get_json()
            self.assertEqual(1, response_json["id"])
            self.assertEqual("updated-title", response_json["title"])
            self.assertEqual("updated-content", response_json["content"])
            self.assertIsNotNone(response_json.get("created"))

    def test_delete(self):
        insert_test_post()
        with app.test_client() as c:
            response = c.delete("/posts/1")
            self.assertEqual(204, response.status_code)

    def test_delete_not_found(self):
        with app.test_client() as c:
            response = c.delete("/posts/99")
            self.assertEqual(404, response.status_code)
            self.assertEqual("No post found with id 99", response.get_json()["message"])

    def test_index_empty(self):
        with app.test_client() as c:
            response = c.get("/posts")
            self.assertEqual(200, response.status_code)
            self.assertEqual([], response.get_json())

    def test_index(self):
        insert_test_post()
        insert_test_comment()
        with app.test_client() as c:
            response = c.get("/posts")
            self.assertEqual(200, response.status_code)
            response_json = response.get_json()
            self.assertEqual(1, len(response_json))

            self.assertEqual(1, response_json[0]["id"])
            self.assertEqual("title-1", response_json[0]["title"])
            self.assertEqual("content-1", response_json[0]["content"])
            self.assertIsNotNone(response_json[0].get("created"))
