
from helpers import (
    exit_program,
    list_locations,
    find_location_by_id,
    find_location_by_name,
    update_location,
    delete_location,
    create_location,
    list_events,
    find_event_by_id,
    find_event_by_name,
    update_event,
    delete_event,
    create_event,
    list_attendees,
    find_attendee_by_id,
    update_attendee,
    delete_attendee,
    create_attendee,
    
    
)

def main():
    while True:
        menu()
        choice = input("> ")
        
        # Exit
        if choice == "0":
            exit_program()

        # Locations
        elif choice == "1":
            list_locations()
        elif choice == "2":
            find_location_by_name()
        elif choice == "3":
            find_location_by_id()
        elif choice == "4":
            create_location()
        elif choice == "5":
            update_location()
        elif choice == "6":
            delete_location()
        elif choice == "7":
            list_events()
        elif choice == "8":
            find_event_by_name()
        elif choice == "9":
            find_event_by_id()
        elif choice == "10":
            create_event()
        elif choice == "11":
            update_event()
        elif choice == "12":
            delete_event()
        elif choice == "13":
            list_attendees()
        elif choice == "14":
            find_attendee_by_id()
        elif choice == "15":
            create_attendee()
        elif choice == "16":
            update_attendee()
        elif choice == "17":
            delete_attendee()
        else:
            print("Invalid choice")


def menu():
    print("\nPlease select an option:")
    print("0. Exit the program")
    print("1. List all locations")
    print("2. Find location by name")
    print("3. Find location by id")
    print("4. Create location")
    print("5. Update location")
    print("6. Delete location")
    print("7. List all events")
    print("8. Find event by name")
    print("9. Find event by id")
    print("10. Create event")
    print("11. Update event")
    print("12. Delete event")
    print("13. List all attendees")
    print("14. Find attendee by id")
    print("15. Create attendee")
    print("16. Update attendee")
    print("17. Delete attendee")

if __name__ == "__main__":
    main()
