# EVENT WIZARD - Phase 3 CLI Project

Event Wizard CLI is a Python command-line application that helps users manage events, venues, and safety rules. The project demonstrates the use of SQLAlchemy ORM, Alembic migrations, and interactive CLI development with input validation and data management.
The application is ideal for organizers who need a platform to record stats and analyze or get estimates.

---

## Features

1. Locations Management

- Create, read, update, and delete locations. Find a location by name or ID.

2. Track capacity, and resources

- Assess a location's capacity by number of attendees with tickets sold
- Log a location's resources e.g no. of toilets

3. Events Management

- Create, read, update, and delete events

- Assign events to locations and track tickets sold

- Identify the best-selling event
  
- Easily find your event with an ID or name

4. Safety Management

- Add, view, update, and delete safety information for events

- Track staff, nurses, and ambulances required

5. User-Friendly CLI

- Clear menu navigation with color-styled menus and results.

- Input validation to prevent errors

- Easy navigation per operation

---


**## Technologies Used**

Python 3

SQLAlchemy ORM for database interactions

Alembic for database migrations

SQLite (default local database)

Tabulate
( for neatly formatted tables in CLI)s

---

**## How to run this project ##**

1.Installation

- Clone the repository:

git clone <your-repo-url>
cd event_wizard_project

- Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

- Install dependencies:

pip install -r requirements.txt

- Set up the database:

python seed.py

---
**## Repository struture**

``
event-wizard-project/
│
├── alembic/
│   ├── versions/
│   └── env.py
│
├── lib/
│   ├── models/
│   │   ├── event.py
│   │   ├── location.py
│   │   └── safety.py
│   └── __init__.py
│
├── .gitignore
├── cli.py
├── event_wizard_db.py
├── requirements.txt
├── README.md
└── venv/
``

---

**## Usage**

Run the CLI:

python cli.py

Follow the prompts in the main menu to manage locations, events, and safety rules.

You are presented with a main menu. You navigate by entering the number corresponding to each option.

**##.Main Menu Options**

*1. Locations*

List Locations: Displays all stored locations in a table.

Find by ID: Retrieve a location by its unique ID.

Find by Name: Search for a location by name.

Create Location: Add a new location with capacity, number of bars, and toilets.

Update Location: Modify an existing location’s details.

Delete Location: Remove a location from the database.

*2. Events*

List Events: Show all events.

Find by ID / Name: Search for events using ID or name.

Create Event: Add a new event by specifying name, tickets sold, and location.

Update Event: Edit an event’s details.

Delete Event: Remove an event.

Best-Selling Event: Displays the event with the highest ticket sales.

*3.Safety*

List Safety Rules/Measures: Displays all safety rules linked to events.

Create Safety Rule: Add security staff, ambulances, and nurses for a specific event.

Update Safety Rule: Modify existing safety information.

Delete Safety Rule: Remove safety information.

Find Safety by Event ID: Retrieve safety info for a specific event.

*4.Helpers / Quick Actions*

Suggest Location: Input tickets sold and the CLI recommends a suitable location.

Event Ticket Overview: Displays all events with their current tickets sold.

*5.Exit*

---

**##Workflow**

1. Select a menu option by entering its corresponding number.

2. Input prompts guide you through each operation.

3. Tables are displayed using tabulate for readability.

4. Invalid inputs trigger error messages.

5. After completing an action, press Enter to return to the previous menu or main menu.

**## Preview**
---
<img width="1857" height="954" alt="Screenshot from 2025-08-29 03-56-14" src="https://github.com/user-attachments/assets/5964688c-6222-4800-bab4-1b31bfbabd71" />
---

**###  Author**

**Akumu Omolo**  
GitHub: [@AkumuOmolo-SH](https://github.com/AkumuOmolo-SH)


**### License**

[![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)  
This project is licensed under the [MIT License](LICENSE).
