from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from app.config import settings

# Database configurations
engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get the database session


def get_db() -> DeclarativeMeta:  # type: ignore
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
