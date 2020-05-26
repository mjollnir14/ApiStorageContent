from flask import Flask
from flask_alembic import Alembic

from api_storage_content.models import db
from api_storage_content.apis import api_v1


def create_app():
    app = Flask(__name__)
    app.config.from_object('api_storage_content.config.settings')

    db.init_app(app)
    api_v1.init_app(app)
    Alembic(app)

    return app
