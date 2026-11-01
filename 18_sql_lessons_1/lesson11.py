# part7
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="abc@123",
    database="mall"
)

mycursor = mydb.cursor()

# UNION
print("\n----- UNION -----")

query = """
SELECT city FROM Customers
UNION
SELECT product FROM Orders
"""

mycursor.execute(query)

for row in mycursor.fetchall():
    print(row)


# UNION ALL
print("\n----- UNION ALL -----")

query = """
SELECT city FROM Customers
UNION ALL
SELECT product FROM Orders
"""

mycursor.execute(query)

for row in mycursor.fetchall():
    print(row)


mycursor.close()
mydb.close()