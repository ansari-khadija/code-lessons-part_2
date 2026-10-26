import json

name=input("Enter your name: ")
age=int(input("Enter your age: "))  
city=input("Enter your city: ")
subject=input("Enter your subject: ")

student = {
    "name": name,
    "age": age,
    "city": city,
    "subject": subject
}

# WRITE: Python dictionary → JSON file
with open("student.json", "w") as file:
    json.dump(student, file)

print("Data written to student.json")


# READ: JSON file → Python dictionary
with open("student.json", "r") as file:
    student_data = json.load(file)

print("Data read from file:")
print(student_data)


# PARSE: Get/use the data from the Python object
key = input("What do you want to see? (name/age/city/subject): ")

print("Value:", student_data[key])

