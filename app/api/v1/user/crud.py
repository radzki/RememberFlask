from app.domain.user import get_users
from user import user_ns as ns
from flask_restx import Resource, fields

model = ns.model('Model', {
    'name': fields.String,
    'id': fields.String(readonly=True)
})

@ns.route('/cacaca')
class UserList(Resource):
    @ns.marshal_with(model)
    def get(self):
        return get_users()
