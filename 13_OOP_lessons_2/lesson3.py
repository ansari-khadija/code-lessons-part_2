# Multilevel Inheritance 

a = input("Enter name of files: ")
class CEO:
    def check(self):
        print(f"Mrs. CEO is checking {a} files.")

class Manager(CEO):
    def manage(self):
        print(f"Manager is Managing {a} meeting.")

class Employee(Manager):
    def work(self):
        print(f"Employee is Working on {a} project.")

e = Employee()
e.check()
e.manage()
e.work()
