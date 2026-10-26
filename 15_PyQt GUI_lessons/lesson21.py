# Database Handling with Python and PyQt5


import sqlite3

# Connect to the database.
# SQLite creates the file if it does not exist.
connection = sqlite3.connect("students.db")

# Create a cursor to execute SQL commands.
cursor = connection.cursor()

# Create a table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL
    )
""")

# Insert a student record
cursor.execute(
    "INSERT INTO students (name, email) VALUES (?, ?)",
    ("Rahul", "rahul@example.com")
)

# Save changes
connection.commit()

print("Student record inserted successfully.")

# Retrieve all student records
cursor.execute("SELECT * FROM students")
records = cursor.fetchall()

for record in records:
    print(record)

# Close the database connection
connection.close()
