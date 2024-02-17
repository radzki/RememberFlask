from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from app.api.v1 import api_v1
from app.domain.model import DbBaseModel


app = Flask(__name__)
db = SQLAlchemy(model_class=DbBaseModel)
migrate = Migrate(app, db)

def create_app(app):
    app.config.from_object('config.Config')


    db.init_app(app)
    migrate.init_app(app, db)

    api_v1.init_app(app)


create_app(app)
