
# Class Method in OOP

class Player:
    game = "Cyber Arena"
    players_count = 0

    def __init__(self, name, score):
        self.name = name
        self.score = score
        Player.players_count += 1

    # Class Method to change the game name
    @classmethod
    def change_game(cls, new_game):
        cls.game = new_game

    # Class Method to display total players
    @classmethod
    def show_players_count(cls):
        print("Total Players:", cls.players_count)

# Create Objects
p1 = Player("Nova", 850)
p2 = Player("Shadow", 920)
p3 = Player("Ghost", 700)

# Display Original Game Name
print("Original Game:", Player.game)

# Change Game Name
Player.change_game("Battle Zone")

# Display Updated Game Name
print("Updated Game:", Player.game)

# Display Total Players
Player.show_players_count()
