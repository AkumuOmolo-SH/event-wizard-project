from event_wizard_db import session
from db import session
from models.location import Location
from models.event import Event
from models.attendee import Attendee
from models.safety import Safety

#  LOCATION 

def list_locations():
    locations = session.query(Location).all()
    for loc in locations:
        print(loc)

def find_location_by_id(location_id):
    loc = session.get(Location, location_id)
    if loc:
        print(loc)
    else:
        print(f"Location with id {location_id} not found")

def find_location_by_name(name):
    loc = session.query(Location).filter(Location.name == name).first()
    if loc:
        print(loc)
    else:
        print(f"Location '{name}' not found")

def create_location(name, capacity, num_bars=0, num_toilets=0):
    loc = Location(name=name, capacity=capacity, num_bars=num_bars, num_toilets=num_toilets)
    session.add(loc)
    session.commit()
    print(f"Created location: {loc}")

def update_location(location_id, **kwargs):
    loc = session.get(Location, location_id)
    if loc:
        for key, value in kwargs.items():
            setattr(loc, key, value)
        session.commit()
        print(f"Updated location: {loc}")
    else:
        print(f"Location {location_id} not found")

def delete_location(location_id):
    loc = session.get(Location, location_id)
    if loc:
        session.delete(loc)
        session.commit()
        print(f"Deleted location {location_id}")
    else:
        print(f"Location {location_id} not found")


# EVENT HELPERS

def list_events():
    events = session.query(Event).all()
    for event in events:
        print(event)

def find_event_by_id(event_id):
    event = session.get(Event, event_id)
    if event:
        print(event)
    else:
        print(f"Event {event_id} not found")

def create_event(name, tickets_sold, location_id):
    event = Event(name=name, tickets_sold=tickets_sold, location_id=location_id)
    session.add(event)
    session.commit()
    print(f"Created event: {event}")

def update_event(event_id, **kwargs):
    event = session.get(Event, event_id)
    if event:
        for key, value in kwargs.items():
            setattr(event, key, value)
        session.commit()
        print(f"Updated event: {event}")
    else:
        print(f"Event {event_id} not found")

def delete_event(event_id):
    event = session.get(Event, event_id)
    if event:
        session.delete(event)
        session.commit()
        print(f"Deleted event {event_id}")
    else:
        print(f"Event {event_id} not found")


#ATTENDEE

def list_attendees():
    attendees = session.query(Attendee).all()
    for a in attendees:
        print(a)

def find_attendee_by_id(attendee_id):
    a = session.get(Attendee, attendee_id)
    if a:
        print(a)
    else:
        print(f"Attendee {attendee_id} not found")

def find_attendees_by_sex(sex):
    attendees = session.query(Attendee).filter(Attendee.sex == sex).all()
    if attendees:
        for a in attendees:
            print(a)
    else:
        print(f"No attendees with sex '{sex}' found")

def create_attendee(sex, ticket_price, event_id):
    attendee = Attendee(sex=sex, ticket_price=ticket_price, event_id=event_id)
    session.add(attendee)
    session.commit()
    print(f"Created attendee: {attendee}")

def update_attendee(attendee_id, **kwargs):
    a = session.get(Attendee, attendee_id)
    if a:
        for key, value in kwargs.items():
            setattr(a, key, value)
        session.commit()
        print(f"Updated attendee: {a}")
    else:
        print(f"Attendee {attendee_id} not found")

def delete_attendee(attendee_id):
    a = session.get(Attendee, attendee_id)
    if a:
        session.delete(a)
        session.commit()
        print(f"Deleted attendee {attendee_id}")
    else:
        print(f"Attendee {attendee_id} not found")


# SAFETY

def list_safety():
    rules = session.query(Safety).all()
    for r in rules:
        print(r)

def create_safety(location_id, trained_staff, ambulances, nurses):
    rule = Safety(location_id=location_id, trained_staff=trained_staff,
                  ambulances=ambulances, nurses=nurses)
    session.add(rule)
    session.commit()
    print(f"Created safety rule: {rule}")

def find_safety_by_location(location_id):
    rule = session.query(Safety).filter(Safety.location_id == location_id).first()
    if rule:
        print(rule)
    else:
        print(f"No safety info for location {location_id}")
