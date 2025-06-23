from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, Text, text
from sqlalchemy.orm import relationship

from src.models.base import Base


class Milestone(Base):
    __tablename__ = "Milestones"

    id = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('\"Milestones_id_seq\"'::regclass)"),
    )
    description = Column(Text)
    start = Column(DateTime(True))
    end = Column(DateTime(True))
    start_time_specified = Column(Boolean)
    end_time_specified = Column(Boolean)
    location = Column(Text)
    bid_id = Column(ForeignKey("Bids.id", ondelete="CASCADE"), index=True)

    bid = relationship("Bid", back_populates="milestones")
