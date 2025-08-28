
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from lib.event_wizard_db import Base
from sqlalchemy.orm import validates


class Location(Base):
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    capacity = Column(Integer, nullable=False)
    num_bars = Column(Integer, default=0)
    num_toilets = Column(Integer, default=0)

    events = relationship("Event", back_populates="location")
   
    @validates("name")
    def validate_name(self, key, value):
        if not value or not value.strip():
            raise ValueError("Location name cannot be empty")
        return value.strip()

    @validates("capacity")
    def validate_capacity(self, key, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Capacity must be a positive number")
        return value

    @validates("num_bars", "num_toilets")
    def validate_non_negative(self, key, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError(f"{key} cannot be negative number")
        return value

    @classmethod
    def suggest_location(cls, expected_attendees, session):
        return session.query(cls).filter(cls.capacity >= expected_attendees).all()
    
    def __repr__(self):
        return (
            f"<Location(name='{self.name}', capacity={self.capacity}, "
            f"bars={self.num_bars}, toilets={self.num_toilets})>"
        )


  
