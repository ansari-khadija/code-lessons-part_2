# Polymorphism code
a = int(input("Enter payment: "))
total = 70000
b = total - a

class Payment:
    def pay(self):
        print("Processing payment...")

class UPI(Payment):
    def pay(self):
        print("Total amount:", total)

class CreditCard(Payment):
    def pay(self):
        print(f"You have {total} in your credit card.")

class Cash(Payment):
    def pay(self):
        print("Cash successfully transferred.")
        print("Remaining amount:", b)
        
# Create objects
p1 = UPI()
p2 = CreditCard()
p3 = Cash()

# Call the same method
p1.pay()
p2.pay()
p3.pay()