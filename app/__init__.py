from flask import Flask
from flask_migrate import Migrate
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy

from .api_v1 import api_v1_blueprint
from app.domain.model.base import DbBaseModel

app = Flask(__name__)
api = Api(app, version='1.0', title='Remember Flask API')
db = SQLAlchemy(model_class=DbBaseModel)
migrate = Migrate(app, db)

def create_app(app):
    app.register_blueprint(api_v1_blueprint)
    app.config.from_object('config.Config')

    db.init_app(app)

    #from app.domain.model import BasicModel, PrimaryKeyMixin, User

    migrate.init_app(app, db)


create_app(app)
