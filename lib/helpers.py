
from .event_wizard_db import session
from lib.models.location import Location
from lib.models.event import Event
from lib.models.attendee import Attendee
from lib.models.safety import Safety
import sys
from sqlalchemy import func

# LOCATION 

def list_locations():
    locations = session.query(Location).all()
    for loc in locations:
        print(loc)


def find_location_by_id():
    location_id = input("Enter location ID: ")
    loc = session.get(Location, int(location_id))
    if loc:
        print(loc)
    else:
        print(f"Location with id {location_id} not found")


def find_location_by_name():
    name = input("Enter location name: ")
    loc = session.query(Location).filter(Location.name == name).first()
    if loc:
        print(loc)
    else:
        print(f"Location '{name}' not found")


def create_location():
    name = input("Enter location name: ")
    capacity = int(input("Enter location capacity: "))
    num_bars = int(input("Enter number of bars (default 0): ") or 0)
    num_toilets = int(input("Enter number of toilets (default 0): ") or 0)
    loc = Location(name=name, capacity=capacity, num_bars=num_bars, num_toilets=num_toilets)
    session.add(loc)
    session.commit()
    print(f"Created location: {loc}")


def update_location():
    location_id = int(input("Enter location ID to update: "))
    loc = session.get(Location, location_id)
    if loc:
        name = input(f"New name ({loc.name}): ") or loc.name
        capacity = input(f"New capacity ({loc.capacity}): ")
        num_bars = input(f"Number of bars ({loc.num_bars}): ")
        num_toilets = input(f"Number of toilets ({loc.num_toilets}): ")

        loc.name = name
        if capacity: loc.capacity = int(capacity)
        if num_bars: loc.num_bars = int(num_bars)
        if num_toilets: loc.num_toilets = int(num_toilets)

        session.commit()
        print(f"Updated location: {loc}")
    else:
        print(f"Location {location_id} not found")


def delete_location():
    location_id = int(input("Enter location ID to delete: "))
    loc = session.get(Location, location_id)
    if loc:
        session.delete(loc)
        session.commit()
        print(f"Deleted location {location_id}")
    else:
        print(f"Location {location_id} not found")


# EVENT 

def list_events():
    events = session.query(Event).all()
    for event in events:
        print(event)


def find_event_by_id():
    event_id = int(input("Enter event ID: "))
    event = session.get(Event, event_id)
    if event:
        print(event)
    else:
        print(f"Event {event_id} not found")


def find_event_by_name():
    name = input("Enter event name: ")
    event = session.query(Event).filter(Event.name == name).first()
    if event:
        print(event)
    else:
        print(f"Event '{name}' not found")


def create_event():
    name = input("Enter event name: ")
    tickets_sold = int(input("Enter tickets sold: "))
    location_id = int(input("Enter location ID: "))
    event = Event(name=name, tickets_sold=tickets_sold, location_id=location_id)
    session.add(event)
    session.commit()
    print(f"Created event: {event}")


def update_event():
    event_id = int(input("Enter event ID to update: "))
    event = session.get(Event, event_id)
    if event:
        name = input(f"New name ({event.name}): ") or event.name
        tickets_sold = input(f"Tickets sold ({event.tickets_sold}): ")
        location_id = input(f"Location ID ({event.location_id}): ")

        event.name = name
        if tickets_sold: event.tickets_sold = int(tickets_sold)
        if location_id: event.location_id = int(location_id)

        session.commit()
        print(f"Updated event: {event}")
    else:
        print(f"Event {event_id} not found")


def delete_event():
    event_id = int(input("Enter event ID to delete: "))
    event = session.get(Event, event_id)
    if event:
        session.delete(event)
        session.commit()
        print(f"Deleted event {event_id}")
    else:
        print(f"Event {event_id} not found")


def show_best_selling_event():
    top_event = Event.best_selling_event()
    if top_event:
        print(f"Best selling event: {top_event.name} with {top_event.tickets_sold} tickets sold")
    else:
        print("No events found.")


#  ATTENDEE 

def list_attendees():
    attendees = session.query(Attendee).all()
    for a in attendees:
        print(a)


def find_attendee_by_id():
    attendee_id = int(input("Enter attendee ID: "))
    a = session.get(Attendee, attendee_id)
    if a:
        print(a)
    else:
        print(f"Attendee {attendee_id} not found")


def find_attendees_by_sex():
    sex = input("Enter sex (M/F): ")
    attendees = session.query(Attendee).filter(Attendee.sex == sex).all()
    if attendees:
        for a in attendees:
            print(a)
    else:
        print(f"No attendees with sex '{sex}' found")


def create_attendee():
    sex = input("Enter sex (M/F): ")
    ticket_price = float(input("Enter ticket price: "))
    event_id = int(input("Enter event ID: "))
    attendee = Attendee(sex=sex, ticket_price=ticket_price, event_id=event_id)
    session.add(attendee)
    session.commit()
    print(f"Created attendee: {attendee}")


def update_attendee():
    attendee_id = int(input("Enter attendee ID to update: "))
    a = session.get(Attendee, attendee_id)
    if a:
        sex = input(f"New sex ({a.sex}): ") or a.sex
        ticket_price = input(f"Ticket price ({a.ticket_price}): ")
        event_id = input(f"Event ID ({a.event_id}): ")

        a.sex = sex
        if ticket_price: a.ticket_price = float(ticket_price)
        if event_id: a.event_id = int(event_id)

        session.commit()
        print(f"Updated attendee: {a}")
    else:
        print(f"Attendee {attendee_id} not found")


def delete_attendee():
    attendee_id = int(input("Enter attendee ID to delete: "))
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


def create_safety():
    location_id = int(input("Enter location ID: "))
    trained_staff = int(input("Enter trained staff count: "))
    ambulances = int(input("Enter number of ambulances: "))
    nurses = int(input("Enter number of nurses: "))
    rule = Safety(location_id=location_id, trained_staff=trained_staff, ambulances=ambulances, nurses=nurses)
    session.add(rule)
    session.commit()
    print(f"Created safety rule: {rule}")


def find_safety_by_location():
    location_id = int(input("Enter location ID: "))
    rule = session.query(Safety).filter(Safety.location_id == location_id).first()
    if rule:
        print(rule)
    else:
        print(f"No safety info for location {location_id}")

def get_safety_for_event(event_id):
    rules = session.query(Safety).filter(Safety.event_id == event_id).all()
    if rules:
        for r in rules:
            print(r)
    else:
        print(f"No safety info for event {event_id}")



# SUGGESTIONS

def suggest_location_and_safety():
    capacity = int(input("Enter expected attendees: "))
    suitable_locations = [loc for loc in session.query(Location).all() if loc.capacity >= capacity]

    if not suitable_locations:
        print("No location can handle this capacity.")
        return

    suggested_location = suitable_locations[0]
    security_staff = max(25, capacity // 200)
    ambulances = max(5, capacity // 500)

    print(f"Suggested location: {suggested_location.name}")
    print(f"Required security staff: {security_staff}")
    print(f"Required ambulances: {ambulances}")


# EXIT 

def exit_program():
    print("Exited Event Wizard. Goodbye!")
    sys.exit()

