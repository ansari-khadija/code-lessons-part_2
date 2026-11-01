# view data
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="abc@123",
    database="mall"
)

mycursor = mydb.cursor()

# Execute SELECT query
mycursor.execute("SELECT * FROM customer")

# Fetch records
results = mycursor.fetchall()

# Display records
for row in results:
    print(row)

# Close connection
mycursor.close()
mydb.close()