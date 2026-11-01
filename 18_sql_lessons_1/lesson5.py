# mysql functions part1

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="abc@123",
    database="mall"
)

mycursor = mydb.cursor()

# Count total customers
mycursor.execute("SELECT COUNT(*) FROM customer")

result = mycursor.fetchone()

print("Total customers:", result[0])

mycursor.close()
mydb.close()
