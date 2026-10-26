import json

name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")
subject = input("Enter your subject: ")

student = {
    "name": name,
    "age": age,
    "city": city,
    "subject": subject
}

json_data = json.dumps(student)
print(json_data)

student = json.loads(json_data)

key = input("What do you want to see? (name/age/city/subject): ")

print("Value:", student[key])
