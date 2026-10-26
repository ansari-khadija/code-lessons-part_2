
class A:
    def college(self):
        print("This is an IT and Software college.")

class B(A):
    def student(self):
        print("I am a student of AI software engineering.")

class C(A):
    def teacher(self):
        print("Professor Riya is our AI development teacher.")

class D(B, C):
    def details(self):
        print("College has various departments.")


obj = D()

obj.college()   # Inherited from A
obj.student()   # Inherited from B
obj.teacher()   # Inherited from C
obj.details()   # Defined in D