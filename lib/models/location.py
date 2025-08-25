from sqlalchemy import Column, Integer, String
from models import Base


class Location(Base):
    __tablename__="locations"

    id = Column(Integer, primary_key=True)
    name=Column(String, nullable=False, unique=True)
    capacity=Column(Integer, nullable=False)
    num_bars=Column(Integer, default=0)
    num_toilets=Column(Integer, default=0)

    all = {}

    def __init__(self, name, capacity, num_bars, num_toilets, id=None):
        self.id = id
        self.name = name
        self.capacity=capacity
        self.num_bars=num_bars
        self.num_toilets=num_toilets

    def __repr__(self):
        return f"<Location {self.name}, capacity={self.capacity}, Bars={self.num_bars}, Toilets={self.num_toilets}>"
    


    
        