import pickle

# Take input from user
name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")
subject = input("Enter your subject: ")

# Create dictionary
student = {
    "name": name,
    "age": age,
    "city": city,
    "subject": subject
}

# ---------------- PICKLING ----------------
# Python dictionary → Pickle file
with open("student.pkl", "wb") as file:
    pickle.dump(student, file)

print("Data written to student.pkl")


# ---------------- UNPICKLING ----------------
# Pickle file → Python dictionary
with open("student.pkl", "rb") as file:
    student_data = pickle.load(file)

print("Data read from student.pkl:")
print(student_data)


# ---------------- ACCESS DATA ----------------
key = input("What do you want to see? (name/age/city/subject): ")

print("Value:", student_data[key])