import sqlite3
from models.__init__ import CURSOR, CONN

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()


class Location:

    all = {}

    def __init__(self, name, capacity, num_bars=0, num_toilets=0, id=None):
        self.id = id
        self.name = name
        self.capacity = capacity
        self.num_bars = num_bars
        self.num_toilets = num_toilets

    def __repr__(self):
        return (f"<Location {self.name}, capacity={self.capacity}, "
                f"Bars={self.num_bars}, Toilets={self.num_toilets}>")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Please enter a valid location name")
        self._name = value.strip()

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Capacity must be a positive number")
        self._capacity = value

    @property
    def num_bars(self):
        return self._num_bars

    @num_bars.setter
    def num_bars(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Number of bars must be more than 0")
        self._num_bars = value

    @property
    def num_toilets(self):
        return self._num_toilets

    @num_toilets.setter
    def num_toilets(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Number of toilets must be a number more than 0")
        self._num_toilets = value

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS locations (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE,
            capacity INTEGER NOT NULL,
            num_bars INTEGER DEFAULT 0,
            num_toilets INTEGER DEFAULT 0)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS locations;
        """
        CURSOR.execute(sql)
        CONN.commit()

    
    def save(self):
        sql = """
            INSERT INTO locations (name, capacity, num_bars, num_toilets)
            VALUES (?, ?, ?, ?)
         """

        CURSOR.execute(sql, (self.name, self.capacity,
                       self.num_bars, self.num_toilets))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, capacity, num_bars=0, num_toilets=0):
        location = cls(name, capacity, num_bars, num_toilets)
        location.save()
        return location

    def update(self):
        sql = """
            UPDATE locations
            SET name = ?, capacity = ?, num_bars = ?, num_toilets = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.capacity,
                       self.num_bars, self.num_toilets))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM locations
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        location = cls.all.get(row[0])
        if location:
            location.name = row[1]
            location.capacity = row[2]
            location.num_bars = row[3]
            location.num_toilets = row[4]
        else:
            location = cls(row[1], row[2], row[3], row[4])
            location.id = row[0]
            cls.all[location.id] = location
        return location
        

    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM locations
        """

        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_name(cls, name):
        sql = """"
        SELECT *
        FROM locations
        WHERE name is ?
        """
        
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    def events(self):
        from models.event import Event
        sql = """
            SELECT * FROM events
            WHERE location_id = ?
        """

        CURSOR.execute(sql, (self.id,),)

        rows = CURSOR.fetchall()
        return [
            Event.instance_from_db(row) for row in rows
        ]


