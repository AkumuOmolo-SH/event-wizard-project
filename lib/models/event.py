# models/event.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, validates
from lib.event_wizard_db import Base


class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    tickets_sold = Column(Integer, default=0)
    location_id = Column(Integer, ForeignKey("locations.id"))

    attendees = relationship("Attendee", back_populates="event")   
    location = relationship("Location", back_populates="events")   

    def __repr__(self):
        return f"<Event {self.id}: {self.name}, Tickets Sold: {self.tickets_sold}, Location ID: {self.location_id}>"

    @validates("name")
    def validate_name(self, key, value):
        if not value or not value.strip():
            raise ValueError("Event name cannot be empty")
        return value.strip()

    @validates("tickets_sold")
    def validate_tickets(self, key, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Tickets sold must be a non-negative integer")
        return value