import random
print("Welcome to Rock, Paper, Scissors Game")
print("What do you choose?")

user_choice = int(input("Type 0 for Rock, 1 for Paper, or 2 for Scissors\n"))
computer_choice = random.randint(0, 2)

user_choice_list = ['Rock', 'Paper', "Scissors"]
computer_choice_list = ['Rock', 'Paper', "Scissors"]

print(f"Your choice is {user_choice_list[user_choice]}")
print(f"Computer choice is {computer_choice_list[computer_choice]}")


if((user_choice == 0) and (computer_choice == 2)):
    print("You win!")
elif((user_choice == 2) and (computer_choice == 1)):
    print("You win!")
elif((user_choice == 1) and (computer_choice == 0)):
    print("You win!")
elif((user_choice == 2) and (computer_choice == 0)):
    print("You lose!")
elif((user_choice == 1) and (computer_choice == 2)):
    print("You lose!")
elif((user_choice == 0) and (computer_choice == 1)):
    print("You lose!")
elif((user_choice == 0) and (computer_choice == 0)):
    print("Game draw!")
elif((user_choice == 1) and (computer_choice == 1)):
    print("Game draw!")
elif((user_choice == 2) and (computer_choice == 2)):
    print("Game draw!")
