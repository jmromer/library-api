from flask import Flask
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import config


db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)

    # @app.cli.command("db")

    from .api_v1 import api as api_v1_blueprint
    app.register_blueprint(api_v1_blueprint, url_prefix='/api/v1')

    return app
