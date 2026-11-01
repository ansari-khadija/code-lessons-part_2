# part6

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="abc@123",
    database="mall"
)

mycursor = mydb.cursor()

# INNER JOIN
print("\n----- INNER JOIN -----")

query = """
SELECT *
FROM Customers
INNER JOIN Orders
ON Customers.customer_id = Orders.customer_id
"""

mycursor.execute(query)

for row in mycursor.fetchall():
    print(row)


# LEFT JOIN
print("\n----- LEFT JOIN -----")

query = """
SELECT *
FROM Customers
LEFT JOIN Orders
ON Customers.customer_id = Orders.customer_id
"""

mycursor.execute(query)

for row in mycursor.fetchall():
    print(row)


# RIGHT JOIN
print("\n----- RIGHT JOIN -----")

query = """
SELECT *
FROM Customers
RIGHT JOIN Orders
ON Customers.customer_id = Orders.customer_id
"""

mycursor.execute(query)

for row in mycursor.fetchall():
    print(row)


mycursor.close()
mydb.close()