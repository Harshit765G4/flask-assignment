# 🧪 Flask & MongoDB Assignment

A small Flask coursework repository demonstrating two backend tasks: serving JSON data through a Flask API and building a simple HTML form that stores submitted student information in MongoDB.

## 🎯 Overview

This repository is focused on learning the fundamentals of:

- Flask application setup and routing
- JSON file handling
- Building simple API endpoints
- HTML forms with Jinja templates
- Handling GET and POST requests
- MongoDB connectivity with PyMongo
- Persisting form data in a MongoDB collection

## 📁 Repository Structure

```text
flask-assignment/
├── flask-mongo-assignment-task-1/
│   ├── app.py
│   └── data.json
└── flask-mongo-assignment-task-2/
    ├── app.py
    ├── requirements.txt
    └── templates/
        └── form.html
```

## 🧩 Task 1 — Flask JSON API

Path:

```text
flask-mongo-assignment-task-1/
```

This task implements a minimal Flask API that reads records from `data.json` and returns them as JSON.

### Route

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api` | Reads `data.json` and returns the contents through `jsonify()` |

### Example data

The included `data.json` contains simple records with an `id` and `name` field:

```json
[
  { "id": 1, "name": "Harshit Garg" },
  { "id": 2, "name": "Harsh Sharma" },
  { "id": 3, "name": "New User" }
]
```

## 🧩 Task 2 — Flask Form + MongoDB

Path:

```text
flask-mongo-assignment-task-2/
```

This task extends the Flask application with:

- A browser-based student submission form
- Jinja template rendering
- POST form handling
- MongoDB persistence through PyMongo
- A success response after insertion
- The same JSON-backed `/api` endpoint

### Routes

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | Displays the student form |
| POST | `/` | Reads name/email and inserts a document into MongoDB |
| GET | `/success` | Shows a successful submission message |
| GET | `/api` | Loads and returns JSON data from `data.json` |

### MongoDB document

Submitted form data is inserted into the `students` collection in the `studentDB` database using a structure similar to:

```json
{
  "name": "Student Name",
  "email": "student@example.com"
}
```

### Form

`templates/form.html` contains required fields for:

- Name
- Email

The template also displays a server-side error message when the Flask application passes an `error` value to the template.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Application language |
| Flask | Web framework |
| PyMongo | MongoDB driver |
| MongoDB | Persistent student data storage |
| HTML | Form UI |
| Jinja | Server-side templating |
| JSON | Local API data source |

## 🚀 Getting Started

### Prerequisites

- Python 3
- `pip`
- MongoDB for Task 2

### Task 1 Setup

Navigate to the first task:

```bash
cd flask-mongo-assignment-task-1
python -m pip install flask
python app.py
```

Open:

```text
http://127.0.0.1:5000/api
```

### Task 2 Setup

Navigate to the second task:

```bash
cd flask-mongo-assignment-task-2
python -m pip install -r requirements.txt
python app.py
```

Open:

```text
http://127.0.0.1:5000/
```

Then submit a name and email through the form.

## 🔌 MongoDB Configuration

The current Task 2 implementation creates the client using a connection value directly inside `app.py`:

```python
client = MongoClient("mongodbKey")
```

For local practice, replace that value with a valid MongoDB connection string appropriate for your environment.

For a production-style implementation, keep the connection string in an environment variable instead:

```python
import os
from pymongo import MongoClient

client = MongoClient(os.environ["MONGODB_URI"])
```

Do not commit real MongoDB usernames, passwords, or connection strings to source control.

## ⚠️ Current Limitations

The code is suitable as a learning assignment but is not production-ready.

- Both Flask applications use `debug=True`.
- MongoDB connection configuration is hard-coded in Task 2.
- There is no authentication or authorization.
- Validation is basic and mostly provided by the HTML form.
- Database errors are surfaced directly to the template through the caught exception text.
- There are no automated tests.
- There is no logging, rate limiting, or production deployment configuration.

## 🔐 Security Recommendations

Before deploying beyond local coursework:

1. Move MongoDB configuration to environment variables.
2. Disable Flask debug mode.
3. Add server-side input validation and sanitization.
4. Avoid returning raw database exception messages to users.
5. Add authentication and authorization where student data requires protection.
6. Add HTTPS and appropriate deployment configuration.

## 🧠 Learning Outcomes

This assignment provides hands-on practice with:

- Flask application structure
- Route decorators
- GET and POST requests
- JSON serialization
- Local JSON file reading
- Jinja templates
- HTML form handling
- Redirects
- MongoDB collections
- Document insertion
- Basic error handling

## 🚀 Suggested Improvements

- Add a shared `requirements.txt` at the repository root.
- Add environment-based MongoDB configuration with `.env`.
- Add CRUD operations for student records.
- Add duplicate-email validation.
- Add a page to view submitted records.
- Add proper success/error templates.
- Add unit and integration tests with `pytest`.
- Add API response validation and structured error responses.
- Add a production WSGI server and deployment instructions.

## 📄 License

No `LICENSE` file is currently present, so no formal open-source license should be assumed.

## 👨‍💻 Author

**Harshit Garg**

GitHub: [@Harshit765G4](https://github.com/Harshit765G4)

---

This repository is maintained as a Flask learning and assignment project.
