from sqlalchemy import create_engine
from src.db.config import settings

engine = create_engine(
    settings.DATABASE_URL_psycopg,
    echo=True
)