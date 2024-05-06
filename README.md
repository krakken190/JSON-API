# Simple Flask API for User Management

1.Add users (multiple in a single request)

2.Retrieve users with IDs above a threshold

# Setup

1.Create a virtual environment.

2.Install Flask & sqlite3: pip install Flask sqlite3

3.Clone this repository.

# Usage

1.Run the app: python app.py

# Endpoints

1./adduser (POST): Add users (JSON with id & name keys)

2./getusers (GET): Retrieve users above threshold (default 5) - Optional threshold query parameter

# Database

1.Uses database.db (SQLite)

# Example (Postman):

# Adding Users:

1.POST: http://localhost:5000/adduser
2.Body (raw JSON):
JSON
[
  { "id": 100, "name": "xyz" },
  { "id": 10, "name": "abc" }
]
