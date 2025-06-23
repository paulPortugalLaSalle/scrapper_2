from sqlalchemy import Column, ForeignKey, Integer, Text, text
from sqlalchemy.orm import relationship

from src.models.base import Base


class Document(Base):
    __tablename__ = "Documents"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('\"Documentations_id_seq\"'::regclass)"),
    )
    stage = Column(Text)
    type = Column(Text)
    seace_id = Column(Text)
    name = Column(Text)
    bid_id = Column(ForeignKey("Bids.id", ondelete="CASCADE"), index=True)
    order = Column(Text)

    bid = relationship("Bid", back_populates="documents")
