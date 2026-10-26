from collections import defaultdict

students = defaultdict(list)

students["Python"].append("Rahul")
students["Python"].append("Priya")
students["Java"].append("Amit")

print(students)
print(students["Python"])
