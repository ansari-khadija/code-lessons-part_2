# inserting data
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="abc@123",
    database="mall"
)

mycursor = mydb.cursor()


values = (
    input("Enter name: "),
      input("Enter phone: "), 
      input("Enter product: "), 
      float(input("Enter price: ")))

query ="""
INSERT INTO customer(name,phone,product,price) 
VALUES(%s,%s,%s,%s)
"""

mycursor.execute(query, values)
mydb.commit()

# print("Data inserted successfully!")



mydb.commit()
mycursor.close()
mydb.close()