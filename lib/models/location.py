
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from event_wizard_db import Base

class Location(Base):
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    capacity = Column(Integer, nullable=False)
    num_bars = Column(Integer, default=0)
    num_toilets = Column(Integer, default=0)

    events = relationship("Event", back_populates="location")

    def __repr__(self):
        return (
            f"<Location(name='{self.name}', capacity={self.capacity}, "
            f"bars={self.num_bars}, toilets={self.num_toilets})>"
        )
