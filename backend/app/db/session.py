import os
from contextlib import contextmanager
from typing import Callable

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

engine = create_engine(os.getenv("DATABASE_URL"), pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
DatabaseSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@contextmanager
def session_manager(session_factory: Callable[[], Session] = DatabaseSession):
    session = session_factory()
    try:
        yield session
    finally:
        session.close()


Base = declarative_base()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
