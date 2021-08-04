# Hangman Game
import random
import hangman_words
import hangman_art

print(hangman_art.logo)
# from hangman_art import logo
# print(logo)
#word_list = ['grapes', 'orange', 'apple', 'mango']

chosen = random.randint(0, 3)
chosen_word = hangman_words.word_list[chosen]
# print(chosen_word)

display = []
for word_length in range(0, len(chosen_word)):
    display.append("---",)
print(display)

game_ended = False
lives = 6
while(game_ended == False):
    guess = input("Enter a letter to guess: ")
    guess_word = guess.lower()

    # if the user has entered a letter they have already guessed, print the letter and let them know
    if guess_word in display:
        print(f"You've already guessed {guess_word}")

    for position in range(0, len(chosen_word)):
        letter = chosen_word[position]
        if guess_word in letter:
            display[position] = letter

    print(display)
    if guess_word not in chosen_word:
        print(
            f"You guessed {guess_word}, that's not in the word. You lose a life!")
        lives = lives - 1
        if(lives == 0):
            game_ended = True
            print("You lose!")

    if '---' not in display and lives != 0:
        game_ended = True
        print("You Win!")

# printing the ascii art from 'stages' that corresponds to current no. of lives user has remaining
print(hangman_art.stages[lives])
