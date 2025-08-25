from sqlalchemy import Column, Integer, String
from __init__ import Base


class Location(Base):
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    capacity = Column(Integer, nullable=False)
    num_bars = Column(Integer, default=0)
    num_toilets = Column(Integer, default=0)

    def __init__(self, name, capacity, num_bars, num_toilets, id=None):
        self.id = id
        self.name = name
        self.capacity = capacity
        self.num_bars = num_bars
        self.num_toilets = num_toilets

    def __repr__(self):
        return f"<Location {self.name}, capacity={self.capacity}, Bars={self.num_bars}, Toilets={self.num_toilets}>"

    @property
    def num_bars(self):
        return self._num_bars

    @num_bars.setter
    def numbars(self, value):
        if not isinstance(value, int):
            raise ValueError("Number of bars must be an integer")
        self.num_bars = value

    @property
    def num_toilets(self):
        return self._num_toilets

    @num_toilets.setter
    def num_toilets(self, value):
        if not isinstance(value, int):
            raise ValueError("Number of toilets must be an integer")
        self.num_toilets = value

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        if not isinstance(value, int):
            raise ValueError("Capacity must be a number")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            return self._name = name
        else:
            raise ValueError("Please enter a location")

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

    def delete(self):
        session.delete(self)
        session.commit()

    