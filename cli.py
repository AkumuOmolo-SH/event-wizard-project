#!/usr/bin/env python
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
from lib.event_wizard_db import session
from lib.models.event import Event
from tabulate import tabulate

RESET = "\033[0m"
CYAN = "\033[36m"


def main_menu():
    title = "EVENT WIZARD"
    print("\n" + "=" * len(title))
    print(title)
    print("=" * len(title) + "\n")

    print("Welcome to Event Wizard. Your go to platform for organizing, analyzing and managing events.")
    print("Let's get started!")

    print("\n===== Navigation Instructions =====")
    print("Use the numbers in the menu to select an option. Press enter to confirm.")
    print("To cancel an action, leave the input empty and press Enter.")
    print("\n")

    menu_title = "MAIN MENU"
    print(menu_title)
    print("-" * len(menu_title) + "\n")

    print(f"{CYAN}1. Locations")
    print("2. Events")
    print("3. Safety")
    print("4. Quick Actions")
    print("0. Exit" + RESET)


def location_menu():
    print(f"{CYAN}\n--- Locations Menu ---")
    print("1. List all locations")
    print("2. Find location by name")
    print("3. Find location by ID")
    print("4. Create a location")
    print("5. Update a location")
    print("6. Delete a location")
    print("0. Back to main menu" + RESET)


def event_menu():
    print(f"{CYAN}\n--- Events Menu ---")
    print("1. List all events")
    print("2. Find event by name")
    print("3. Find event by ID")
    print("4. Create an event")
    print("5. Update an event")
    print("6. Delete an event")
    print("7. Show best-selling event")
    print("0. Back to main menu" + RESET)


def safety_menu():
    print(f"{CYAN}\n--- Safety Measures Menu ---")
    print("1. List safety measures for all events")
    print("2. Create new safety measure")
    print("3. Update safety measure")
    print("4. Delete safety measure")
    print("5. Find safety measure by event")
    print("0. Back to main menu" + RESET)


def helpers_menu():
    print(f"{CYAN}\n--- Quick Actions ---")
    print("1. Suggest location for expected attendees")
    print("2. Show attendees per event")
    print("0. Back to main menu" + RESET)


def pause():
    input("\nPress Enter to return to the main menu")


def main():
    while True:
        main_menu()
        choice = input("Select a number: ").strip()

        if choice == "0":
            exit_program()

        elif choice == "1":  # Location
            while True:
                location_menu()
                loc_choice = input("Enter number from menu... ").strip()
                if loc_choice == "0":
                    break
                elif loc_choice == "1":
                    list_locations()
                    pause()
                elif loc_choice == "2":
                    find_location_by_name()
                    pause()
                elif loc_choice == "3":
                    find_location_by_id()
                    pause()
                elif loc_choice == "4":
                    create_location()
                    pause()
                elif loc_choice == "5":
                    update_location()
                    pause()
                elif loc_choice == "6":
                    delete_location()
                    pause()
                else:
                    print("Invalid choice")

        elif choice == "2":  # Events
            while True:
                event_menu()
                ev_choice = input("Enter number from menu... ").strip()
                if ev_choice == "0":
                    break
                elif ev_choice == "1":
                    list_events()
                    pause()
                elif ev_choice == "2":
                    find_event_by_name()
                    pause()
                elif ev_choice == "3":
                    find_event_by_id()
                    pause()
                elif ev_choice == "4":
                    create_event()
                    pause()
                elif ev_choice == "5":
                    update_event()
                    pause()
                elif ev_choice == "6":
                    delete_event()
                    pause()
                elif ev_choice == "7":
                    show_best_selling_event()
                    pause()
                else:
                    print("Invalid choice")

        elif choice == "3":  # Safety
            while True:
                safety_menu()
                saf_choice = input("Enter number from menu... ").strip()
                if saf_choice == "0":
                    break
                elif saf_choice == "1":
                    list_safety()
                    pause()
                elif saf_choice == "2":
                    create_safety()
                    pause()
                elif saf_choice == "3":
                    update_safety()
                    pause()
                elif saf_choice == "4":
                    delete_safety()
                    pause()
                elif saf_choice == "5":
                    find_safety_by_event_id()
                    pause()
                else:
                    print("Invalid choice")

        elif choice == "4":  # Helpers
            while True:
                helpers_menu()
                help_choice = input("Enter number from menu... ").strip()
                if help_choice == "0":
                    break
                elif help_choice == "1":
                    tickets = input("Enter expected tickets: ")
                    try:
                        tickets = int(tickets)
                        loc = suggest_location_for_attendees(tickets)
                        if loc:
                            print(f"Suggested location:")
                            print(tabulate([(loc.id, loc.name, loc.capacity, loc.num_bars, loc.num_toilets)], headers=("ID", "Name", "Capacity", "Bars", "Toilets"), tablefmt="fancy_grid"
                                           ))
                        else:
                            print(
                                "No location can accommodate this number of attendees.")
                    except ValueError:
                        print("Please enter a valid number")
                    pause()

                elif help_choice == "2":
                    events = session.query(Event).all()
                    if events:
                        table = [(e.name, e.tickets_sold) for e in events]
                        print(tabulate(table, headers=("Event Name",
                              "Tickets Sold"), tablefmt="fancy_grid"))
                    else:
                        print("No events found.")
                    pause()
                else:
                    print("Invalid choice")


if __name__ == "__main__":
    main()
