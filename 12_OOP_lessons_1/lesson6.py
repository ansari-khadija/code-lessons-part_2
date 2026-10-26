# local variable in oop variable 

def calculate_score():
    player = input("Enter player name: ")
    kills = int(input("Enter kills: "))
    bonus = int(input("Enter bonus: "))

    score = (kills * 100) + bonus

    print("\n--- SCORE ---")
    print("Player:", player)
    print("Score:", score)


calculate_score()
