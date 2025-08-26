from models.__init__ import CURSOR, CONN
from models.location import Location


class Event:

    all = {}

    def __init__(self, name, tickets_sold, location_id, id=None):
        self.id = id
        self.name = name
        self.tickets_sold = tickets_sold
        self.location_id = location_id

    def __repr__(self):
        return (
            f"<Event {self.id}: {self.name}, {self.tickets_sold} " +
            f"Location ID: , {self.location_id}>"
        )

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError(
                "Name cannot be empty"
            )

    @property
    def tickets_sold(self):
        return self._tickets_sold

    @tickets_sold.setter
    def tickets_sold(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Tickets sold must be a number")
        self._tickets_sold = value

    @classmethod
    def create_table(cls):

        sql = """
            CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY,
            name TEXT,
            tickets_sold INTEGER,
            location_id INTEGER,
            FOREIGN KEY (location_id) REFERENCES locations(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):

        sql = """
            DROP TABLE IF EXISTS events;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):

        sql = """
                INSERT INTO events (name, tickets_sold, location_id)
                VALUES (?, ?, ?)
        """

        CURSOR.execute(sql, (self.name, self.tickets_sold, self.location_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):

        sql = """
            UPDATE events
            SET name = ?, tickets_sold = ?, location_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.job_title,
                             self.location_id, self.id))
        CONN.commit()

    def delete(self):

        sql = """
            DELETE FROM events
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]

        self.id = None

    @classmethod
    def create(cls, name, tickets_sold, location_id):

        event = cls(name, tickets_sold, location_id)
        event.save()
        return event

    @classmethod
    def instance_from_db(cls, row):

        event = cls.all.get(row[0])
        if event:
            event.name = row[1]
            event.ticket_sales = row[2]
            event.location_id = row[3]
        else:
            event = cls(row[1], row[2], row[3])
            event.id = row[0]
            cls.all[event.id] = event
        return event

    @classmethod
    def get_all(cls):

        sql = """
            SELECT *
            FROM events
        """

        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return Employee object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM employees
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM event
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
