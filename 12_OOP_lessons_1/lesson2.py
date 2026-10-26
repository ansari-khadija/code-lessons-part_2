# static method in oop methods

a, b = map(int, input("Enter a and b: ").split())

class Calculator:

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b


print("Addition:", Calculator.add(a, b))
print("Subtraction:", Calculator.subtract(a, b))
print("Multiplication:", Calculator.multiply(a, b))


