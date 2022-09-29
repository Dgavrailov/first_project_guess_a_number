import random

computer_number = random.randint(1, 100)
# the computer generates a random number


while True:
    player_input = input("Guess the number between 1 - 100 : ")
    if not player_input.isdigit():
        print("Invalid input. Try again :")
        continue
    player_number = int(player_input)
    if player_number == computer_number:
        print("You guess it")
        break
    elif player_number > computer_number:
        print("The computer number is lower")
    elif player_number < computer_number:
        print("The computer number is higher")
