from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship, validates
from lib.event_wizard_db import Base


class Safety(Base):
    __tablename__ = "safety"

    id = Column(Integer, primary_key=True)
    ambulances = Column(Integer, default=0)
    nurses = Column(Integer, default=0)
    security_staff = Column(Integer, default=0)
    event_id = Column(Integer, ForeignKey("events.id"),
                      nullable=False, unique=True)

    event = relationship("Event", back_populates="safety")
    # location = relationship("Location", back_populates="safety")

    def __repr__(self):
        return (
            f"<Safety {self.id}: Event {self.event_id}, "
            f"Ambulances={self.ambulances}, Nurses={self.nurses}, Security={self.security_staff}>"
        )

    @validates("ambulances", "nurses", "security_staff")
    def validate_non_negative(self, key, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError(f"{key} must be a positive number")
        return value

    @staticmethod
    def suggest_staff(expected_attendees):
        expected_attendees = int(expected_attendees)

        security_staff = max(15, expected_attendees // 100)
        nurses = max(6, expected_attendees // 500)
        ambulances = max(2, expected_attendees // 500)

        return {
            "For" :expected_attendees, 
            "security_staff": security_staff, 
            "nurses": nurses, 
            "ambulances": ambulances
            }
    

