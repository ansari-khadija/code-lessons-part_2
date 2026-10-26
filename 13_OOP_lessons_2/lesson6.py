
name= input("Enter student name: ")
marks= int(input("Enter student marks: "))

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Grade:", self.calculate_grade())

    def calculate_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 60:
            return "C"
        elif self.marks >= 35:
            return "D"
        else:
            return "Fail"


s1 = Student(name, marks)
s1.display()