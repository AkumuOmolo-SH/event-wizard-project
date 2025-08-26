#!/usr/bin/env python3

import sqlite3
from models.attendee import Attendee
from models.event import Event
from models.location import Location
from models.__init__ import CONN, CURSOR


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

    concert = Event.create("AfroBeats Festival", 20, alchemist.id)
    match = Event.create("Championship Final", 35, living_rooms.id)
    dance = Event.create("Salsa class", 55, geco.id)

    Attendee.create("M", 2000, concert.id)
    Attendee.create("F", 2000, concert.id)
    Attendee.create("M", 1500, match.id)
    Attendee.create("Other", 1000, dance.id)
    Attendee.create("F", 2000, concert.id)
    Attendee.create("M", 2000, concert.id)
    Attendee.create("M", 1500, match.id)
    Attendee.create("Other", 1000, dance.id)


seed_database()
print("Seeded database")
