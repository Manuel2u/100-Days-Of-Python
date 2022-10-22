from art import logo
import random
import os
start = input("Do You want to play a game of Blackjack? Type 'y' or 'n': ")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def clear():
    os.system('cls')


if start == "y":
    clear()
    print(logo)
    player = []
    dealer = []
    for i in range(2):
        player.append(random.choice(cards))
        dealer.append(random.choice(cards))
    print(f"Your cards: {player}, current score: {sum(player)}")
    print(f"Computer's first card: {dealer[0]}")

    if sum(player) == 21 and sum(dealer) == 21:
        print("Draw!")
    elif sum(player) == 21:
        print("You win!")
    elif sum(dealer) == 21:
        print("You lose!")
    elif sum(player) > 21:
        for player in player:
            if player == 11:
                player = 1
                if sum(player) < 21:
                    break
                else:
                    print("You lose!")
    else:
        hit = input("Type 'y' to get another card, type 'n' to pass: ")

        if hit == "y":
            player.append(random.choice(cards))
            print(f"Your cards: {player}, current score: {sum(player)}")
            print(f"Computer's first card: {dealer[0]}")
            if sum(player) == 21:
                print("You win!")
            elif sum(player) > 21:
                print("You lose!")
            else:
                hit = input("Type 'y' to get another card, type 'n' to pass: ")
                if hit == "y":
                    player.append(random.choice(cards))
                    print(
                        f"Your cards: {player}, current score: {sum(player)}")
                    print(f"Computer's first card: {dealer[0]}")
                    if sum(player) == 21:
                        print("You win!")
                    elif sum(player) > 21:
                        print("You lose!")
        else:
            dealer.append(random.choice(cards))
            print(f"Your final hand: {player}, final score: {sum(player)}")
            print(
                f"Computer's final hand: {dealer}, final score: {sum(dealer)}")
            if sum(dealer) == 21:
                print("You lose!")
            elif sum(dealer) > 21:
                print("You win!")
            elif sum(dealer) > sum(player):
                print("You lose!")
            elif sum(dealer) < sum(player):
                print("You win!")
            else:
                print("Draw!")

else:
    print("Bye!")
