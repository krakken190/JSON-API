from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def create_users_table():
  conn = sqlite3.connect('database.db')
  c = conn.cursor()
  c.execute('''CREATE TABLE IF NOT EXISTS users (
              user_id INTEGER PRIMARY KEY NOT NULL,
              name TEXT NOT NULL
             )''')
  conn.commit()
  conn.close()

create_users_table()

@app.route('/', methods=['GET'])
def index():
  return "Welcome to the API!"

@app.route('/adduser', methods=['POST'])
def add_user():
  user_data = request.json

  conn = sqlite3.connect('database.db')
  c = conn.cursor()

  # Iterating through each user dictionary in the list and adding them to the database
  for user in user_data:
    user_id = user.get('id')
    name = user.get('name')

    # Checking if user ID already exists
    c.execute("SELECT COUNT(*) FROM users WHERE user_id = ?", (user_id,))
    if c.fetchone()[0] == 0:  
      c.execute("INSERT INTO users (user_id, name) VALUES (?, ?)", (user_id, name))
    else:
      print(f"Duplicate user ID: {user_id} - Skipping insertion")  # Log a message for duplicates

  conn.commit()
  conn.close()

  return jsonify({'message': 'Users added successfully'}), 200

@app.route('/getusers', methods=['GET'])
def get_users():
  # Checking threshold ID from the query parameter
  threshold_id = int(request.args.get('threshold', 5))  # Taking default threshold as 5

  conn = sqlite3.connect('database.db')
  c = conn.cursor()

  c.execute("SELECT name FROM users WHERE user_id > ?", (threshold_id,))
  names = [row[0] for row in c.fetchall()]  # Extract names from results

  response = {'names_with_ids_above_' + str(threshold_id): names}

  conn.close()
  return jsonify(response)

if __name__ == '__main__':
  app.run(debug=True)