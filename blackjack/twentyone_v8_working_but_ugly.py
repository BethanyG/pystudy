# Global section begins

clubs = {'2' + '\u2663': 2, '3' + '\u2663': 3, '4' + '\u2663': 4, '5' + '\u2663': 5, '6' + '\u2663': 6,
         '7' + '\u2663': 7, '8' + '\u2663': 8, '9' + '\u2663': 9, '10' + '\u2663': 10, 'J' + '\u2663': 10,
         'Q' + '\u2663': 10, 'K' + '\u2663': 10, 'A' + '\u2663': 11}
diamonds = {'2' + '\u2662': 2, '3' + '\u2662': 3, '4' + '\u2662': 4, '5' + '\u2662': 5, '6' + '\u2662': 6,
            '7' + '\u2662': 7, '8' + '\u2662': 8, '9' + '\u2662': 9, '10' + '\u2662': 10, 'J' + '\u2662': 10,
            'Q' + '\u2662': 10, 'K' + '\u2662': 10, 'A' + '\u2662': 11}
hearts = {'2' + '\u2661': 2, '3' + '\u2661': 3, '4' + '\u2661': 4, '5' + '\u2661': 5, '6' + '\u2661': 6,
          '7' + '\u2661': 7, '8' + '\u2661': 8, '9' + '\u2661': 9, '10' + '\u2661': 10, 'J' + '\u2661': 10,
          'Q' + '\u2661': 10, 'K' + '\u2661': 10, 'A' + '\u2661': 11}
spades = {'2' + '\u2660': 2, '3' + '\u2660': 3, '4' + '\u2660': 4, '5' + '\u2660': 5, '6' + '\u2660': 6,
          '7' + '\u2660': 7, '8' + '\u2660': 8, '9' + '\u2660': 9, '10' + '\u2660': 10, 'J' + '\u2660': 10,
          'Q' + '\u2660': 10, 'K' + '\u2660': 10, 'A' + '\u2660': 11}
deckdef = {**clubs, **hearts, **spades, **diamonds}
import random

gamenumber = 0
standarddeck = []

for zerokey in deckdef.keys():  # This section creates the standarddeck variable from the initial deckdef keys
    standarddeck.append(zerokey)

deckdef.update({'__': 0})  # This adds a dictionary item for '__' with 0 as value to deckdef for score calc
"""  Start of Defining Objects  """

class Player(object):
    def __init__(self):
        self.chips = 0
        self.name = ''
        self.bet = 0

    def set_bet(self, betamt):
        self.bet = betamt

    def set_chips(self,chipamt):
        self.chips = chipamt

    def set_name(self,plname):
        self.name = plname
        
    def set_reward(self,bet,win_loss_tie):
        if win_loss_tie == 'W':
            self.chips = self.bet + self.chips
        elif win_loss_tie == 'L':
            self.chips = self.chips - self.bet
        elif win_loss_tie == 'T':
            pass
    def show_bet(self):
        print('Your bet is %s.  Your chipcount before bet was %s' % (self.bet, self.chips))
        print('')
        print("Currently it is %s's turn" % (whoseturn))
        print('')

class Board(object):
    def __init__(self, d1='__', d2='__', d3='__', d4='__', d5='__', dscore=0, p1='__', p2='__', p3='__', p4='__',
                 p5='__', pscore=0, dhand=['__', '__', '__', '__', '__'], phand=['__', '__', '__', '__', '__'],
                 deck=standarddeck[:]):
        self.d1 = d1
        self.d2 = d2
        self.d3 = d3
        self.d4 = d4
        self.d5 = d5
        self.dhand = dhand
        self.dscore = dscore
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
        self.p5 = p5
        self.phand = phand
        self.pscore = pscore
        self.deck = deck
                

    def get_board(self):
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
            for card in self.phand:
                if card[0] == 'A' and self.pscore > 21:
                    self.pscore = self.pscore - 10

        elif whoseturn == 'Dealer':
            self.d1 = self.dhand[0]
            self.d2 = self.dhand[1]
            self.d3 = self.dhand[2]
            self.d4 = self.dhand[3]
            self.d5 = self.dhand[4]
            self.dscore = deckdef.get(self.d1) + deckdef.get(self.d2) + deckdef.get(self.d3) + deckdef.get(
            self.d4) + deckdef.get(self.d5)
            for card in self.dhand:
                if card[0] == 'A' and self.dscore > 21:
                    self.dscore = self.dscore - 10
         # End of Calc       

        # Now print board
        clearme()
        print('')
        print('')
        print('                  |   Cards           | Score |')
        print('-------------------------------------------------------')
        print('| Dealer          | %s | %s | %s | %s | %s | %s  ' % (self.d1, self.d2, self.d3, self.d4, self.d5, self.dscore))
        print('-------------------------------------------------------')
        print('| %s| %s | %s | %s | %s | %s | %s     ' % (paddedname, self.p1, self.p2, self.p3, self.p4, self.p5, self.pscore))
        print('-------------------------------------------------------')
        print('')
        print('The number of cards in deck is %s' %len(self.deck))
        print('The number of cards in standarddeck is %s' % len(standarddeck))
        p.show_bet()
        
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

    ##def __del__(self): # This deletes the board object "b" so it can be refreshed for next hand.
    def reset_board(self):
        self.d1='__'
        self.d2='__'
        self.d3='__'
        self.d4='__'
        self.d5='__'
        self.dscore=0
        self.p1='__'
        self.p2='__'
        self.p3='__'
        self.p4='__'
        self.p5='__'
        self.pscore=0
        self.dhand=['__', '__', '__', '__', '__']
        self.phand=['__', '__', '__', '__', '__']
        #self.deck=[]
        #print('after deck emptied %s ' %(len(self.deck)))
        self.deck=standarddeck[:]
        #print('after deck copied from standarddeck %s ' %(len(self.deck)))
        print('Deck shuffled.  Table cleared.')

def clearme():
    """
    This is just a function to be called to clear the screen so player is not seeing previous board
    OUTPUT: 50  blank lines making it appears as though it is a clear screen
    """
    return print('\n'*50)

# This is a global function that helps pad filling to keep grid of board clean
def pad(str1, fullLength):
    """
    Parameter 1: str1 is variable you want to pad with spaces for printing
    Parameter 2: fullLength is a integer to define the full length you want printed
    OUTPUT: Str1 plus necessary spaces to get to the fullLength
    """
    return str1 + (" " * (fullLength - (len(str1))))

""" Start of create Class instances """
p = Player()
b = Board()

# Application Opens
print("Welcome to Scooter's Casino BlackJack Table \n")
playername = input("What is your name? ")[:10]
print('Fantastic to have you %s !!!' %(playername))
p.set_name(playername)

paddedname = pad(playername, 16)


while True:
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

keepplayin = 'Y'

b.reset_board()

while keepplayin != 'N':  #This is the outer most loop that allows multiple hands
    gamenumber += 1

    while True: #This loop runs once for every hand to be played
        print('you currently have %s chips' % (p.chips))
        try:
            playerwager = int(input('Ok, so how much do you want to wager on this hand of blackjack? '))
        except ValueError:
            print('Seriously?  You cannot type a number?  Try again!')
            continue
        if playerwager > p.chips or playerwager < 0:
            print('No you cannot bet negative amount and yes it must less or equal to your chip balance.  Try again!')
            continue
        else:
            p.set_bet(playerwager)
            break
    ######## This ends the Get Wager loop
            
    whoseturn = playername  # This just resets the turn to the player each time a new hand is dealt
    # Lets deal the first two cards to dealer and player
    b.hit_dealer()
    b.hit_dealer()
    b.hit_player()
    b.hit_player()

    b.d1 = b.dhand[0]
    b.d2 = '__' # The second card will show as '__' until dealers turn

    """ Lets get the initial board and calculate the scores """
    b.get_board()

    while whoseturn == playername:
        if b.pscore < 21:
            print('Your current score is ', b.pscore)
            hitOrstick = str(input('What would you like to do? (H)it or (S)tick? '))
            if hitOrstick.upper() != 'H' and hitOrstick.upper() != 'S':
                print('Do not be a dummy.  Press H or S for your choice then press Enter key.')
            elif hitOrstick.upper() == 'H':
                b.hit_player()
                b.get_board()
                hitOrstick = ' '
            elif hitOrstick.upper() == 'S':
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
        elif b.pscore > 21:
            print('You have busted with a score of %s ' %(b.pscore))
            print('You lost %s chips. Your new chip balance is %s' %(p.bet,p.chips - p.bet))
            p.set_reward(p.bet,'L')
            print('')
            playagain = str(input('Would you like to play again? [Y]es or [N]o'))
            if playagain.upper() == 'Y':
                b.reset_board()
                whoseturn = "New Game"
                break
            else:
                keepplayin = 'N' #should end game play
                break
                                
    while whoseturn == 'Dealer':
        # See if dealer has winning hand or is 16 or higher
        b.get_board()
        if b.dscore >= 16 and b.pscore < b.dscore and b.dscore < 22:
            print('Dealer wins with score of %s to players %s. DEALER WINS' %(b.dscore,b.pscore))
            print('You lost %s chips. Your new chip balance is %s' %(p.bet,p.chips - p.bet))
            p.set_reward(p.bet,'L')
            playagain = str(input('Would you like to play again? [Y]es or [N]o'))
            if playagain.upper() == 'Y':
                b.reset_board()
                whoseturn = "New Game"
                break
            else:
                keepplayin = 'N' #should end game play
                break
        elif b.dscore >= 16 and b.pscore > b.dscore:
            print('Player wins with score of %s to players %s. PLAYER WINS' %(b.dscore,b.pscore))
            print('You WON %s chips. Your new chip balance is %s' %(p.bet,p.chips + p.bet))
            p.set_reward(p.bet,'W')
            playagain = str(input('Would you like to play again? [Y]es or [N]o'))
            if playagain.upper() == 'Y':
                b.reset_board()
                whoseturn = "New Game"
                break
            else:
                keepplayin = 'N' #should end game play
                break
        elif b.dscore >= 16 and b.pscore == b.dscore:
            print('Dealer ties with score of %s to players %s. IT IS A TIE' %(b.dscore,b.pscore))
            print('The wager is is a push since no hand won.')
            playagain = str(input('Would you like to play again? [Y]es or [N]o'))
            if playagain.upper() == 'Y':
                b.reset_board()
                whoseturn = "New Game"
                break
            else:
                keepplayin = 'N' #should end game play
                break
        elif b.dscore > 21:
            print('Dealer busts with score of %s to players %s. PLAYER WINS' %(b.dscore,b.pscore))
            print('You WON %s chips. Your new chip balance is %s' %(p.bet,p.chips + p.bet))
            p.set_reward(p.bet,'W')
            playagain = str(input('Would you like to play again? [Y]es or [N]o'))
            if playagain.upper() == 'Y':
                b.reset_board()
                whoseturn = "New Game"
                break
            else:
                keepplayin = 'N' #should end game play
                break
        else:
            print('Now it is the dealers turn.  He must beat or tie ', b.pscore)
            print('Press the G key then enter button for dealer to deal his next card: ')
        
            dealerhit = input(':')
            b.get_board()
            if dealerhit.upper() == 'G':
                b.hit_dealer()
                b.get_board()
                dealerhit = ' '
            else:
                continue
    
print('Thank you for playing.')