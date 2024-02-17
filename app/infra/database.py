from sqlalchemy import Engine, create_engine
from app import app

app_engine: Engine = create_engine(
    app.config['DATABASE_URI']
)