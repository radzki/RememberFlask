from flask_restx import fields
from flask_restx import Resource
from user import user_ns as ns

from app.domain.user import get_users

model = ns.model(
    'Model', {
        'name': fields.String,
        'id': fields.String(readonly=True),
    },
)

@ns.route('/', endpoint='user_list')
class UserList(Resource):
    @ns.marshal_with(model)
    def get(self):
        return get_users()
