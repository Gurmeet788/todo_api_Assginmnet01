# FlyRank Assignment 01 - Flask Todo API

This repository contains the solution for **FlyRank Assignment 01**. The project is a RESTful Todo API built using **Flask** and **Flask-RESTX**, implementing CRUD operations with interactive API documentation using Swagger UI.

## Objective

Develop a RESTful API that allows users to create, retrieve, update, and delete tasks while documenting the API using Swagger UI.

## Features

- Create a task
- Retrieve all tasks
- Retrieve a task by ID
- Replace a task (PUT)
- Partially update a task (PATCH)
- Delete a task
- Interactive Swagger UI documentation
- In-memory data storage (No database)

## Technologies Used

- Python 3.x
- Flask
- Flask-RESTX

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/flask-todo-api.git
cd flask-todo-api
```

### 2. Create a virtual environment (Optional)

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

or

```bash
pip install flask flask-restx
```

## Running the Application

```bash
python app.py
```

The server will start at:

```
http://127.0.0.1:5000
```

Swagger UI:

```
http://127.0.0.1:5000/
```

*(Use the correct URL if your Swagger UI is configured differently.)*

---

# API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/tasks` | Retrieve all tasks |
| GET | `/tasks/<id>` | Retrieve a task by ID |
| POST | `/tasks` | Create a new task |
| PUT | `/tasks/<id>` | Replace an existing task |
| PATCH | `/tasks/<id>` | Partially update a task |
| DELETE | `/tasks/<id>` | Delete a task |

---

## Sample Task Object

```json
{
    "id": 1,
    "title": "Learn Flask",
    "completed": false
}
```

---

## Project Structure

```
flask-todo-api/
│
├── app.py
├── requirements.txt
├── README.md
└── routes/
    └── task_routes.py
```

*(Remove the `routes` folder section if your project is contained in a single `app.py`.)*

---

## Testing

The API can be tested using:

- Swagger UI
- Postman
- cURL

---

## Notes

- This project was developed as part of **FlyRank Assignment 01**.
- Tasks are stored in memory and will be lost when the application restarts.
- The project is intended for demonstrating REST API development using Flask and Swagger.

---

## Author

**Gurmeet Kumar**

Computer Science Student | Backend Developer