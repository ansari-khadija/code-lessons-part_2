# Employee Management System

# Base class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


# Multilevel inheritance: Person -> Employee -> Manager
class Employee(Person):
    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = salary

    def show_role(self):
        print("Role: Employee")

    def calculate_salary(self):
        return self.salary


class Manager(Employee):
    def __init__(self, name, age, employee_id, salary, bonus):
        super().__init__(name, age, employee_id, salary)
        self.bonus = bonus

    # Method overriding
    def show_role(self):
        print("Role: Manager")

    def calculate_salary(self):
        return super().calculate_salary() + self.bonus


# Hierarchical inheritance:
# Employee -> Developer and Designer
class Developer(Employee):
    def show_role(self):
        print("Role: Software Developer")


class Designer(Employee):
    def show_role(self):
        print("Role: UI/UX Designer")


# Multiple inheritance
class Attendance:
    def mark_attendance(self):
        print("Attendance marked")


class ManagerDashboard(Manager, Attendance):
    def show_dashboard(self):
        print("Manager dashboard opened")


# Display employee information
print("=== Manager Details ===")

m = Manager("Rahul", 35, "M101", 50000, 10000)
m.show_details()
m.show_role()
print("Total salary:", m.calculate_salary())

print("\n=== Developer Details ===")

d = Developer("Priya", 25, "E102", 40000)
d.show_details()
d.show_role()
print("Total salary:", d.calculate_salary())

print("\n=== Manager Dashboard ===")

dashboard = ManagerDashboard(
    "Amit", 40, "M103", 60000, 15000
)

dashboard.show_role()
dashboard.mark_attendance()
dashboard.show_dashboard()

print("\n=== Method Resolution Order ===")
print([cls.__name__ for cls in ManagerDashboard.mro()])