import http

import flask
from flask import jsonify, redirect, request, url_for
from werkzeug.exceptions import abort

from example_backend.app import app
from example_backend.posts import dao


class BadRequest(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv["message"] = self.message
        return rv


@app.errorhandler(BadRequest)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@app.route("/posts/create", methods=("POST",))
def create():
    request_json = flask.request.json

    if "title" not in request_json:
        raise BadRequest("Title is required")
    else:
        post = dao.insert(request_json["title"], request_json["content"])
        return jsonify(post.to_dict())


@app.route("/posts/<int:post_id>")
def get_post(post_id):
    post = dao.find(post_id)
    if post is None:
        abort(404)
    # from comments import get_comments
    return jsonify(post.to_dict())


@app.route("/posts/<int:post_id>/edit", methods=("GET", "POST"))
def edit(post_id):
    post = get_post(post_id)
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]

        if not title:
            raise BadRequest("Title is required")
        else:
            dao.update(post_id, title, content)
            return redirect(url_for("index"))

    return jsonify(post.to_dict())


@app.route("/posts<int:post_id>/delete", methods=("POST",))
def delete(post_id):
    dao.delete(post_id)
    return "", http.HTTPStatus.NO_CONTENT


@app.route("/posts")
def index():
    return jsonify([post.to_dict() for post in dao.find_all()])
