
# Multiple Inheritance in Python OOP

# Parent Class 1
class Student:
    def __init__(self, name):
        self.name = name

    def display_student(self):
        print("Student Name:", self.name)

# Parent Class 2
class Exam:
    def __init__(self, subject_marks):
        self.subject_marks = subject_marks

    def calculate_total(self):
        return sum(self.subject_marks.values())

    def calculate_percentage(self):
        total = self.calculate_total()
        return total / len(self.subject_marks)

# Child Class inherits from both parents
class Result(Student, Exam):
    def __init__(self, name, subject_marks):
        Student.__init__(self, name)
        Exam.__init__(self, subject_marks)

    def display_result(self):
        self.display_student()

        print("\n--- Exam Result ---")

        for subject, marks in self.subject_marks.items():
            print(f"{subject}: {marks}")

        print("Total Marks:", self.calculate_total())
        print(f"Percentage: {self.calculate_percentage():.2f}%")

        if self.calculate_percentage() >= 40:
            print("Result: PASS")
        else:
            print("Result: FAIL")

# Get Student Details
name = input("Enter student name: ")

subject_marks = {
    "Python": int(input("Enter Python marks: ")),
    "SQL": int(input("Enter SQL marks: ")),
    "Statistics": int(input("Enter Statistics marks: "))
}

# Create Result Object
student = Result(name, subject_marks)

# Display Final Result
student.display_result()


