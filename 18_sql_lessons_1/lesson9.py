# part5

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="abc@123",
    database="mall"
)

mycursor = mydb.cursor()

# Get customer ID and new price
customer_id = int(input("Enter customer ID: "))
new_price = float(input("Enter new price: "))

# Update customer price
query = """
UPDATE customer
SET price = %s
WHERE id = %s
"""

values = (new_price, customer_id)

mycursor.execute(query, values)

mydb.commit()

print(mycursor.rowcount, "record(s) updated!")

mycursor.close()
mydb.close()
