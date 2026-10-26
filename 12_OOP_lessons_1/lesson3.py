# instance method in oop methods

class ExpenseTracker:

    def __init__(self, name, income):
        self.name = name
        self.income = income
        self.expenses = 0

    def add_expense(self, amount):
        self.expenses += amount

    def remaining_money(self):
        return self.income - self.expenses

    def show_summary(self):
        print("\n--- Expense Summary ---")
        print("Name:", self.name)
        print("Income:", self.income)
        print("Total Expenses:", self.expenses)
        print("Remaining:", self.remaining_money())


# Create an object
name = input("Enter your name: ")
income = int(input("Enter your monthly income: "))

person = ExpenseTracker(name, income)

# Add expenses
food = int(input("Enter food expense: "))
travel = int(input("Enter travel expense: "))
shopping = int(input("Enter shopping expense: "))

person.add_expense(food)
person.add_expense(travel)
person.add_expense(shopping)

# Show result
person.show_summary()
