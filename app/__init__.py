from flask import Flask
from flask_restx import Api, Resource, fields
from .api_v1 import api_v1_blueprint

app = Flask(__name__)
api = Api(app, version='1.0', title='Remember Flask API')

def create_app(app):
    app.register_blueprint(api_v1_blueprint)


create_app(app)