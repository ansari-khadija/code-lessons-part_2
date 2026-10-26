# Multi-threading

import threading
import time

num = int(input("Enter a number: "))

def square(num):
    print(f"Square: {num * num}")
    time.sleep(1)

def cube(num):
    print(f"Cube: {num * num * num}")
    time.sleep(1)

t1 = threading.Thread(target=square, args=(num,))
t2 = threading.Thread(target=cube, args=(num,))

t1.start()
t2.start()

t1.join()
t2.join()

print("Done!")
