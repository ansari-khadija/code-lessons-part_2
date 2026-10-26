
# Single Inheritance in OOP

# Parent Class
a=input("Enter animal name: ")

class Animal:

    def run(self):
        print(a, "is running")

# Child Class inherits from Animal
class Dog(Animal):

    def bark(self):
        print("Dog is barking at",a)

# Create an object of the Child Class
d = Dog()

# Call Parent Class Method
d.run()

# Call Child Class Method
d.bark()


### Key points

# - Parent class: `Animal`
# - Child class: `Dog`
# - Inheritance: `class Dog(Animal)` means `Dog` inherits from `Animal`.
# - Object: `d = Dog()` creates a `Dog` object.
# - Parent method: `d.eat()` works because `Dog` inherits from `Animal`.
# - Child method: `d.bark()` belongs directly to `Dog`.

# Definition: Single inheritance occurs when one child class inherits from one parent class.