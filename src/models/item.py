from sqlalchemy import Column, ForeignKey, Integer, Numeric, Text, text
from sqlalchemy.orm import relationship

from src.models.base import Base


class Item(Base):
    __tablename__ = "Items"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('\"Items_id_seq\"'::regclass)"),
    )
    quantity = Column(Integer)
    cubso_code = Column(Text)
    description = Column(Text)
    object_type = Column(Text)
    state = Column(Text)
    number = Column(Integer)
    estimated_amount = Column(Numeric)
    currency = Column(Text)
    MYPE_reservation = Column(Text)
    package = Column(Text)
    seace_id = Column(Text)
    bid_id = Column(ForeignKey("Bids.id", ondelete="CASCADE"), index=True)

    bid = relationship("Bid", back_populates="items", lazy="joined")
    participants = relationship("Participant", back_populates="item")
