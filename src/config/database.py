import os
from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import List

DB_TEST_HOST = os.getenv("DB_TEST_HOST")
DB_TEST_PORT = os.getenv("DB_TEST_PORT")
DB_TEST_NAME = os.getenv("DB_TEST_NAME")
DB_TEST_USER = os.getenv("DB_TEST_USER")
DB_TEST_PASSWORD = os.getenv("DB_TEST_PASSWORD")

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

class DatabaseSession:
    def __init__(self):
        db_url = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
        if os.getenv("DEBUG"):
            db_url = f"postgresql://{DB_TEST_USER}:{DB_TEST_PASSWORD}@{DB_TEST_HOST}:{DB_TEST_PORT}/{DB_TEST_NAME}"
        self.DATABASE_URL = db_url
        self.engine = create_engine(self.DATABASE_URL)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    @contextmanager
    def get_session(self):
        session = self.SessionLocal()
        try:
            yield session
            session.commit()
        except Exception as e:
            session.rollback()
            print(f"Connection failed: {str(e)}")
            raise
        finally:
            session.close()
