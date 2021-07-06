from sqlalchemy_serializer import SerializerMixin

from example_backend.app import db


class Posts(db.Model, SerializerMixin):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, server_default=db.func.now())
    title = db.Column(db.String())
    content = db.Column(db.String())

    def __init__(self, title, content):
        self.title = title
        self.content = content


def insert(title, content):
    post = Posts(title=title, content=content)
    db.session.add(post)
    db.session.commit()
    return post


def find(post_id):
    return db.session.query(Posts).get(post_id)


def find_all():
    return db.session.query(Posts).all()


def delete(post_id):
    post = find(post_id)
    db.session.delete(post)
    db.session.commit()


def update(post_id, title, content):
    post = find(post_id)
    if not post:
        return None

    post.title = title
    post.content = content
    db.session.commit()
    return post
