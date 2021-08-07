# The Blackjack game

from art import logo
import random


def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card 


def calculate_score(cards):
    """Takes a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Game Draw!"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack!"
    elif user_score == 0:
        return "Win, with a Blackjack!"
    elif user_score > 21:
        return "You went over 21. You lose!"
    elif computer_score > 21:
        return "Opponent went over 21. You win!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose!"


def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False

    for i in range(0, 2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # for user to keep drawing cards
    while is_game_over == False:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input(
                "Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # computer should keep drawing cards until its score is less than 17
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(
        f"Computer's final hand: {computer_cards}, computer's final score: {computer_score}")

    # comparing both the total scores of cards drawn by both user and the computer
    print(compare(user_score, computer_score))


# to again restart a new game
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    play_game()
