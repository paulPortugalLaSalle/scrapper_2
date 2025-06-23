from sqlalchemy import Boolean, Column, DateTime, Integer, String, text

from src.models.base import Base


class User(Base):
    __tablename__ = "User"

    password = Column(String(128), nullable=False)
    last_login = Column(DateTime(True))
    is_superuser = Column(Boolean, nullable=False)
    first_name = Column(String(30), nullable=False)
    last_name = Column(String(150), nullable=False)
    email = Column(String(254), nullable=False, unique=True)
    is_staff = Column(Boolean, nullable=False)
    is_active = Column(Boolean, nullable=False)
    date_joined = Column(DateTime(True), nullable=False)
    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('\"User_id_seq\"'::regclass)"),
    )
