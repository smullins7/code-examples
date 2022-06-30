import http
from typing import List

import flask
from flask import Blueprint, jsonify, request

from example_backend.exc.bad_request import BadRequest
from example_backend.exc.not_found import NotFound
from example_backend.posts import dao
from example_backend.users.service import auth_required

blueprint = Blueprint("post", __name__, url_prefix="/posts")


@blueprint.route("", methods=("POST",))
@auth_required(inject_user=True)
def create_post(user):
    request_json = flask.request.json

    if "title" not in request_json:
        raise BadRequest("Title is required")
    else:
        post = dao.insert(request_json["title"], request_json["content"], user.id)
        return post_to_json(post)


@blueprint.route("/<int:post_id>", methods=("GET",))
def get_post(post_id):
    post = dao.find(post_id)
    if post is None:
        raise NotFound(f"No post found with id {post_id}")
    return post_to_json(post)


@blueprint.route("/<int:post_id>", methods=("PUT",))
@auth_required()
def edit_post(post_id):
    get_post(post_id)
    json_data = request.get_json()
    if "title" not in json_data:
        raise BadRequest("Title is required")

    updated = dao.update(post_id, json_data["title"], json_data["content"])
    return post_to_json(updated)


@blueprint.route("/<int:post_id>", methods=("DELETE",))
@auth_required()
def delete_post(post_id):
    get_post(post_id)
    dao.delete(post_id)
    return "", http.HTTPStatus.NO_CONTENT


@blueprint.route("")
def index():
    return posts_to_json(dao.find_all())


def post_to_json(post: dao.Posts):
    return jsonify(post.to_dict())


def posts_to_json(posts: List[dao.Posts]):
    return jsonify([post.to_dict() for post in posts])
