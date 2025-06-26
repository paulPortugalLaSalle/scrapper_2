import logging
from datetime import datetime

from sqlalchemy.exc import SQLAlchemyError

from src.config.database import DatabaseSession
from src.models import User


class UserOperations:
    def __init__(self):
        self.db = DatabaseSession()

    def create_user(self, first_name: str, last_name: str, email: str, password: str,
                    is_superuser: bool = False, is_staff: bool = False, is_active: bool = True):
        with self.db.get_session() as session:
            try:
                new_user = User(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    password=password,  # Note: Password should be hashed before storing
                    is_superuser=is_superuser,
                    is_staff=is_staff,
                    is_active=is_active,
                    date_joined=datetime.now(),
                    last_login=None
                )
                session.add(new_user)
                session.commit()
                return new_user
            except SQLAlchemyError as e:
                logging.info(e)

    def list_users(self):
        with self.db.get_session() as session:
            users = session.query(User).all()
            return users
