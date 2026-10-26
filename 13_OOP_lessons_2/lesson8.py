# different methods of polymorphism
class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Marks: {self.marks}"

    def __add__(self, other):
        return self.marks + other.marks

    def __len__(self):
        return len(self.name)

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.marks == other.marks
    
    def __gt__(self, other):
        return self.marks > other.marks

    def __lt__(self, other):
        return self.marks < other.marks

# Store student objects in a list
students = []

for i in range(2):
    print(f"\nEnter details of Student {i + 1}")

    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    marks = float(input("Enter your marks: "))

    s = Student(name, age, marks)
    students.append(s)

s1 = students[0]
s2 = students[1]


# Calling magic methods
print("\n--- Student Details ---")
print(s1)                 # __str__()

print("\nTotal marks of Student 1 and 2:")
print(s1 + s2)            # __add__()

print("\nLength of Student 1's name:")
print(len(s1))            # __len__()

print("\nComparing Student 1 and 2:")
print("Students are equal" if s1 == s2 else "Students are not equal")           # __eq__()

     