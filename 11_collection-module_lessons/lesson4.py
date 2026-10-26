from collections import namedtuple

Student = namedtuple("Student", ["name", "age", "marks"])

student = Student("Rahul", 20, 85)

print(student)
print(student.name)
print(student.age)
print(student.marks)
