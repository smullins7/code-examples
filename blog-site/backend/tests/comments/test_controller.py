from tests.base_classes import BaseControllerTestCase
from tests.testdata.db_helper import insert_comment, insert_post


class CommentsControllerTestCase(BaseControllerTestCase):
    def test_create_succeeds(self):
        insert_post()
        with self.client as c:
            response_json = c.post("/posts/1/comments", json={"content": "unit test content"}).get_json()
            self.assertEqual(1, response_json["id"])
            self.assertEqual("unit test content", response_json["content"])
            self.assertIsNotNone(response_json["created"])

    def test_get_comment_post_not_found(self):
        with self.client as c:
            response = c.get("/posts/99/comments/88")
            self.assertEqual(404, response.status_code)
            self.assertEqual("No post found with id 99", response.get_json()["message"])

    def test_get_comment_not_found(self):
        insert_post()
        with self.client as c:
            response = c.get("/posts/1/comments/88")
            self.assertEqual(404, response.status_code)
            self.assertEqual("No comment found with id 88", response.get_json()["message"])

    def test_get_comment(self):
        insert_post()
        insert_comment()
        with self.client as c:
            response = c.get("/posts/1/comments/1")
            self.assertEqual(200, response.status_code)
            response_json = response.get_json()
            self.assertEqual(1, response_json["id"])
            self.assertEqual("content-1", response_json["content"])
            self.assertIsNotNone(response_json.get("created"))

    def test_edit_comment(self):
        insert_post()
        insert_comment()
        with self.client as c:
            response = c.put("/posts/1/comments/1", json={"content": "updated-content"})
            self.assertEqual(200, response.status_code)
            response_json = response.get_json()
            self.assertEqual(1, response_json["id"])
            self.assertEqual("updated-content", response_json["content"])
            self.assertIsNotNone(response_json.get("created"))

    def test_delete(self):
        insert_post()
        insert_comment()
        with self.client as c:
            response = c.delete("/posts/1/comments/1")
            self.assertEqual(204, response.status_code)

    def test_delete_post_not_found(self):
        with self.client as c:
            response = c.delete("/posts/99")
            self.assertEqual(404, response.status_code)
            self.assertEqual("No post found with id 99", response.get_json()["message"])

    def test_delete_comment_not_found(self):
        insert_post()
        with self.client as c:
            response = c.delete("/posts/1/comments/88")
            self.assertEqual(404, response.status_code)
            self.assertEqual("No comment found with id 88", response.get_json()["message"])

    def test_get_comments_empty(self):
        with self.client as c:
            response = c.get("/posts")
            self.assertEqual(200, response.status_code)
            self.assertEqual([], response.get_json())

    def test_get_comments(self):
        insert_post()
        insert_comment()
        with self.client as c:
            response = c.get("/posts")
            self.assertEqual(200, response.status_code)
            response_json = response.get_json()
            self.assertEqual(1, len(response_json))

            self.assertEqual(1, response_json[0]["id"])
            self.assertEqual("title-1", response_json[0]["title"])
            self.assertEqual("content-1", response_json[0]["content"])
            self.assertIsNotNone(response_json[0].get("created"))
