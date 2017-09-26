# Global section begins


from collections import namedtuple
from itertools import product
from unicards import unicard
import random


Card = namedtuple("Card", "name, suite")
names = ['a','2','3','4','5','6','7','8','9','10','k','q','j']
suites = ['Heart', 'Spade', 'Diamond', 'Club']
scoring = dict(zip(names,
         [11,2,3,4,5,6,7,8,9,10,10,10, 10]))

"""  Start of Defining Objects  """


class Player(object):
    def __init__(self, chips, name):
        self.chips = chips
        self.name = name
        self.bet = 0
        self.hand = []
        self.score = 0
        

    def display_hand(self):
        for card in self.hand:
            
            print(unicard(card.name + card.suite[0], color=True), end=' ')
        
        print()
            

class Dealer(Player):
    def __init__(self):
        super().__init__(chips=0, name='Dealer')
        

class BlackJackTable(object):
    def __init__(self):
        self.deck = self.get_new_deck()   
        self.dealer = Dealer()
        self.players = []

    def get_new_deck(self):
        deck = [Card(name, suite) for name, suite in product(names, suites)]
        random.shuffle(deck)
        return deck
    
    def deal_cards(self, player, how_many=1):
        
        for _ in range(how_many):
            card = self.deck.pop()
            player.hand.append(card)
    
    def add_player(self, player):
        self.players.append(player)
    
    def remove_player(self, player):
        self.players.pop(player)
    
    
    def calc_score(self, hand):
        
        total = sum(scoring[card.name] for card in hand if card.name !='a') 
        aces = len([card.name for card in hand if card.name == 'a'])
        
        if total < 10 :
            total += 11 + aces - 1
        
        elif total == 10 and aces == 1:
            total += 11
        
        elif total == 10 and aces > 1:
            total += aces
            
        else:
            total += aces
            
        return total
    
        #iterate throught hand, looking up value (filter out Ace)
        #sum values
        #test for limit, if over then A =1
        #return total
    
    
    def run_game(self):
        
        participants = self.players[:]
        participants.append(self.dealer)
        
        for player in self.players:
            self.take_bet(player)
    
        for participant in participants:
            self.deal_cards(participant, how_many=2)
        
        for participant in participants:
            participant.score = self.calc_score(participant.hand)
            
            #print(participant.name, participant.score)

            participant.display_hand()
        
        #Dealer goes last, and his hand is partially obscured (only 1st card is turned over)
        #take bets
        #dealer deals cards
        #score calc
        #board display
        #final tally
        #exit
    
    
    def take_bet(self, player):
        print('%s currently has %s chips' % (player.name, player.chips))
        while True:
            try:
                playerwager = int(input('Ok %s, so how much do you want to wager '
                                        'on this hand of blackjack? ' % (player.name)))
            except ValueError:
                print('Seriously?  You cannot type a number?  Try again!')
                continue
            
            if playerwager > player.chips or playerwager < 1:
                print('No you cannot bet a negative amount and yes it must be '
                      'less or equal to your chip balance.  Try again!')
                continue
            
            player.bet = playerwager
            break    
     
    '''    
    def display_board(self):
        # First need to calc the new info
        if whoseturn == playername:
            self.p1 = self.phand[0]
            self.p2 = self.phand[1]
            self.p3 = self.phand[2]
            self.p4 = self.phand[3]
            self.p5 = self.phand[4]
            self.pscore = deckdef.get(self.p1) + deckdef.get(self.p2) + deckdef.get(self.p3) + deckdef.get(
                self.p4) + deckdef.get(self.p5)
            self.dscore = deckdef.get(self.d1)

        elif whoseturn == 'Dealer':
            self.d1 = self.dhand[0]
            self.d2 = self.dhand[1]
            self.d3 = self.dhand[2]
            self.d4 = self.dhand[3]
            self.d5 = self.dhand[4]
            self.dscore = deckdef.get(self.d1) + deckdef.get(self.d2) + deckdef.get(self.d3) + deckdef.get(
                self.d4) + deckdef.get(self.d5)
        # End of Calc

        # Now print board
        print('')
        print('')
        print('                  |   Cards           | Score |')
        print('-------------------------------------------------------')
        print('| Dealer          | %s | %s | %s | %s | %s | %s  ' % (b.d1, b.d2, b.d3, b.d4, b.d5, b.dscore))
        print('-------------------------------------------------------')
        print('| %s| %s | %s | %s | %s | %s | %s     ' % (paddedname, b.p1, b.p2, b.p3, b.p4, b.p5, b.pscore))
        print('-------------------------------------------------------')
        print('')
        print('Your bet is %s.  Your chipcount before bet was %s' % (playerwager, playerbalance))
        print('')
        print("Currently it is %s's turn" % (whoseturn))
        print('')

    def hit_player(self):
        card = random.choice(self.deck)
        self.deck.remove(card)
        if self.phand[0] == '__':
            self.phand[0] = card
        elif self.phand[1] == '__':
            self.phand[1] = card
        elif self.phand[2] == '__':
            self.phand[2] = card
        elif self.phand[3] == '__':
            self.phand[3] = card
        elif self.phand[4] == '__':
            self.phand[4] = card

    def hit_dealer(self):
        card = random.choice(self.deck)
        self.deck.remove(card)
        if self.dhand[0] == '__':
            self.dhand[0] = card
        elif self.dhand[1] == '__':
            self.dhand[1] = card
        elif self.dhand[2] == '__':
            self.dhand[2] = card
        elif self.dhand[3] == '__':
            self.dhand[3] = card
        elif self.dhand[4] == '__':
            self.dhand[4] = card

# This is a global function that helps pad filling to keep grid of board clean
def pad(str1, fullLength):
    """
    Parameter 1: str1 is variable you want to pad with spaces for printing
    Parameter 2: fullLength is a integer to define the full length you want printed
    OUTPUT: Str1 plus necessary spaces to get to the fullLength
    """
    return str1 + (" " * (fullLength - (len(str1))))

def scott(): 
    """ Start of create Class instances """
    p = Player()
    b = Board()
    
    # Application Opens
    print("Welcome to Scooter's Casino BlackJack Table \n")
    playername = input("What is your name? ")[:10]
    print('Fantastic to have you %s !!!' %(playername))
    p.set_name(playername)
    
    paddedname = pad(playername, 16)
    
    isgameover = 'N' #This variable controls when the over all game is to be ended.
    
    while isgameover!= 'Y':
        try:
            playerbalance = int(input('How much money do you have to chip up? '))
        except ValueError:
            print('Look you ding dong. A whole number!  Try again.')
            continue
        if playerbalance < 0:
            continue
        else:
            p.set_chips(playerbalance)
            break
    
    print('')
    print('--------------------------------------')
    print('')
    
    playagain = '' # This variable controls playing another hand.
    
    while playagain != 'N':
        gamenumber += gamenumber
        print('you currently have %s chips' % (p.chips))
        try:
            playerwager = int(input('Ok, so how much do you want to wager on this hand of blackjack? '))
        except ValueError:
            print('Seriously?  You cannot type a number?  Try again!')
            continue
        if playerwager > playerbalance or playerwager < 0:
            print('No you cannot bet negative amount and yes it must less or equal to your chip balance.  Try again!')
            continue
        else:
            p.set_bet(playerwager)
            break
    
    """ End of create Class instances """
    
    # Now we have the initial balance and the players name so we can get the first wager.
    # This is the loop below that will allow us to player additional hands with this player33333
    while 'True':
        whoseturn = playername  # This just resets the turn to the player each time a new hand is dealt
        """
        Lets deal the first two cards to dealer and player
        """
        b.hit_dealer()
        b.hit_dealer()
        b.hit_player()
        b.hit_player()
    
        b.d1 = b.dhand[0]
        b.d2 = '__'
        b.get_board()
    
        while whoseturn == playername:
            if b.pscore < 21:
                print('Your current score is ', b.pscore)
                hitOrstick = str(input('What would you like to do? (H)it or (S)tick? '))
                if hitOrstick != 'H' and hitOrstick != 'S':
                    print('Do not be a dummy.  Press H or S for your choice then press Enter key.')
                elif hitOrstick == 'H':
                    b.hit_player()
                    b.get_board()
                    hitOrstick = ' '
                elif hitOrstick == 'S':
                    print('You chosen to stick at ', b.pscore)
                    print('It is now the dealers turn.')
                    whoseturn = 'Dealer'
                    break
            elif b.pscore == 21:
                print('You have hit 21 !!! Blackjack!  Well done.')
                print('The dealer can only tie you so you cannot lose.')
                print('It is now the dealers turn.')
                whoseturn = 'Dealer'
                hitOrstick = ' '
                break
            elif b.pscore > 21:
                print('You have busted with a score of ', b.pscore)
                print('You lost your bet of ' + str(p.bet) + 'chips.')
                print('Your remaining chip balance is ' + str(playerbalance - p.bet) + 'chips.')
                print('')
                playagain = str(input('Would you like to play again? [Y]es or [N]o'))
                break
            break
    
        while whoseturn == 'Dealer':
            print('Now it is the dealers turn.  He must beat or tie ', b.pscore)
            print('Press the G key then enter button for dealer to deal his next card: ')
            dealerhit = input(':')
            b.get_board()
            if dealerhit == 'G':
                b.hit_dealer()
                b.get_board()
                dealerhit = ' '
            else:
                whoseturn = 'End of Game'
                break
    
    print('Thank you for playing.')
    
'''

def chip_up(player):    
    while True: 
        try:
            playerbalance = int(input('How much money do you have to chip up?'))
        except ValueError:
            print('Look you ding dong. A whole number!  Try again.')
            continue
        if playerbalance < 0:
            continue
        else:
            player.chips= playerbalance

        



if __name__ == '__main__':
    table = BlackJackTable()
    player = Player(chips=100, name='BG')

    table.add_player(player)
    
    table.run_game()