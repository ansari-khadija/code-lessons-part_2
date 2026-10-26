# oop functions 

def student_info(last, now, profit, loss):
    print("Last Month Income:", last)
    print("This Month Income:", now)
    print("Your Profit:", profit)
    print("Your Loss:", loss)


last = int(input("Enter Last Month income: "))
now = int(input("Enter This Month income: "))

profit = max(now - last, 0)
loss = min(now - last, 0)

student_info(last, now, profit, loss)
