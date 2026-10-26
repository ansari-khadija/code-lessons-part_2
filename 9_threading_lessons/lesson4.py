# lock in python multithreading

import threading

count = 0
lock = threading.Lock()

def increment():
    global count
    with lock:
        count += 1

def task():
    for _ in range(10):
        increment()

t1 = threading.Thread(target=task)
t2 = threading.Thread(target=task)

t1.start()
t2.start()

t1.join()
t2.join()

print("Final count:", count)
