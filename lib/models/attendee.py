
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship, validates
from lib.event_wizard_db import Base


class Attendee(Base):
    __tablename__ = "attendees"

    id = Column(Integer, primary_key=True)
    sex = Column(String, nullable=False) 
    age = Column(Integer, nullable=False)
    ticket_price = Column(Integer, nullable=False)
    checked_in = Column(Boolean, default=False)
    event_id = Column(Integer, ForeignKey("events.id"), nullable=False)

  
    event = relationship("Event", back_populates="attendees")

    def __repr__(self):
        return f"<Attendee {self.id}: {self.sex}, Age: {self.age},Ticket Price: KSh{self.ticket_price}, Checked in: {self.checked_in}, Event ID: {self.event_id}>"
    
    @validates("sex")
    def validate_sex(self, key, value):
        if value not in ("M", "F", "Other"):
            raise ValueError("Sex must be 'M', 'F', or 'Other'")
        return value

    @validates("age")
    def validate_age(self, key, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Age must be a positive number")
        return value

    @validates("ticket_price")
    def validate_price(self, key, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Ticket price must be a number in KSh")
        return value 
