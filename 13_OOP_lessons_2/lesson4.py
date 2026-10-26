# Hierarchical Inheritance


class Animal:
    def __init__(self, name1, name2):
        self.name1 = name1
        self.name2 = name2

    def work(self):
        print(f"{self.name1} is participating in hackathons.")
        print(f"{self.name1} made a project on {self.name2}")


class Win(Animal):
    def wins(self):
        print(f"{self.name1} wins hackathons!")


class Prize(Animal):
    def prizes(self):
        print(f"{self.name1} got 1st prize for project {self.name2}.")


a1 = Win("Rohan", "AI Traffic Assistant")
a2 = Prize("Rohan", "AI Traffic Assistant")

a1.work()
a1.wins()
a2.prizes()
