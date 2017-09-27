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

#If we were making more than blackjack, should we consider an abstract *participant*
#class with Player and Dealer inheriting from it?
class Player(object):
    def __init__(self, chips, name):
        self.chips = chips
        self.name = name
        self.bet = 0
        self.hand = []
        self.score = 0
        
    #Three implementations, here - each has different issues displaying
    #Do we want to move printing Player name here, or is that something 
    #only calc score does?
    
    def display_hand(self):
        for card in self.hand:
            
            # 1: using unicards lib
            print(unicard(card.name + card.suite[0], color=True), end=' ')
            
            
            # 2: using unicode symbols for Suite
            unicode_suites = {'Diamond':'\u2662', 'Spade':'\u2660','Heart':'\u2661', 'Club':'\u2663'}
            print(card.name.upper() + unicode_suites[card.suite], end=' ')
            
            
            # 3: simple name display (has layout implications)
            print(card.name.upper() + ' of ' + card.suite + 's', end= ' ')
            
        print()

            
#The Dealer here is a specialized sort of player that doesn't have chips or a name.
#Dealer's __init__ explicitly calls Player's __init__ with the specific parameters
#set....this could also be done by simply calling player, but the rules of play
#for the dealer are different, so we've made a seperate class.
class Dealer(Player):
    def __init__(self):
        super().__init__(chips=0, name='Dealer')



        
#This is a compairativley large class - should it be broken up?
class BlackJackTable(object):
    def __init__(self):
        self.deck = self.get_new_deck()   
        self.dealer = Dealer()
        self.players = []

    def get_new_deck(self):
        deck = [Card(name, suite) for name, suite in product(names, suites)]
        random.shuffle(deck)
        return deck
    
    
    def add_player(self, player):
        self.players.append(player)
    
    
    def remove_player(self, player):
        self.players.pop(player)
    
    
    def deal_cards(self, player, how_many=1):
        
        for _ in range(how_many):
            card = self.deck.pop()
            player.hand.append(card)
    
    
    def hit_player(self, player):
        card = self.deck.pop()
        player.hand.append(card)
    
    
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
    
    #The logic here still needs work.  Specifically, the case where the total
    #is 9, and the player has 3 aces....
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
        
        ####
        
        #if any player loss is > than their chip balance, they go bust
        #players going bust should be removed from the player list.
        #does that logic belong here...or elsewhere??
    
    
    def get_board():
        pass
    
    
    
    def run_game(self):
        
        participants = self.players[:]
        participants.append(self.dealer) 
        
        for player in self.players:
            self.take_bet(player)
    
        for participant in participants:
            self.deal_cards(participant, how_many=2)
        
        
        #Display initial board here??
        
        
        #While loop here??
        for player in self.players:
            player.score = self.calc_score(player.hand)
            
            #need additional while loop here if we have more than one player &
            #want to do checks on input...
            if player.score < 21:
                
                hitOrStick = ''
                
                while hitOrStick not in ('H' or 'S'):
                    print('%s, your current score is: ' %(player.name), player.score)
                    hitOrStick = str(input('What would you like to do? (H)it or (S)tick? '))
                
                    if hitOrStick not in ('H','S'):
                        print('Do not be a dummy.  Press H or S for your choice then press Enter key.')
                    
                    if hitOrStick == 'H':
                        hit_player(player)
                        player.display_hand()
                        
                    if hitOrstick == 'S':
                        player.display_hand()
                        print("%s, you've chosen to stick at: " %(player.name), player.score)

            elif player.score == 21:
                print('You have hit 21, %s !!! Blackjack!  Well done.' %(player.name))
                player.display_hand(player)
                
                print('The dealer can only tie you so you cannot lose.')
  
            
            elif player.score > 21:
                print("%s, you've busted with a score of: " %(player.name), player.score)
                print("You've lost your bet of " + str(player.bet) + ' chips.')
                
                player.chips = player.chips - player.bet
                
                print('Your remaining chip balance is: ' + str(player.chips) + ' chips.')
       
        display_board()
        print("Now it's the dealers turn.")

            

            #Dealer goes last, and his hand is partially obscured (only 1st card is turned over)
            #take bets
            #dealer deals cards
            #score calc for players
            #board display
            #final tally
            #exit
    

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
    
###########################
        
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


###############
#Main Game Loop or Class would go Here...

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
            player.chips = playerbalance
            break


#does thois go here..or in the table class??  
#Feels like it really belongs in a utility class....        
def display_board(player, dealer):
    pass

#don't even know if this is needed, but it does change display and scoring...
#Dealer goes last, so there are two different turn 'modes'.
def turn():
    pass


#Main code entry point - current code is here for testing, but this would
#ultimatley be in the main game loop, and this would just call that loop/class...            
if __name__ == '__main__':
    # Application Opens
    print("Welcome to Scooter's Casino BlackJack Table \n")
    
    #this would be a for loop if there were n players.....
    new_player = Player(chips=0, name=input("What is your name? ")[:10])
    
    print('Fantastic to have you %s !!!' %(new_player.name))

    chip_up(new_player)
    
    table = BlackJackTable()
    
    #another for loop if there were n players added...
    table.add_player(new_player)
    
    print(new_player.name)
    print(new_player.chips)
    
    table.run_game()
    



    
#Code yet to be re-organized.  
########################################################################     
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
