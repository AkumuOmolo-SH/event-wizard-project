# EVENT WIZARD - Phase 3 CLI Project

Event Wizard CLI is a Python command-line application that helps users manage events, venues, and safety rules. The project demonstrates the use of SQLAlchemy ORM, Alembic migrations, and interactive CLI development with input validation and data management.
The application is ideal for organizers who need a platform to record stats and analyze or get estimates.

---

## Features

1. Locations Management

- Create, read, update, and delete locations. Find a location by name or ID.

2. Track capacity, and resources

- Assess a location's capacity by number of attendees with tickets sold
- 
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

SQLAlchemy ORM
 for database interactions

Alembic
 for database migrations

SQLite (default local database)

Tabulate
(optional, for neatly formatted tables in CLI)se
Pipenv to install Faker to save you some time.

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
Usage:

Run the CLI:

python cli.py

Follow the prompts to manage locations, events, attendees, and safety rules.

Example:

1. Create Location
2. List Locations
3. Create Event
...
0. Exit

**## Preview**
<img width="1857" height="954" alt="Screenshot from 2025-08-29 03-56-14" src="https://github.com/user-attachments/assets/5964688c-6222-4800-bab4-1b31bfbabd71" />


**###  Author**

**Akumu Omolo**  
GitHub: [@AkumuOmolo-SH](https://github.com/AkumuOmolo-SH)

---

**### License**

[![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)  
This project is licensed under the [MIT License](LICENSE).
