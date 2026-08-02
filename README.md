# FlyRank Backend Assignments - Flask Todo API

This repository contains my solutions for **FlyRank Backend Assignments**. The project is a RESTful Todo API built using **Flask**, **Flask-RESTX**, and **SQLite**, with interactive API documentation provided by **Swagger UI**.

---

# Assignments

## Assignment 01

Implemented a RESTful Todo API with:

* CRUD operations
* Flask-RESTX
* Swagger UI documentation
* In-memory data storage

## Assignment 02

Enhanced Assignment 01 by replacing in-memory storage with **SQLite** and adding persistent database support.

New additions include:

* SQLite database integration
* Database initialization
* Database seeding
* Parameterized SQL queries
* Persistent task storage

---

# Features

* Create a task
* Retrieve all tasks
* Retrieve a task by ID
* Replace a task (PUT)
* Partially update a task (PATCH)
* Delete a task
* Interactive Swagger UI documentation
* SQLite database persistence
* Automatic database initialization
* Database seeding with sample tasks
* Request validation using Flask-RESTX

---

# Technologies Used

* Python 3.x
* Flask
* Flask-RESTX
* SQLite

---

# Installation

## 1. Clone the repository

```bash
git clone https://github.com/your-username/flask-todo-api.git
cd flask-todo-api
```

## 2. Create a virtual environment (Optional)

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

or

```bash
pip install flask flask-restx
```

---

# Running the Application

```bash
python app.py
```

The server will start at:

```
http://127.0.0.1:5000
```

Swagger UI is available at:

```
http://127.0.0.1:5000/
```

---

# API Endpoints

| Method | Endpoint      | Description                       |
| ------ | ------------- | --------------------------------- |
| GET    | `/tasks`      | Retrieve all tasks                |
| GET    | `/tasks/<id>` | Retrieve a task by ID             |
| POST   | `/tasks`      | Create a new task                 |
| PUT    | `/tasks/<id>` | Replace an existing task          |
| PATCH  | `/tasks/<id>` | Partially update an existing task |
| DELETE | `/tasks/<id>` | Delete a task                     |

---

# Sample Task Object

```json
{
    "id": 1,
    "title": "Learn Flask",
    "completed": false
}
```

---

# Project Structure

```text
flask-todo-api/
│
├── app.py
├── database.py
├── requirements.txt
├── README.md
├── .gitignore
└── routes/
    └── task_routes.py
```

---

# Database Initialization

When the application starts, it automatically performs the following steps:

1. Creates the **tasks** table if it does not already exist.
2. Checks whether the table contains any records.
3. Seeds the database with three sample tasks only if the table is empty.

This ensures that duplicate sample data is never inserted.

---

# Database Seeding

The application automatically inserts the following sample tasks when the database is created for the first time:

* Learn Flask
* Learn SQL
* Learn Python

Seeding only occurs when the `tasks` table is empty.

---

# Git Repository

The SQLite database file (`tasks.db`) is **not included** in this repository.

The file is automatically created when the application runs for the first time through the database initialization process.

The `tasks.db` file is excluded from version control using `.gitignore` because it is generated automatically and should not be committed to the repository.

---

# Testing

The API can be tested using:

* Swagger UI
* Postman
* cURL

---

# Notes

* This repository contains solutions for **FlyRank Assignment 01** and **FlyRank Assignment 02**.
* Assignment 02 extends Assignment 01 by replacing in-memory storage with SQLite.
* All CRUD operations use parameterized SQL queries to improve security and help prevent SQL injection.
* Tasks are stored persistently in the SQLite database.
* Swagger UI provides interactive API documentation and request validation.

---

# Author

**Gurmeet Kumar**

Computer Science Student | Backend Developer
