from sqlalchemy import create_engine
from sqlalchemy import Engine

from app import app

app_engine: Engine = create_engine(
    app.config['DATABASE_URI'],
)
