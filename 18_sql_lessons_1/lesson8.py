# part4

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="abc@123",
    database="mall"
)

mycursor = mydb.cursor()

query = """
SELECT product, SUM(price)
FROM customer
GROUP BY product
HAVING SUM(price) > 2000
"""

mycursor.execute(query)

results = mycursor.fetchall()

for row in results:
    print("Product:", row[0], "| Total:", row[1])

mycursor.close()
mydb.close()
