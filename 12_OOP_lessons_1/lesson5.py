# instance variable in oop

def calculate():
    a = 20
    b = 10
    result = a + b

    print("Result:", result)


calculate()
class Player:

    game = "Cyber Arena"       # Class variable
    players_count = 0         # Class variable

    def __init__(self, name, score):
        self.name = name       # Instance variable
        self.score = score     # Instance variable

        Player.players_count += 1


p1 = Player("Nova", 850)
p2 = Player("Shadow", 920)
p3 = Player("Ghost", 700)


print("Game:", Player.game)

print("\nPlayer 1")
print("Name:", p1.name)
print("Score:", p1.score)

print("\nPlayer 2")
print("Name:", p2.name)
print("Score:", p2.score)

print("\nPlayer 3")
print("Name:", p3.name)
print("Score:", p3.score)

print("\nTotal Players:", Player.players_count)
