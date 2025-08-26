#!/usr/bin/env python3
from models.attendee import Attendee
from models.event import Event
from models.location import Location
from models.__init__ import CONN, CURSOR
import sqlite3

conn = sqlite3.connect("events_wiz.db")
cursor = conn.cursor()


def seed_database():
    Attendee.drop_table()
    Event.drop_table()
    Location.drop_table()

    Location.create_table()
    Event.create_table()
    Attendee.create_table()

    alchemist = Location.create("Alchemist", 500, 5, 3)
    geco = Location.create("Geco", 350, 4, 4)
    living_rooms = Location.create("Living Rooms", 200, 2, 1)

    concert = Event.create("AfroBeats Festival", "20", alchemist.id)
    match = Event.create("Championship Final", "35", living_rooms.id)
    dance = Event.create("Salsa class", "55", geco.id)

    Attendee.create("M", concert.id, 2000.0)
    Attendee.create("F", concert.id, 2000.0)
    Attendee.create("M", match.id, 1500.0)
    Attendee.create("Other", dance.id, 1000.0)
    Attendee.create("F", concert.id, 2000.0)
    Attendee.create("M", concert.id, 2000.0)
    Attendee.create("M", match.id, 1500.0)
    Attendee.create("Other", dance.id, 1000.0)


seed_database()
print("Seeded database")
