# -*- coding: utf-8 -*-


class Player:
    def __init__(self, name):
        self.hand = []
        self.name = name

    def take(self, card):
        """Take a card and place it in the hand"""
        self.hand.append(card)

    def show_hand(self):
        """Returns a string representing the player's hand"""
        result = ""
        for card in self.hand:
            result = result + card + " "
        return result


class Dealer:
    def __init__(self):
        self.hand = []
        self.deck = None
        self.reset()

    def reset(self):
        """Reset the deck."""
        self.deck = ["2S", "5H", "KD", "3S", "JH", "6C"]

    def deal(self, player):
        """Deals a card to the player"""
        card = self.deck.pop()
        player.take(card)


class Board:
    def __init__(self):
        self.jack = Dealer()
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def display(self):
        """Display the status of the Board"""
        print("List of player's hand")
        for player in self.players:
            # hand_representation = player.show_hand()
            # print("{} hand: {}".format(player.name, hand_representation))
            print(f"{player.name}'s hand: {player.show_hand()}")


if __name__ == '__main__':
    board = Board()
    scott = Player("Scott")
    bethany = Player("Bethany")

    board.add_player(scott)
    board.add_player(bethany)

    jack = board.jack
    jack.deal(scott)
    jack.deal(bethany)
    board.display()