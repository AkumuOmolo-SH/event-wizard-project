#!/usr/bin/env python3
from lib.helpers import (
    list_locations, find_location_by_id, find_location_by_name,
    create_location, update_location, delete_location,
    list_events, find_event_by_id, find_event_by_name,
    create_event, update_event, delete_event,
    list_safety, create_safety, update_safety, delete_safety, find_safety_by_event_id,
    suggest_location_for_attendees,
    show_best_selling_event,
    exit_program
)
from lib.models import Event
from lib.event_wizard_db import session


def main_menu():
    print("\n--- Event Wizard CLI ---")
    print("1. Locations")
    print("2. Events")
    print("3. Safety Measures")
    print("4. Quick Actions")
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


def safety_menu():
    print("\n --- Safety Measures Menu ---")
    print("1. List safety measures for all events")
    print("2. New safety measure")
    print("3. Find safety measure by event")
    print("4. Update a safety measure")
    print("5. Delete a safety measure")
    print("0. Back")


def helpers_menu():
    print("\n--- Quick Actions ---")
    print("1. Suggest location for expected attendees")
    print("2. Show attendees per event")
    print("3. Show best-selling event")
    print("0. Back")


def main():
    while True:
        main_menu()
        choice = input("Select a number: ").strip()

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
                    top_event = show_best_selling_event()
                    if top_event:
                        print(
                            f"Best-selling event: {top_event.name} ({top_event.tickets_sold} tickets sold)")
                    else:
                        print("No events found.")
                else:
                    print("Invalid choice")

        elif choice == "3":
            while True:
                safety_menu()
                saf_choice = input("Select:").strip()
                if saf_choice == "0":
                    break
                if saf_choice == "1":
                    list_safety()
                elif saf_choice == "2":
                    create_safety()
                elif saf_choice == "3":
                    find_safety_by_event_id()
                elif saf_choice == "4":
                    update_safety()
                elif saf_choice == "5":
                    delete_safety()
                else:
                    print("Invalid choice")

        elif choice == "4":
            while True:
                helpers_menu()

                help_choice = input("Select:").strip()
                if help_choice == "0":
                    break

                elif help_choice == "1":
                    tickets = input("Enter expected tickets: ")
                    try:
                        tickets = int(tickets)
                        suggested = suggest_location_for_attendees(tickets)
                        if suggested:
                            print(f"Suggested locations: {suggested}")

                        else:
                            print("No suitable location")
                    except ValueError:
                        print("Please enter another number")

                # elif help_choice == "2":

                #     tickets = input("Enter expected tickets sold: ")
                #     try:
                #         tickets = int(tickets)
                #         staff = suggest_staff(tickets)
                #         print(f"Suggested staff: {staff}")
                #     except ValueError:
                #         print("Please enter a valid number")

                elif help_choice == "2":
                    events = session.query(Event).all()
                    if events:
                        for e in events:
                            print(f"{e.name}: {e.tickets_sold} tickets sold")
                    else:
                        print("No events found.")

                elif help_choice == "3":
                    show_best_selling_event()

                else:
                    print("Invalid choice")

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
