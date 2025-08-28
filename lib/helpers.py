from .event_wizard_db import session
from lib.models.location import Location
from lib.models.event import Event
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
    loc = Location(name=name, capacity=capacity,
                   num_bars=num_bars, num_toilets=num_toilets)
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
        if capacity:
            loc.capacity = int(capacity)
        if num_bars:
            loc.num_bars = int(num_bars)
        if num_toilets:
            loc.num_toilets = int(num_toilets)

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

    location_id = choose_location()
    if not location_id:
        print("No valid location selected. Event not created.")
        return

    location = session.query(Location).get(location_id)

    tickets_sold = int(input("Enter tickets sold: "))

    if tickets_sold > location.capacity:
        print(
            f" Warning: Tickets sold-({tickets_sold}) exceed location capacity-({location.capacity})")

    event = Event(name=name, tickets_sold=tickets_sold,
                  location_id=location_id)

    session.add(event)
    session.commit()
    print(f"Created event: {event}")


def choose_location():
    locations = session.query(Location).all()
    if not locations:
        print("No locations available.")
        return None

    location_choices = ", ".join(
        [f"{loc.id}: {loc.name}" for loc in locations])
    while True:
        try:
            location_id = int(
                input(f"Enter location ID ({location_choices}): "))
            if any(loc.id == location_id for loc in locations):
                return location_id
            else:
                print("Invalid ID. Please choose from the list.")
        except ValueError:
            print("Please enter an available ID number.")


def update_event():
    event_id = int(input("Enter event ID to update: "))
    event = session.get(Event, event_id)
    if event:
        name = input(f"New name ({event.name}): ") or event.name
        tickets_sold = input(f"Tickets sold ({event.tickets_sold}): ")
        location_id = input(f"Location ID ({event.location_id}): ")

        event.name = name
        if tickets_sold:
            event.tickets_sold = int(tickets_sold)
        if location_id:
            event.location_id = int(location_id)

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
        print(
            f"Best selling event: {top_event.name} with {top_event.tickets_sold} tickets sold")
    else:
        print("No events found.")


# SAFETY

def list_safety():
    rules = session.query(Safety).all()
    for r in rules:
        print(r)


def create_safety():
    event_id = int(input("Enter Event ID: "))
    trained_staff = int(input("Enter trained staff count: "))
    ambulances = int(input("Enter number of ambulances: "))
    nurses = int(input("Enter number of nurses: "))
    rule = Safety(event_id=event_id, trained_staff=trained_staff,
                  ambulances=ambulances, nurses=nurses)
    session.add(rule)
    session.commit()
    print(f"Created safety rule: {rule}")


def find_safety_by_event_id():
    event_id = int(input("Enter location ID: "))
    rule = session.query(Safety).filter(Safety.event_id == event_id).first()
    if rule:
        print(rule)
    else:
        print(f"No safety info for location {event_id}")


# SUGGESTIONS

def suggest_location_for_attendees(expected_attendees):
    locations = session.query(Location).order_by(Location.capacity).all()
    for loc in locations:
        if loc.capacity >= expected_attendees:
            return loc
    return None


# def suggest_staff(expected_attendees):
#     security_staff = max(15, expected_attendees // 900)  
#     ambulances = max(1, expected_attendees // 500)     
#     return {"security_staff": security_staff, "ambulances": ambulances}



# EXIT

def exit_program():
    print("Exited Event Wizard. Goodbye!")
    sys.exit()
