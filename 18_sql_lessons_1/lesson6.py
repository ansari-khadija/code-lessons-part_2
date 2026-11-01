# part2
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="abc@123",
    database="mall"
)

mycursor = mydb.cursor()

# 1. SUM - Total price
mycursor.execute("SELECT SUM(price) FROM customer")
total = mycursor.fetchone()
print("Total sales:", total[0])

# 2. AVG - Average price
mycursor.execute("SELECT AVG(price) FROM customer")
average = mycursor.fetchone()
print("Average price:", average[0])

# 3. MAX - Highest price
mycursor.execute("SELECT MAX(price) FROM customer")
maximum = mycursor.fetchone()
print("Highest price:", maximum[0])

# 4. MIN - Lowest price
mycursor.execute("SELECT MIN(price) FROM customer")
minimum = mycursor.fetchone()
print("Lowest price:", minimum[0])

mycursor.close()
mydb.close()
