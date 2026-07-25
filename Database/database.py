from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from Database.models import Base

DATABASE_URL = "sqlite:///ene.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=engine
)


def init_db():
    Base.metadata.create_all(bind=engine)