#!/usr/bin/env python3
from lib.helpers import (
    list_locations, find_location_by_id, find_location_by_name,
    create_location, update_location, delete_location,
    list_events, find_event_by_id, find_event_by_name,
    create_event, update_event, delete_event,
    list_attendees, find_attendee_by_id,
    create_attendee, update_attendee, delete_attendee,
    suggest_location_and_safety, 
    # suggest_staff, 
    # best_selling_event,
    # attendees_per_event,
    #  get_safety_for_event, 
    exit_program
)


def main_menu():
    print("\n--- Event Wizard CLI ---")
    print("1. Locations")
    print("2. Events")
    print("3. Attendees")
    print("4. Helpers / Suggestions")
    print("0. Exit")


def location_menu():
    print("\n--- Locations Menu ---")
    print("1. List all locations")
    print("2. Find location by name")
    print("3. Find location by ID")
    print("4. Create a location")
    print("5. Update a location")
    print("6. Delete a location")
    print("0. Back")


def event_menu():
    print("\n--- Events Menu ---")
    print("1. List all events")
    print("2. Find event by name")
    print("3. Find event by ID")
    print("4. Create an event")
    print("5. Update an event")
    print("6. Delete an event")
    print("7. Show best-selling event")
    print("0. Back")


def attendee_menu():
    print("\n--- Attendees Menu ---")
    print("1. List all attendees")
    print("2. Find attendee by ID")
    print("3. Create an attendee")
    print("4. Update an attendee")
    print("5. Delete an attendee")
    print("0. Back")


def helpers_menu():
    print("\n--- Quick Suggestions ---")
    print("1. Suggest location for expected attendees")
    print("2. Suggest staff for expected attendees")
    print("3. Show attendees per event")
    print("0. Back")


def main():
    while True:
        main_menu()
        choice = input("> ").strip()

        if choice == "0":
            exit_program()

        elif choice == "1":
            while True:
                location_menu()
                loc_choice = input("> ").strip()
                if loc_choice == "0":
                    break
                elif loc_choice == "1":
                    list_locations()
                elif loc_choice == "2":
                    find_location_by_name()
                elif loc_choice == "3":
                    find_location_by_id()
                elif loc_choice == "4":
                    create_location()
                elif loc_choice == "5":
                    update_location()
                elif loc_choice == "6":
                    delete_location()
                else:
                    print("Invalid choice")

        elif choice == "2":
            while True:
                event_menu()
                ev_choice = input("> ").strip()
                if ev_choice == "0":
                    break
                elif ev_choice == "1":
                    list_events()
                elif ev_choice == "2":
                    find_event_by_name()
                elif ev_choice == "3":
                    find_event_by_id()
                elif ev_choice == "4":
                    create_event()
                elif ev_choice == "5":
                    update_event()
                elif ev_choice == "6":
                    delete_event()
                elif ev_choice == "7":
                    top_event = best_selling_event()
                    if top_event:
                        print(f"Best-selling event: {top_event.name} ({top_event.tickets_sold} tickets sold)")
                    else:
                        print("No events found.")
                else:
                    print("Invalid choice")

        elif choice == "3":
            while True:
                attendee_menu()
                att_choice = input("> ").strip()
                if att_choice == "0":
                    break
                elif att_choice == "1":
                    list_attendees()
                elif att_choice == "2":
                    find_attendee_by_id()
                elif att_choice == "3":
                    create_attendee()
                elif att_choice == "4":
                    update_attendee()
                elif att_choice == "5":
                    delete_attendee()
                else:
                    print("Invalid choice")

        elif choice == "4":
            while True:
                helpers_menu()
                help_choice = input("> ").strip()
                if help_choice == "0":
                    break
                elif help_choice == "1":
                    attendees = input("Enter expected number of attendees: ")
                    try:
                        attendees = int(attendees)
                        suggested = suggest_location(attendees)
                        print(f"Suggested locations: {suggested}")
                    except ValueError:
                        print("Please enter a valid number")
                elif help_choice == "2":
                    attendees = input("Enter expected number of attendees: ")
                    try:
                        attendees = int(attendees)
                        staff = suggest_staff(attendees)
                        print(f"Suggested staff: {staff}")
                    except ValueError:
                        print("Please enter a valid number")
                elif help_choice == "3":
                    attendees_per_event()
                else:
                    print("Invalid choice")

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
