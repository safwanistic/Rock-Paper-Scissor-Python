import random

user_wins =0
computer_wins=0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input('Type Rock/Paper/Scissors or Q to Quit: ').lower()
    if user_input == 'q':
        break
    
    if user_input not in ["rock", "paper", "scissors"]:
        continue
    
    random_number = random.randint(0,2)
    # Rock:0 , Paper: 1, Scissors:2
    computer_pick = options[random_number]
    print("Computer selected ", computer_pick + " !")

    if user_input == "rock" and computer_pick== "scissors":
        print("YOU WON!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick== "paper":
        print("YOU WON!")
        user_wins += 1

    if user_input == "paper" and computer_pick== "rock":
        print("YOU WON!")
        user_wins += 1
    
    else:
        print("YOU LOST ! BETTER LUCK NEXT TIME!")
        computer_wins+=1

print('YOU WON ', user_wins, " time(s)")
print('COMPUTER WON', computer_wins, 'time(s)')
print('THANK YOU FOR PLAYING!')
