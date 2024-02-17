from app import db
from app.domain.model import User

def get_users():
    return db.session.query(User)

def list_users():
    return get_users().all()