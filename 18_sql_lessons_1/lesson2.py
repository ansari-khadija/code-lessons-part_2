# create table
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="abc@123",
    database="mall"
)

mycursor = mydb.cursor()

# print("Connected to Mall Database!")

mycursor.execute(
    "CREATE TABLE customer("
    "id INT AUTO_INCREMENT PRIMARY KEY,"
    "name  VARCHAR(200),"
    "phone VARCHAR(14),"
    "product VARCHAR(200),"
    "price DECIMAL(10, 2)"
    ")"
)

mydb.commit()
mycursor.close()
mydb.close()