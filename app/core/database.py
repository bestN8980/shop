from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from app.core.config import DATABASE_URL

#Create engine to connect to database
engine = create_engine(DATABASE_URL)

#A factory to create session
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

#Create class Base for all models to inheritate
Base = declarative_base()
