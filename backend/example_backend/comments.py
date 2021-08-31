from flask import jsonify
from sqlalchemy import func
from werkzeug.exceptions import abort

from example_backend.app import app, db


class Comments(db.Model):
    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, server_default=db.func.now())
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"))
    content = db.Column(db.String())
    # comments = db.relationship('Post', backref=db.backref('comment'), lazy='dynamic')

    def __init__(self, post_id, content):
        self.post_id = post_id
        self.content = content


def db_get_comment(comment_id):
    post = db.session.query(Comments).get(comment_id)
    if post is None:
        abort(404)
    return post


@app.route("/comments/<int:comment_id>")
def get_comment(comment_id):
    return jsonify(db_get_comment(comment_id))


def get_comments(post_id):
    return db.session.query(Comments).filter(Comments.post_id == post_id).all()


def get_comment_counts():
    return dict(db.session.query(Comments.post_id, func.count(Comments.post_id)).group_by(Comments.post_id).all())
