
from app import app, db
from sqlalchemy import text

if __name__ == "__main__":
    with app.app_context():
        with db.engine.begin() as conn:
            conn.execute(text("DROP TABLE alembic_version;"))

        db.drop_all()