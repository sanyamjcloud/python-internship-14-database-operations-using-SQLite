README.md

# Database App (SQLite + Python)

## Project Overview

This is a command-line Python database application demonstrating full CRUD operations using SQLite. It allows users to create a database, insert records, fetch data, update entries, and delete records securely using parameterized queries.

---

## Features

* Programmatic database and table creation
* Insert user records dynamically
* Fetch and display records in formatted table output
* Update existing records
* Delete records
* SQL injection protection using parameterized queries
* Proper transaction handling with commit
* Safe connection closing

---

## Tech Stack

* Python 3
* SQLite3 (built-in library)

---

## File Structure

```
project-folder/
│
├── database_app.py
└── users.db (auto-generated after running)
```

---

## How to Run

1. Open the project folder in VS Code
2. Open terminal
3. Run:

```
python database_app.py
```

---

## Menu Options

```
1. Add User
2. View Users
3. Update User
4. Delete User
5. Exit
```

---

## Concepts Demonstrated

* Database connection handling
* SQL schema creation
* CRUD operations
* Parameterized SQL queries
* Data persistence using SQLite

---

## Future Improvements

* Search functionality
* Input validation
* Password encryption support
* GUI interface
* Logging system

---

## Author

sanyam jain