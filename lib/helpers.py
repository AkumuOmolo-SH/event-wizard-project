from .event_wizard_db import session
from lib.models.location import Location
from lib.models.event import Event
from lib.models.safety import Safety
import sys
from sqlalchemy import func

# LOCATION


def list_locations():
    locations = session.query(Location).all()
    if locations:
        for loc in locations:
            print(loc)
    else:
        print("No locations found.")


def find_location_by_id():
    try:
        location_id = int(input("Enter location ID: "))
        loc = session.get(Location, location_id)
        if loc:
            print(loc)
        else:
            print(f"Location with id {location_id} not found")
    except ValueError:
        print("Please enter a valid ID")


def find_location_by_name():
    name = input("Enter location name: ").strip()
    if not name:
        print("Name cannot be empty")
        return
    loc = session.query(Location).filter(Location.name == name).first()
    if loc:
        print(loc)
    else:
        print(f"Location '{name}' not found")


def create_location():
    name = input("Enter location name: ").strip()
    if not name:
        print("Location name cannot be empty.")
        return
    try:
        capacity = int(input("Enter location capacity: "))
        num_bars = int(input("Enter number of bars (default 0): ") or 0)
        num_toilets = int(input("Enter number of toilets (default 0): ") or 0)
    except ValueError:
        print("Please enter valid numbers.")
        return
    loc = Location(name=name, capacity=capacity,
                   num_bars=num_bars, num_toilets=num_toilets)
    session.add(loc)
    session.commit()
    print(f"Created location: {loc}")


def update_location():
    try:

        location_id = int(input("Enter location ID to update: "))
    except ValueError:
        print("Please enter valid numbers.")
        return
    loc = session.get(Location, location_id)
    if not loc:
        print(f"Location {location_id} not found.")
        return

    name = input(f"New name ({loc.name}): ") or loc.name
    capacity = input(f"New capacity ({loc.capacity}): ")
    num_bars = input(f"Number of bars ({loc.num_bars}): ")
    num_toilets = input(f"Number of toilets ({loc.num_toilets}): ")

    loc.name = name
    if capacity:
        try:
            loc.capacity = int(capacity)
        except ValueError:
            print("Invalid capacity. Keeping previous value.")
    if num_bars:
        loc.num_bars = int(num_bars)
    if num_toilets:
        try:
            loc.num_toilets = int(num_toilets)
        except ValueError:
            print("Invalid number of toilets. Keeping previous value.")

        session.commit()
        print(f"Updated location: {loc}")
    # else:
    #     print(f"Location {location_id} not found")


def delete_location():
    try:
        location_id = int(input("Enter location ID to delete: "))
    except ValueError:
        print("Please enter a valid number.")
        return
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
    if events:
        for event in events:
            print(event)
    else:
        print("No events found.")


def find_event_by_id():
    try:
        event_id = int(input("Enter event ID: "))
        event = session.get(Event, event_id)
        if event:
            print(event)
        else:
            print(f"Event {event_id} not found")
    except ValueError:
        print("Please enter a valid ID number.")


def find_event_by_name():
    name = input("Enter event name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    event = session.query(Event).filter(Event.name == name).first()
    if event:
        print(event)
    else:
        print(f"Event '{name}' not found.")


def create_event():
    name = input("Enter event name: ").strip()
    if not name:
        print("Event name cannot be empty.")
        return

    location_id = choose_location()
    if not location_id:
        print("No valid location selected. Event not created.")
        return

    location = session.query(Location).get(location_id)

    try:

        tickets_sold = int(input("Enter tickets sold: "))
    except ValueError:
        print("Invalid number of tickets.")

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
    try:
        event_id = int(input("Enter event ID to update: "))
    except ValueError:
        print("Please enter a valid number.")
        return
    event = session.get(Event, event_id)
    if not event:
        print(f"Event {event_id} not found.")
        return

    name = input(f"New name ({event.name}): ") or event.name
    tickets_sold = input(f"Tickets sold ({event.tickets_sold}): ")
    location_id = input(f"Location ID ({event.location_id}): ")

    event.name = name
    if tickets_sold:
        try:
            tickets = int(tickets_sold)
            event.tickets_sold = tickets_sold
        except ValueError:
            print("Invalid tickets sold. Keeping previous value.")
    if location_id:
        try:
            loc_id = int(location_id)
            event.location_id = loc_id
        except ValueError:
            print("Invalid location ID sold. Keeping previous value.")

    session.commit()
    print(f"Updated event: {event}")


def delete_event():
    try:
        event_id = int(input("Enter event ID to delete: "))
    except ValueError:
        print("Please enter a valid number.")
        return

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
    if rules:
        for r in rules:
            print(r)
    else:
        print("No safety info found.")


def create_safety():
    try:
        event_id = int(input("Enter Event ID: "))
        security_staff = int(input("Enter staff count: "))
        ambulances = int(input("Enter number of ambulances: "))
        nurses = int(input("Enter number of nurses: "))
    except ValueError:
        print("Please enter valid numbers.")
        return
    rule = Safety(event_id=event_id, security_staff=security_staff,
                  ambulances=ambulances, nurses=nurses)
    session.add(rule)
    session.commit()
    print(f"Created safety rule: {rule}")


def update_safety():
    try:
        event_id = int(input("Enter event ID to update safety info: "))
    except ValueError:
        print("Please enter a valid number.")
        return
    rule = session.query(Safety).filter(Safety.event_id == event_id).first()
    if not rule:
        print(f"No safety info for event ID{event_id}")
        return

    print(f"Current safety info: {rule}")
    security_staff = input(
        f"Enter new security staff count (current {rule.security_staff}): ")
    ambulances = input(
        f"Enter new ambulances count (current {rule.ambulances}): ")
    nurses = input(f"Enter new nurses count (current {rule.nurses}): ")

    if security_staff:
        try:
            rule.security_staff = int(security_staff)
        except ValueError:
            print("Invalid input. Keeping previous value.")
    if ambulances:
        try:
            rule.ambulances = int(ambulances)
        except ValueError:
            print("Invalid input. Keeping previous value.")
    if nurses:
        try:
            rule.nurses = int(nurses)
        except ValueError:
            print("Invalid input. Keeping previous value.")

    session.commit()
    print(f"Updated safety info: {rule}")


def delete_safety():
    try:
        event_id = int(input("Enter event ID to delete: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    rule = session.query(Safety).filter(Safety.event_id == event_id).first()
    if rule:
        session.delete(rule)
        session.commit()
        print(f"Deleted safety info for event ID:{event_id}")
    else:
        print(f"No safety info found for event {event_id}")


def find_safety_by_event_id():
    try:
        event_id = int(input("Enter event ID: "))
    except ValueError:
        print("Please enter a valid number.")
        return
    rule = session.query(Safety).filter(Safety.event_id == event_id).first()
    if rule:
        print(rule)
    else:
        print(f"No safety info for event {event_id}")


# SUGGESTIONS/QUICK ACTIONS

def suggest_location_for_attendees(expected_attendees):
    locations = session.query(Location).order_by(Location.capacity).all()
    for loc in locations:
        if loc.capacity >= expected_attendees:
            return loc
    return None


# EXIT

def exit_program():
    print("Exited Event Wizard. Goodbye!")
    sys.exit()
