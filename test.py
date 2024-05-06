import sqlite3

conn = sqlite3.connect('C:/Users/USER/Desktop/aws/database.db')  # Adjust the path if necessary
c = conn.cursor()

c.execute("SELECT * FROM users")

for row in c.fetchall():
  print(row)

conn.close()