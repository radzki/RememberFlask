from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from app.domain.model import DbBaseModel


db = SQLAlchemy(model_class=DbBaseModel)
migrate = Migrate()


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    from app.api.v1 import api_v1_bp
    app.register_blueprint(api_v1_bp)

    db.init_app(app)
    migrate.init_app(app, db)

    return app
