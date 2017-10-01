clubs = {'2C':2,'3C':3,'4C':4,'5C':5,'6C':6,'7C':7,'8C':8,'9C':9,'10C':10,'JC':10,'QC':10,'KC':10,'AC':11}
diamonds = {'2D':2,'3D':3,'4D':4,'5D':5,'6D':6,'7D':7,'8D':8,'9D':9,'10D':10,'JD':10,'QD':10,'KD':10,'AD':11}
hearts = {'2H':2,'3H':3,'4H':4,'5H':5,'6H':6,'7H':7,'8H':8,'9H':9,'10H':10,'JH':10,'QH':10,'KH':10,'AH':11}
spades = {'2S':2,'3S':3,'4S':4,'5S':5,'6S':6,'7S':7,'8S':8,'9S':9,'10S':10,'JS':10,'QS':10,'KS':10,'AS':11}
deckdef = {**clubs, **hearts, **spades, **diamonds}
curdeck = set()

for key in deckdef.keys():
    curdeck.add(key)

print("Welcome to Scooter's Casino BlackJack Table \n")
playername = input("What is your name sucker.. eh .. I mean player? ")
print('Fantastic to have you %s !!!'%(playername))
while True:
    try:
        playerbalance=int(input('How much money do you have to chip up? '))
    except ValueError:
        print('Look you ding dong. A whole number!  Try again.')
        continue
    else:
        if playerbalance < 0:
            continue
        else:
            break
        break

while True:
    print('')
    print('--------------------------------------')
    print('')
    print('you currently have %s chips'%(playerbalance))    
    while True:
            try:
                playerwager=int(input('Ok, so how much do you want to wager on this hand of blackjack? \n Me vs You punk! '))
            except ValueError:
                print('Seriously?  You cannot type a number?  Try again!')
                continue
            if playerwager > playerbalance or playerwager < 0:
                print('No you cannot bet negative amount and yes it must less or equal to your chip balance.  Try again!')
                continue
            else:
                break
    break        
    
while 'True':
    
    whoseturn = playername
    
    class Dealer(object):
        def __init__(self):
            self.deck=curdeck
            self.hand=set()
            self.score = score
            
        def hitplayer():
            pass 
                 
    class Player(object):
        def __init__(self,chips,name):
            self.chips = chips
            self.name = name
            self.bet = bet
            self.hand = set()
            self.score = score

        def set_bet():
            pass
        
        def set_stick():
            pass
        
    class Board(object):
        def __init__(self):
            self.d1 = d1
            self.d2 = d2
            self.d3 = d3
            self.d4 = d4
            self.d5 = d5
            self.dscore = dscore
            self.p1 = p1
            self.p2 = p2
            self.p3 = p3
            self.p4 = p4
            self.p5 = p5
            self.pscore = pscore
    
        def get_board():
            print('             |   Cards                | Score |')
            print('-----------------------------------------------')
            print('| Dealer     | %s | %s | %s | %s | %s | %s    |' %(self.d1,self.d2,self.d3,self.d4,self.d5,self.dscore))
            print('-----------------------------------------------')
            print('| Player1    | %s | %s | %s | %s | %s | %s    |' %(self.p1,self.p2,self.p3,self.p4,self.p5,self.pscore))
            print('-----------------------------------------------')
            print('')
            print('Your bet is %s.  Your chipcount before bet was %s'%(playerbalance))
            print("Currently it is %s's turn"(whoseturn))
    """
                 | Cards                  | Score |
    -----------------------------------------------
    | Dealer     |    |    |    |    |    |       |
    -----------------------------------------------
    | Player1    |    |    |    |    |    |       |
    -----------------------------------------------
    What would you like to do? (H)it or (S)tick? 
    (Results Varable)
    
    """