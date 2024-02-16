from account import account_v1_blueprint

@account_v1_blueprint.route('/<id>')
def read_account(id):
    return f'Batata {id}'
