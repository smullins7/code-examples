from sqlalchemy_serializer import SerializerMixin

from example_backend.app import db


class User(db.Model, SerializerMixin):
    __tablename__ = "users"

    serialize_only = ("id", "created", "email", "name")

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, server_default=db.func.now())
    email = db.Column(db.String())
    name = db.Column(db.String())

    def __init__(self, email, name):
        self.email = email
        self.name = name


def insert(email, name):
    user = User(email, name)
    db.session.add(user)
    db.session.commit()
    return user


def find(user_id):
    return db.session.query(User).get(user_id).first()


def find_by_email(email):
    return db.session.query(User).filter(User.email == email).first()
