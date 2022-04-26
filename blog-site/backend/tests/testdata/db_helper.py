from example_backend.app import app, db


def config_db():
    app.config["SERVER_NAME"] = "localhost:5000"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://"


def create_db():
    db.create_all()


def clear_db():
    db.drop_all()


def insert_post():
    db.engine.execute(
        "INSERT INTO Posts (id, title, content) VALUES (:post_id, :title, :content)",
        [{"post_id": 1, "title": "title-1", "content": "content-1"}],
    )
