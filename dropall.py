from sqlalchemy import text

from app import app
from app import db

if __name__ == '__main__':
    with app.app_context():
        with db.engine.begin() as conn:
            conn.execute(text('DROP TABLE alembic_version;'))

        db.drop_all()
