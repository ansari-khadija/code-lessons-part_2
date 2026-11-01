
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="abc@123",
    database="mall"
)

mycursor = mydb.cursor()

# Close connection
mycursor.close()
mydb.close()
