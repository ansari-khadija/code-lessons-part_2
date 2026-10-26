import threading

num = int(input("Enter a number: "))
def add(num):
    print(f"Square: {num + num}")

t1 = threading.Thread(target=add, args=(num,))

t1.start()
t1.join()

print("Done!")

