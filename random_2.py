import random

cards = ["jack", "king", "queen", "ace"]
random.shuffle(cards)
for card in cards:
    print(card, end=', ')