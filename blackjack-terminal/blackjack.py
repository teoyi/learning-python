# Python - BlackJack (Computer Dealer vs. Human Player)
import random

# GLOBAL VARIABLES
suits = ('Diamonds', 'Hearts', 'Clubs', 'Spades')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
card_count = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
playing = True
dealersturn = True

####################
### WELCOME NOTE ###
####################

def title():
    print('_______________________________________________________________________________')
    print('''
    Welcome to BlackJack Project!
    Aim to get a 21 or a value more than the dealer to win!

    HOW IT WORKS:
    1) The dealer will deal 2 cards each, the player will have it all faced up,
       while the dealer has one card faced down.
    2) Before each round, you will be asked to make a bet.
       Starting amount: 100 chips
    3) Player will be given a choice to hit or stay and player's turn will not end
       until stay is chosen (Aces counts as 1 or 11).
    4) Once the player choose to stay, it is the dealer's turn. The dealer will
       continue to hit as long as his value is less than 17!

    May lady luck smile upon you!''')
    print('_______________________________________________________________________________')

########################################
### CREATING CLASSES FOR GAME ENTITY ###
########################################

class Card():

    def __init__(self, suits, ranks):
        self.suits = suits
        self.ranks = ranks

    def __str__(self):
        return self.ranks + ' of ' + self.suits

class Deck():

    def __init__(self):
        self.allcards = []

        # TO GET ALL 52 UNIQUE CARDS
        for suit in suits:
            for rank in ranks:
                self.allcards.append(Card(suit,rank))

    # SHUFFLING DECK
    def shuffle(self):
        random.shuffle(self.allcards)

    # WHEN DEALING ONE CARD, REMOVES FROM DECK
    def deal_one(self):
        onecard = self.allcards.pop(0)
        return onecard

class Hand():

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_one(self, card):
        self.cards.append(card)
        self.value += card_count[card.ranks]
        if card.ranks == 'Ace':
            self.aces += 1

    def adjust_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Chips():

    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += int(self.bet)

    def lose_bet(self):
        self.total -= int(self.bet)


#######################################
### DEFINING FUNCTIONS FOR THE GAME ###
#######################################

# TAKING BETS FROM PLAYER
def bets(chips):

    betting = True
    print('\nYou currently have %s chips.' % chips.total)

    while betting:
        chips.bet = input('\nHow much would you like to bet?: ')
        if str(chips.bet).isdigit() == False:
            print('Sorry, that is an invalid value. Please try again!')
            continue
        else:
            if int(chips.bet) > chips.total:
                print('Sorry, you have insufficient funds!')
                reset = 'chicken'
                while reset.lower() != 'y' or reset.lower() != 'n':
                    reset = input('Would you like to reset your current balance? (Y or N): ')
                    if reset.lower() == 'y':
                        chips.total = 100
                        print('Your current balance is: %d' % chips.total)
                        break
                    elif reset.lower() == 'n':
                        break
                    else:
                        print('Sorry, that is an invalid input!')
                        continue
                continue
            else:
                print('Bet accepted!')
                break

# FUNCTION FOR HIT
# Called when a player requests for it or if a dealer's hand is < 17
def hit(deck, hand):

    dealt_card = deck.deal_one()
    hand.add_one(dealt_card)
    hand.adjust_ace

# FUNCTION FOR HIT OR STAND
def hit_or_stand(deck, hand):
    global playing

    while True:
        choice = input('\nWould you like to Hit or Stay? (Enter h or s): ')
        if choice == 'h':
            hit(deck, hand)
        elif choice == 's':
            print('\nPlayer Stands. Dealer is playing.')
            playing = False
        else:
            print('\nInvalid Entry, Please Try Again.')
            continue
        break

# FUNCTION TO DISPLAY CARDS
def show_some(player,dealer):
    print('_____________________________________')
    print("\nDealer's Hand:")
    print("<hidden>")
    print(dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep='\n')
    print('Player\'s current count is: ' + str(player.value))

def show_somemore(player,dealer):
    print('_____________________________________')
    print("\nDealer's Hand:")
    print("<hidden>")
    print(dealer.cards[1])
    print(dealer.cards[2])
    print("\nPlayer's Hand:", *player.cards, sep='\n')
    print('Player\'s current count is: ' + str(player.value))

def show_somemore2(player,dealer):
    print('_____________________________________')
    print("\nDealer's Hand:")
    print("<hidden>")
    print(dealer.cards[1])
    print(dealer.cards[2])
    print(dealer.cards[3])
    print("\nPlayer's Hand:", *player.cards, sep='\n')
    print('Player\'s current count is: ' + str(player.value))

def show_all(player,dealer):
    print('_____________________________________')
    print("\nDealer's Hand:", *dealer.cards, sep='\n')
    print("Dealer's Count =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n')
    print("Player's Count =",player.value)

# GAME MECHANICS FUNCTION
def player_busts(player, dealer, chips):
    print('\nPlayer BUSTS! Dealer WINS!')
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print('\nDealer BUSTS! Player WINS!')
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    print('\nDealer BUSTS! Player WINS!')
    chips.win_bet()

def dealer_wins(player, dealer, chips):
    print('\nPlayer BUSTS! Dealer WINS!')
    chips.lose_bet()

def push(player, dealer, chips):
    print('Dealer and Player Tie! It\'s a Push')



##################
### GAME LOGIC ###
##################


# WELCOME NOTE
title()

# Chips for player
player_chips = Chips()

while True:

    # TAKING BETS BEFORE ROUND BEGINS
    bets(player_chips)

    # START GAME

    # DECK SHUFFLING
    deck = Deck()
    deck.shuffle()

    # CREATING HAND FOR PLAYER AND DEALER
    player_hand = Hand()
    player_hand.add_one(deck.deal_one())
    player_hand.add_one(deck.deal_one())

    dealer_hand = Hand()
    dealer_hand.add_one(deck.deal_one())
    dealer_hand.add_one(deck.deal_one())

    show_some(player_hand, dealer_hand)

    # IMMEDIATE CHECK FOR 21
    if player_hand.value == 21:
        player_wins(player_hand, dealer_hand, player_chips)
    elif dealer_hand.value == 21:
        dealer_wins(player_hand, dealer_hand, player_chips)
    else:
        # PLAYER'S TURN
        while playing:

            hit_or_stand(deck, player_hand)
            show_some(player_hand, dealer_hand)

            if player_hand.value > 21:
                # print('\n              SHOW ALL!')
                # show_all(player_hand, dealer_hand)
                player_busts(player_hand, dealer_hand, player_chips)
                break
            elif player_hand.value == 21:
                player_wins(player_hand, dealer_hand, player_chips)
                break
            else:
                continue

    # DEALER'S TURN
    if player_hand.value < 21 and dealer_hand.value != 21:
        while dealersturn:

            if dealer_hand.value < 17:
                hit(deck, dealer_hand)
                if len(dealer_hand.cards) == 3:
                    show_somemore(player_hand, dealer_hand)
                elif len(dealer_hand.cards) == 4:
                    show_somemore2(player_hand, dealer_hand)
                continue

            # EXTRA CONDITION SUCH THAT IT WILL RECOGNIZE A BUST
            elif dealer_hand.value > 21:
                print('\n              SHOW ALL!')
                show_all(player_hand, dealer_hand)
                player_wins(player_hand, dealer_hand, player_chips)
                break

            else:
                # TAKE INTO ACCOUNT OF THE POSSIBLE RESULTS
                print('\n              SHOWDOWN!')
                show_all(player_hand, dealer_hand)
                if player_hand.value == dealer_hand.value:
                    push(player_hand, dealer_hand, player_chips)
                    break
                elif player_hand.value > dealer_hand.value:
                    player_wins(player_hand, dealer_hand, player_chips)
                    break
                elif player_hand.value < dealer_hand.value:
                    dealer_wins(player_hand, dealer_hand, player_chips)
                    break

    print('\nYour current standings are: %d chips.\n' % player_chips.total)
    while True:
        print('_____________________________________')
        restart = input('\nWould you like to continue? (Y or N): ')
        if restart.lower() == 'y':
            playing = True
            break
        elif restart.lower() == 'n':
            print('_____________________________________')
            print('\nThank you for playing! Have a good day!')
            print('\nExiting BlackJack Project...')
            print('\n')
            exit()
        else:
            print('Sorry, that is not a valid input, please try again!')
            continue
    continue
