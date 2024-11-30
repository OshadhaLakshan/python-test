import random

cards = ["jack", "king", "queen", "ace"]
random.shuffle(cards)
print(random.choice(cards))
for card in cards:
    print(card, end=', ')