import random
while True:
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)
    player = None
    while player not in choices:
        player = input("input your choises :").lower()
    if player == computer:
        print("Player : ", player)
        print("Computer : ", computer)
        print("tie!")
    elif player == "rock":
        if computer == "paper":
            print("Player : ", player)
            print("Computer : ", computer)
            print("you lose!")
        elif computer == "scissors":
            print("Player : ", player)
            print("Computer : ", computer)
            print("you win!")
    elif player == "paper":
        if computer == "scissors":
            print("Player : ", player)
            print("Computer : ", computer)
            print("you lose!")
        elif computer == "rock":
            print("Player : ", player)
            print("Computer : ", computer)
            print("you win!")
    elif player == "scissors":
        if computer == "paper":
            print("Player : ", player)
            print("Computer : ", computer)
            print("you win!")
        elif computer == "rock":
            print("Player : ", player)
            print("Computer : ", computer)
            print("you lose!")
    play_again = input("play aigain? (yes/no) :").lower()
    if play_again != "yes":
        break

print("Bye")