import http

import flask
from flask import request, url_for, redirect, jsonify
from sqlalchemy_serializer import SerializerMixin
from werkzeug.exceptions import abort

from app import app, db


class Posts(db.Model, SerializerMixin):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, server_default=db.func.now())
    title = db.Column(db.String())
    content = db.Column(db.String())

    def __init__(self, title, content):
        self.title = title
        self.content = content


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
        rv['message'] = self.message
        return rv


@app.errorhandler(BadRequest)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@app.route('/create', methods=('POST', ))
def create():
    request_json = flask.request.json

    if "title" not in request_json:
        raise BadRequest('Title is required')
    else:
        post = Posts(title=request_json["title"], content=request_json["content"])
        db.session.add(post)
        db.session.commit()
        return jsonify(post.to_dict())


@app.route('/<int:post_id>')
def get_post(post_id):
    post = db.session.query(Posts).get(post_id)
    if post is None:
        abort(404)
    #from comments import get_comments
    return jsonify(post.to_dict())


@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            raise BadRequest('Title is required')
        else:
            post.title = title
            post.content = content
            db.session.commit()
            return redirect(url_for('index'))

    return jsonify(post.to_dict())


@app.route('/<int:post_id>/delete', methods=('POST',))
def delete(post_id):
    post = get_post(post_id)
    db.session.delete(post)
    db.session.commit()
    return '', http.HTTPStatus.NO_CONTENT


@app.route('/')
def index():
    posts = db.session.query(Posts).all()
    # from comments import get_comment_counts

    return jsonify([post.to_dict() for post in posts])
