import random


def random_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def compare(computer_score,user_score):
    if computer_score>21 and user_score>21:
        return "You lose. You went over 21."
    elif computer_score == user_score:
        return "It's a draw."
    elif computer_score == 0:
        return "You lose. Computer got a blackjack."
    elif user_score == 0:
        return "Congrats. You won and You got a BlackJack."
    elif computer_score>21:
        return "You Won."
    elif user_score>21:
        return "You lose."
    elif computer_score > user_score:
        return "You lose."
    else:
        return "You Won."


def calculate_score(player_cards):
    if 11 in player_cards and sum(player_cards)>21:
        player_cards.remove(11)
        player_cards.append(1)

    if 11 in player_cards and 10 in player_cards and len(player_cards):
        return 0

    return sum(player_cards)


computer_cards = []
user_cards = []

for _ in range(2):
    computer_cards.append(random_card())
    user_cards.append(random_card())

computer_score = calculate_score(computer_cards)
user_score = calculate_score(user_cards)

isGameOver = False

while not isGameOver:
    print(f"Your Score: {user_score}. Your cards: {user_cards}.")
    print(f"Computer's first Card: {computer_cards[0]}.")

    if computer_score == 0 or user_score== 0 or user_score>21:
        isGameOver = True
    else:
        user_choice = input("Do you want to draw another card? If yes then press 'y' else press'n'. ")
        if user_choice == 'y':
            user_cards.append(random_card())
            user_score = calculate_score(user_cards)
        else:
            isGameOver = True

while computer_score != 0 and computer_score<17:
    computer_cards.append(random_card())
    computer_score = calculate_score(computer_cards)

print(f"Computer's Cards: {computer_cards}. Computer's Final score: {computer_score}.")
print(f"Your cards: {user_cards}. Your final score: {user_score}.")
print(compare(computer_score,user_score))