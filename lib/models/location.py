from sqlalchemy import create_engine, Column, Integer, String
from __init__ import Base
from sqlalchemy.orm import sessionmaker, validates

Base = declarative_base()

engine = create_engine('sqlite:///:memory:', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

class Location(Base):
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    capacity = Column(Integer, nullable=False)
    num_bars = Column(Integer, default=0)
    num_toilets = Column(Integer, default=0)

    # def __init__(self, name, capacity, num_bars, num_toilets, id=None):
    #     self.id = id
    #     self.name = name
    #     self.capacity = capacity
    #     self.num_bars = num_bars
    #     self.num_toilets = num_toilets

    def __repr__(self):
        return f"<Location {self.name}, capacity={self.capacity}, Bars={self.num_bars}, Toilets={self.num_toilets}>"
    

    @validates("num_bars", "num_toilets")
    def validate_numbers(self, key, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError(f"{key} must be an integer")
        return value


    @validates("capacity")
    def validate_capacity(self, key, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Capacity must be a positive integer")
        return value

    @validates
    def validate_name(self, ket, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Please enter a location name")
        return value

    @classmethod
    def create(cls, session, name, capacity, num_bars=0, num_toilets=0):
        location = cls(
            name=name,
            capacity=capacity,
            num_bars=num_bars,
            num_toilets=num_toilets

        )
        session.add(location)
        session.commit()
        return location
    
    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()
    
    @classmethod
    def find_by_id(cls, session, location_id):
        return session.get(cls, location_id)

    def delete(self, session):
        session.delete(self)
        session.commit()

    # creates the location table
Base.metadata.create_all(engine) 



    