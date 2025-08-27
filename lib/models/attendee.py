
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from event_wizard_db import Base


class Attendee(Base):
    __tablename__ = "attendees"

    id = Column(Integer, primary_key=True)
    sex = Column(String, nullable=False) 
    age = Column(Integer, nullable=False)
    ticket_price = Column(Integer, nullable=False)
    checked_in = Column(Boolean, default=False)
    event_id = Column(Integer, ForeignKey("events.id"), nullable=False)

    # Relationship back to Event (optional, depends on your Event model)
    event = relationship("Event", back_populates="attendees")

    def __repr__(self):
        return f"<Attendee {self.id}: {self.sex}, Age: {self.age}, Checked in: {self.checked_in}, Event ID: {self.event_id}>"
