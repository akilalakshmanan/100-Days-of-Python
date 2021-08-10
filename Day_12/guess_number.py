# Guess the number game
import random
print("Welcome to number guessing game!")
print("I'm thinking of a number between 1 and 100.")
attempts_rem_easy = 10
attempts_rem_hard = 5
difficulty_level = input(
    "Choose a difficulty level. Type 'easy' or 'hard': ").lower()


def game_easy():
    number = random.randint(1, 100)
    print(f"the guessed number is: {number}")
    global attempts_rem_easy
    game_over = False
    print(f"You have {attempts_rem_easy} chances to guess the number")
    while(attempts_rem_easy != 0) and (not game_over):
        user_guess = int(input("Make a guess: "))
        if user_guess > number:
            print("Your guess is too high!")
            attempts_rem_easy = attempts_rem_easy - 1
            print(f"You have {attempts_rem_easy} chances to guess the number")
        elif user_guess < number:
            print("Your guess is too low!")
            attempts_rem_easy = attempts_rem_easy - 1
            print(f"You have {attempts_rem_easy} chances to guess the number")
        elif user_guess == number:
            print(
                f"Good job! You have guessed the {number} with {attempts_rem_easy} guesses remaining")
            game_over = True

    if user_guess != number and attempts_rem_easy == 0:
        print(f"Wrong guess.. You have used all your attempts to guess..")
        print(f"The actual number is {number}.")
        game_over = True


def game_hard():
    number = int(random.randint(1, 100))
    print(f"the guessed number is: {number}")
    global attempts_rem_hard
    game_over = False
    print(f"You have {attempts_rem_hard} chances to guess the number")
    while(attempts_rem_hard != 0) and (not game_over):
        user_guess = int(input("Make a guess: "))
        if user_guess > number:
            print("Your guess is too high!")
            attempts_rem_hard = attempts_rem_hard - 1
            print(f"You have {attempts_rem_hard} chances to guess the number")
        elif user_guess < number:
            print("Your guess is too low!")
            attempts_rem_hard = attempts_rem_hard - 1
            print(f"You have {attempts_rem_hard} chances to guess the number")
        elif user_guess == number:
            print(
                f"Good job! You have guessed the {number} with {attempts_rem_hard} guesses remaining")
            game_over = True

    if user_guess != number and attempts_rem_hard == 0:
        print(f"Wrong guess.. You have used all your attempts to guess..")
        print(f"The actual number is {number}.")
        game_over = True


if difficulty_level == 'easy':
    game_easy()
else:
    game_hard()
