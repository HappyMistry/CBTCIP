import random

options = ("rock","paper","scissors")
running = True

while running:
    player = None
    computer = random.choice(options)
    player = input("Enter Your Choice(rock,paper,scissors)")
    if player not in options:
        print("Don't be stupid...\nPlease select proper option...")
    else:
        print(f"player:{player}")
        print(f"computer:{computer}")
        if player == computer:
            print("It's Tie!")
        elif player == "rock" and computer == "scissors":
            print("You Win!")
        elif player == "scissors" and computer == "paper":
            print("You Win!")  
        elif player == "paper" and computer == "rock":
            print("You Win!")
        else:
            print("You Lost!")
        play_again = input("Do You Want to Play Again?(y/n)")
        if play_again == 'n' or  play_again == 'N':
            running = False
print("Thanks for Playing!...\nVisit Again!...")