from flask_restx import Namespace

user_ns = Namespace(name='users', description='User operations', validate=True)
