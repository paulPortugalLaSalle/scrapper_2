from os import environ
from contextlib import contextmanager

from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from typing import List

from src.models.base import Base

DB_TEST_HOST = environ.get("DB_TEST_HOST")
DB_TEST_PORT = environ.get("DB_TEST_PORT")
DB_TEST_NAME = environ.get("DB_TEST_NAME")
DB_TEST_USER = environ.get("DB_TEST_USER")
DB_TEST_PASSWORD = environ.get("DB_TEST_PASSWORD")

DB_HOST = environ.get("DB_HOST")
DB_PORT = environ.get("DB_PORT")
DB_NAME = environ.get("DB_NAME")
DB_USER = environ.get("DB_USER")
DB_PASSWORD = environ.get("DB_PASSWORD")

class DatabaseSession:
    def __init__(self):
        db_url = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
        if environ.get("DEBUG"):
            db_url = f"postgresql://{DB_TEST_USER}:{DB_TEST_PASSWORD}@{DB_TEST_HOST}:{DB_TEST_PORT}/{DB_TEST_NAME}"
        self.DATABASE_URL = db_url
        self.engine = create_engine(self.DATABASE_URL)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

        self._create_tables_if_not_exist()

    def _create_tables_if_not_exist(self):
        # Obtener el inspector
        inspector = inspect(self.engine)

        # Verificar si alguna tabla no existe
        todas_las_tablas = Base.metadata.tables.keys()
        tablas_existentes = inspector.get_table_names()

        if not all(tabla in tablas_existentes for tabla in todas_las_tablas):
            # Si falta alguna tabla, crear todas
            Base.metadata.create_all(bind=self.engine)
            print("Se han creado las tablas faltantes en la base de datos.")
        else:
            print("Todas las tablas ya existen en la base de datos.")

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
