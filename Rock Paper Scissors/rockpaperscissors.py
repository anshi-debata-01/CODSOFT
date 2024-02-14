import random

options = ("Rock" , "Paper" , "Scissors")
running = True

while running == True:
    player = None
    Computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice(Rock , Paper , Scissors):")

    print(f"Player: {player}")
    print(f"Computer: {Computer}")

    if player == Computer:
        print("It's a Tie!")
    elif player == "Rock" and Computer == "Scissors":
        print("You are Winner")
    elif player == "Paper" and Computer == "Rock":
        print("You are Winner!")
    elif player == "Scissors" and Computer =="Paper":
        print("You are Winner!")
    else:
        print("You Lose!")
    if not input("Play again? (y/n): ").lower()== "y":
        running = False
print("Thanks for Playing!")