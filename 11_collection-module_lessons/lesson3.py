from collections import deque

queue = deque(["A", "B", "C"])

queue.append("D")
queue.appendleft("Z")

print(queue)

queue.popleft()

print(queue)
