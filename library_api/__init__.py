import os

from flask_api import FlaskAPI
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import config

db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()


def seed_database():
    from .models.request import Request  # noqa
    print('Seeding database...')
    Request.query.delete()

    # yapf: disable
    reqs = [
        {'email': 'email1@example.com', 'title': 'Book 1'},
        {'email': 'email2@example.com', 'title': 'Book 2'},
        {'email': 'email3@example.com', 'title': 'Book 3'},
        {'email': 'email4@example.com', 'title': 'Book 4'},
        {'email': 'email5@example.com', 'title': 'Book 5'},
    ]
    # yapf: enable

    for req in reqs:
        db.session.add(Request(**req))

    db.session.commit()

    records_count = Request.query.count()
    print(f'done. Created {records_count} Requests')


def create_app(cfg=None):
    cfg = cfg or config[os.environ['FLASK_ENV']]
    app = FlaskAPI(__name__)
    app.config.from_object(cfg)

    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)

    @app.cli.command("db:seed")
    def db_seed():
        """Seed the database."""
        return seed_database()

    from .api_index import api as api_index_blueprint
    app.register_blueprint(api_index_blueprint, url_prefix='')

    from .api_v1 import api as api_v1_blueprint
    app.register_blueprint(api_v1_blueprint, url_prefix='/api/v1')

    return app
