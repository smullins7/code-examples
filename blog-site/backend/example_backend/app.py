import os
import uuid
from logging.config import dictConfig

from flask import Flask
from flask_alchemydumps import AlchemyDumps
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from example_backend.exc.bad_request import BadRequest, handle_bad_request
from example_backend.exc.not_found import NotFound, handle_not_found

dictConfig(
    {
        "version": 1,
        "formatters": {
            "default": {
                "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
            }
        },
        "handlers": {
            "wsgi": {
                "class": "logging.StreamHandler",
                "stream": "ext://flask.logging.wsgi_errors_stream",
                "formatter": "default",
            },
            "out": {
                "class": "logging.FileHandler",
                "filename": "/tmp/example.log",
                "formatter": "default",
            },
        },
        "root": {"level": "INFO", "handlers": ["out", "wsgi"]},
    }
)

app = Flask(__name__)
app.config["SECRET_KEY"] = str(uuid.uuid4())
# In a production app, credentials would be pulled from secret store
DB_HOST = os.environ.get("DB_HOST", "127.0.0.1")
app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://exampleuser:dev@{DB_HOST}/example"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
CORS(app)

app.register_error_handler(BadRequest, handle_bad_request)
app.register_error_handler(NotFound, handle_not_found)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

alchemydumps = AlchemyDumps(app, db)

from example_backend.comments import controller as comments_controller
from example_backend.posts import controller as posts_controller
from example_backend.users import controller as users_controller
