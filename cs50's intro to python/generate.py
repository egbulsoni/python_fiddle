import random  # imports everything from random
# from random import choice  # import the name of the function

cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)

# number = random.randint(1, 10)  # includes both starting and ending
# print(number)

# coin = choice(["heads", "tails"])
# print(coin)
