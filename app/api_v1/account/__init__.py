from flask import Blueprint
from api_v1 import api_v1_blueprint

account_v1_blueprint = Blueprint('account', __name__, url_prefix='/account')

api_v1_blueprint.register_blueprint(account_v1_blueprint)