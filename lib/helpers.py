from models.location import Location
from models.event import Event
from models.attendee import Attendee


def exit_program():
    print("You Left")
    exit()


def list_locations():
    locations = Location.get_all()
    for location in locations:
        print(location)


def find_location_by_name():
    name = input("Enter the location's name: ")
    location = Location.find_by_name(name)
    print(location) if location else print(
        f'Location {name} not found')


def find_location_by_id():

    id_ = input("Enter the location's id: ")
    try:
        id_ = int(id_)
    except ValueError:
        print("id. must be a number.")
        return

    location = Location.find_by_id(id_)
    print(location) if location else print(f'Location {id_} not found')


def create_location():
    name = input("Enter the location's name: ")
    capacity = input("Enter the department's location: ")
    num_bars = input("How many bars are in this location?")
    num_toilets = input("How many toilets are in this location?")
    try:
        location = Location.create(name, capacity, num_bars, num_toilets)
        print(f'{location} created successfully')
    except Exception as exc:
        print("Error creating location: ", exc)


def update_location():
    id_ = input("Enter the location's id: ")
    if location := Location.find_by_id(id_):
        try:
            name = input("Enter the location's new name: ")
            location.name = name

            capacity = input("Enter the location's new capacity: ")
            location.capacity = int(capacity)

            num_bars = input("Enter the number of bars: ")
            location.num_bars = int(num_bars)

            num_toilets = input("Enter the number of toilets: ")
            location.num_toilets = int(num_toilets)

            location.update()
            print(f'{location} updated succesfully.')
        except Exception as exc:
            print("Error updating location: ", exc)
    else:
        print(f'Location {id_} not found')


def delete_location():
    id_ = input("Enter the location's id: ")
    try:
        id_ = int(id_)
    except ValueError:
        print("id. must be a number.")
        return

    if location := Location.find_by_id(id_):
        location.delete()
        print(f'Location {id_} deleted')
    else:
        print(f'Location {id_} not found')


def list_events():
    events = Event.get_all()
    for event in events:
        print(event)


def find_event_by_name():
    name = input("Enter the event's name: ")
    event = Event.find_by_name(name)
    print(event) if event else print(f'Event {name} not found')


def find_event_by_id():
    id_ = input("Enter the event's id: ")
    try:
        id_ = int(id_)
    except ValueError:
        print("id must be a number.")
        return

    event = Event.find_by_id(id_)
    print(event) if event else print(f'Event {id_} not found')


def create_event():
    name = input("Enter the event's name: ")
    tickets_sold = input("Enter the number of tickets sold: ")
    location_id = input("Enter the location id for this event: ")

    try:
        tickets_sold = int(tickets_sold)
        location_id = int(location_id)
        event = Event.create(name, tickets_sold, location_id)
        print(f'{event} created successfully')
    except Exception as exc:
        print("Error creating event: ", exc)


def update_event():
    id_ = input("Enter the event's id: ")
    try:
        id_ = int(id_)
    except ValueError:
        print("id must be a number.")
        return

    if event := Event.find_by_id(id_):
        try:
            name = input("Enter the event's new name: ")
            event.name = name

            tickets_sold = input("Enter the new number of tickets sold: ")
            event.tickets_sold = int(tickets_sold)

            location_id = input("Enter the new location id: ")
            event.location_id = int(location_id)

            event.update()
            print(f'{event} updated successfully.')
        except Exception as exc:
            print("Error updating event: ", exc)
    else:
        print(f'Event {id_} not found')


def delete_event():
    id_ = input("Enter the event's id: ")
    try:
        id_ = int(id_)
    except ValueError:
        print("id must be a number.")
        return

    if event := Event.find_by_id(id_):
        event.delete()
        print(f'Event {id_} deleted')
    else:
        print(f'Event {id_} not found')

def list_attendees():
    attendees = Attendee.get_all()
    for attendee in attendees:
        print(attendee)




def find_attendee_by_id():
    id_ = input("Enter the attendee's id: ")
    try:
        id_ = int(id_)
    except ValueError:
        print("id must be a number.")
        return

    attendee = Attendee.find_by_id(id_)
    print(attendee) if attendee else print(f'Attendee {id_} not found')


def create_attendee():
    sex = input("Enter attendee's sex (M/F/Other): ")
    ticket_price = input("Enter ticket price: ")
    event_id = input("Enter event id: ")

    try:
        ticket_price = int(ticket_price)
        event_id = int(event_id)
        attendee = Attendee.create(sex, ticket_price, event_id)
        print(f'{attendee} created successfully')
    except Exception as exc:
        print("Error creating attendee: ", exc)


def update_attendee():
    id_ = input("Enter attendee's id: ")
    try:
        id_ = int(id_)
    except ValueError:
        print("id must be a number.")
        return

    if attendee := Attendee.find_by_id(id_):
        try:
            sex = input("Enter attendee's new sex (M/F/Other): ")
            attendee.sex = sex

            ticket_price = input("Enter new ticket price: ")
            attendee.ticket_price = int(ticket_price)

            event_id = input("Enter new event id: ")
            attendee.event_id = int(event_id)

            attendee.update()
            print(f'{attendee} updated successfully.')
        except Exception as exc:
            print("Error updating attendee: ", exc)
    else:
        print(f'Attendee {id_} not found')


def delete_attendee():
    id_ = input("Enter attendee's id: ")
    try:
        id_ = int(id_)
    except ValueError:
        print("id must be a number.")
        return

    if attendee := Attendee.find_by_id(id_):
        attendee.delete()
        print(f'Attendee {id_} deleted')
    else:
        print(f'Attendee {id_} not found')
