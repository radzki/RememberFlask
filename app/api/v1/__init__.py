from app.api.v1.user import user_ns
from flask_restx import Api


api_v1 = Api(version='1.0', title='Remember Flask API', prefix='/v1')


api_v1.add_namespace(user_ns, path='/users')