# part3

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="abc@123",
    database="mall"
)

mycursor = mydb.cursor()

# Group customers by product
query = """
SELECT product, SUM(price)
FROM customer
GROUP BY product
"""

mycursor.execute(query)

results = mycursor.fetchall()

for row in results:
    print("Product:", row[0], "| Total Price:", row[1])

mycursor.close()
mydb.close()
