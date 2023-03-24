import os

from flask import Flask
from flask_migrate import Migrate

from db import db

from resources.index import blp as IndexBlueprint

def create_app(db_url=None):
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL", "sqlite:///data.db")
    app.config["FLASK_DEBUG"] = 1
    db.init_app(app)
    migrate = Migrate(app, db)

    app.register_blueprint(IndexBlueprint)

    return app