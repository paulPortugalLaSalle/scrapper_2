from sqlalchemy import Column, DateTime, Integer, Numeric, Text, text
from sqlalchemy.orm import relationship

from src.models.base import Base


class Bid(Base):
    __tablename__ = "Bids"

    nomenclature = Column(Text)
    number = Column(Integer)
    regulation = Column(Text)
    seace_version = Column(Text)
    seace_id = Column(Text, unique=True)
    address = Column(Text)
    website = Column(Text)
    phone = Column(Text)
    object_type = Column(Text)
    purchase_type = Column(Text)
    estimated_amount = Column(Numeric)
    publication = Column(DateTime(True))
    description = Column(Text)
    entity = Column(Text)
    ruc = Column(Text)
    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('\"Bids_id_seq\"'::regclass)"),
    )
    publication_restart = Column(DateTime(True))
    created_at = Column(DateTime(True), server_default=text("now()"))
    updated_at = Column(DateTime(True), server_default=text("now()"))
    department = Column(Text)
    province = Column(Text)
    district = Column(Text)
    ubigeo = Column(Text)

    milestones = relationship("Milestone", back_populates="bid", lazy="joined")
    documents = relationship("Document", back_populates="bid", lazy="joined")
    items = relationship("Item", back_populates="bid", lazy="joined")
