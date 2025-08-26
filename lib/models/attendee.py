from models.__init__ import CURSOR, CONN
from models.event import Event

class Attendee:
    all={}

    def __init__(self, sex, ticket_price, event_id, id=None):
        self.id = id
        self.sex = sex
        self.ticket_price = ticket_price
        self.event_id = event_id

    def __repr__(self):
        return(
            f"<Attendee {self.id}: {self.sex}," +
            f"Event ID: {self.event_id}>"
        )
    
    @property
    def sex(self):
        return self._sex
    
    @sex.setter
    def sex(self, value):
        if isinstance(value, str) and value in ("M","F","Other"):
            self._sex = value

        else:
            raise ValueError(
                "Sex must be 'M', 'F' or 'Other'"
            )
        
    @property
    def ticket_price(self):
        return self._ticket_price
    
    @ticket_price.setter
    def ticket_price(self, value):
        if not isinstance(value, int) or value <=0:
            raise ValueError("Ticket price must be a positive number")
        self._ticket_price = value
        
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS attendees (
            id INTEGER PRIMARY KEY,
            sex TEXT,
            ticket_price INTEGER,
            event_id INTEGER,
            FOREIGN KEY (event_id) REFERENCES events(id)
            )
            
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):

        sql = """
            DROP TABLE IF EXISTS attendee;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
                INSERT INTO attendees (sex, ticket_price, event_id)
                VALUES (?, ?, ?)
        """

        CURSOR.execute(sql, (self.sex, self.ticket_price, self.event_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        
        sql = """
            UPDATE attendees
            SET sex = ?, ticket_price = ?, event_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.sex, self.ticket_price,
                             self.event_id, self.id))
        CONN.commit()

    def delete(self):
 
        sql = """
            DELETE FROM attendees
            WHERE id = ?
        """   

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None

    @classmethod
    def create(cls, sex, ticket_price, event_id):
        attendee = cls(sex, ticket_price, event_id)
        attendee.save()
        return attendee       

    @classmethod
    def instance_from_db(cls, row):
  
        attendee = cls.all.get(row[0])
        if attendee:        
            attendee.sex = row[1]
            attendee.ticket_price = row[2]
            attendee.event_id = row[3]
        else:
           
            attendee = cls(row[1], row[2], row[3])
            attendee.id = row[0]
            cls.all[attendee.id] = attendee
        return attendee

    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM attendees
        
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]        

    @classmethod
    def find_by_id(cls, id):
        row = CURSOR.execute(
            "SELECT id, event_id, sex, ticket_price FROM attendees WHERE id=?",
            (id,)
        ).fetchone()
        return cls(id=row[0], sex=row[1], ticket_price=row[2], event_id=row[3]) if row else None
    
    @classmethod
    def find_by_sex(cls, sex):
        sql = """SELECT * FROM attendees WHERE sex = ?"""
        rows = CURSOR.execute(sql, (sex,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]



