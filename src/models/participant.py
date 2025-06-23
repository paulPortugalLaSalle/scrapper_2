from sqlalchemy import Column, ForeignKey, Integer, Numeric, Text, text
from sqlalchemy.orm import relationship

from src.models.base import Base


class Participant(Base):
    __tablename__ = "Participants"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('\"Participants_id_seq\"'::regclass)"),
    )
    ruc = Column(Text)
    name = Column(Text)
    MYPE = Column(Text)
    promotion_law = Column(Text)
    bonus = Column(Text)
    awarded_count = Column(Integer)
    awarded_amount = Column(Numeric)
    item_id = Column(ForeignKey("Items.id", ondelete="CASCADE"), index=True)

    item = relationship("Item", back_populates="participants")
