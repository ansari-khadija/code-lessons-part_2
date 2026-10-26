# ThreadPoolExecutor

from concurrent.futures import ThreadPoolExecutor

a,b,c = map(int, input("Enter three numbers separated by spaces: ").split())
num2 = int(input("Enter a number to divide by: "))
def square(num):
    return num / num2

with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(square, [a, b, c])

print("The Division of Numbers:", list(results))
