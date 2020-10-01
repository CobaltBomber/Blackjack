import random

class Card:
    """Card class for representing and manipulating one playing card"""

    def __init__(self, rank, suit):
        """A constructor method that sets the suit and rank"""
        self.suit = suit
        self.rank = rank

    def __str__(self):
        """Overrides the information used by the print function"""
        return "The " + self.rank + " of " + self.suit

    def get_suit(self):
        """A reader method that returns the suit of the card"""
        return self.suit

    def get_rank(self):
        """A reader method that returns the rank of the card"""
        return self.rank

# -----------------------------------------------------

class Deck:
    """Deck class for representing and manipulating 52 instances of Card"""

    def __init__(self):
        """A constructor method that creates a 52 card deck"""
        self.cards = []
        for rank in ["two", "three", "four", "five", "six", "seven", "eight",
                     "nine", "ten", "jack", "queen", "king", "ace"]:
            for suit in ["clubs", "diamonds", "hearts", "spades"]:
                self.cards += [Card(rank,suit)]

    def __str__(self):
        """A method that prints the 52 card deck and prints the string version"""
        answer = "Deck of Cards\n"
        answer += "-------------\n"
        number = 1 
        for card in self.cards:
            answer += str(number) + " " + str(card) + "\n"
            number += 1
        return answer

    def shuffle(self):
        random.shuffle(self.cards)
            
            
# -----------------------------------------------------

def main():
    cards = Deck()
    print(cards)

    cards.shuffle()
    print("After shuffling...\n")
    print(cards)

#-----------------------------------------------------

main()
