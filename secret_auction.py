import os
import platform

from art import logo


def clear():
    return os.system("clear") if platform.system() in ['Linux', 'Darwin'] else os.system("cls")


clear()
new_auction = {}


def auction():
    clear()
    print(logo)
    name = input("Insert your name: ")
    bid = float(input("Insert your bid: $ "))
    new_auction[name] = bid  # stores a name as key and the bid as value
    return new_auction


def who_wins():
    # {"a": 123, "b": 321}
    highest_bid = 0
    winner = ""
    for bidder in new_auction:
        bid_amount = new_auction[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(
        f"The winner is: {winner.upper()}. With a bid of $ {highest_bid:.2f}.")


while True:
    end_auction = ""
    auction()
    end_auction = input("Are there other biders? Y or N: ").lower()
    if end_auction == "n":
        clear()
        break
clear()
print(logo)
who_wins()
