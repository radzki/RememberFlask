from flask import Blueprint
from flask_restx import Api

from app.api.v1.user import user_ns

api_v1_bp = Blueprint('API v1', __name__, url_prefix='/api/v1')
api_v1 = Api(api_v1_bp, version='1.0', title='Remember Flask API')


api_v1.add_namespace(user_ns, path='/users')
