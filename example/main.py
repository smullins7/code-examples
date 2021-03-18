from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import uuid

app = Flask(__name__)
app.config['SECRET_KEY'] = str(uuid.uuid4())
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.sqlite3'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

import posts, comments