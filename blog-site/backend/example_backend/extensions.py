from flask_alchemydumps import AlchemyDumps
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()
alchemydumps = AlchemyDumps()
