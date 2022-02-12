import random

class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
def card_init():
    suit = ['Clubs', 'Spades', 'Diamonds', 'Hearts']
    rank = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']
    cards = []
    for i in suit:
        for j in rank:
            card = Card(i, j)
            cards.append(card)
    return cards

def shuffule_and_print(cards):
    random.shuffle(cards)
    for card in cards:
        print(f"{card.rank} of {card.suit}")

if __name__ == "__main__":
    cards = card_init()
    shuffule_and_print(cards)
