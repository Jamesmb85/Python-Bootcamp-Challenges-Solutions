# Milestone Project 2 - Walkthrough Steps Workbook
#
# Below is a set of steps for you to follow to try to create the Blackjack Milestone Project game!
# Game Play
#
# To play a hand of Blackjack the following steps must be followed:
#
# 1. Create a deck of 52 cards
# 2. Shuffle the deck
# 3. Ask the Player for their bet
# 4. Make sure that the Player's bet does not exceed their available chips
# 5. Deal two cards to the Dealer and two cards to the Player
# 6. Show only one of the Dealer's cards, the other remains hidden
# 7. Show both of the Player's cards
# 8. Ask the Player if they wish to Hit, and take another card
# 8. If the Player's hand doesn't Bust (go over 21), ask if they'd like to Hit again.
# 9. If a Player Stands, play the Dealer's hand. The dealer will always Hit until the Dealer's value meets or exceeds 17
# 10. Determine the winner and adjust the Player's chips accordingly
# 11. Ask the Player if they'd like to play again
#
# Playing Cards
#
# A standard deck of playing cards has four suits (Hearts, Diamonds, Spades and Clubs) and thirteen ranks (2 through 10, then the face cards Jack, Queen, King and Ace)
# for a total of 52 cards per deck. Jacks, Queens and Kings all have a rank of 10. Aces have a rank of either 11 or 1 as needed to reach 21 without busting.
# As a starting point in your program, you may want to assign variables to store a list of suits, ranks, and then use a dictionary to map ranks to values.


#Step 1: Import the random module. This will be used to shuffle the deck prior to dealing. Then, declare variables to store suits, ranks and values

import random

#tuple of suits
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
#tuple of ranks
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
#dictionary of values
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
          'Queen':10, 'King':10, 'Ace':11}

playing = True

#Step 2: Create a Card Class
class Card:
    #init method is called when an instance is created. It's the constructor
    # Initializer / Instance Attributes
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    #for any function that ask for the string representation of my Card class, the function below is performed
    def __str__(self):
        return f"{self.rank} of {self.suit}"

#Step 3: Create a Deck Class
class Deck:
    #when we call this class we instantiate a deck. Which is 52 unique Card objects. We need to iterate through the ranks and suits to create the cards
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits: #4 suits
            for rank in ranks: #times 13 ranks will give us 52 Card objects when we create a deck object
                self.deck.append(Card(suit, rank)) #append Card Object to list.

    #return the contents of the deck
    def __str__(self):
        #for every card in the deck, call the str method from the Card class and print out its string representation
        for cards in self.deck:
            print(cards.__str__())
        return ""

    def shuffle(self): #take the deck shuffle it. call the shuffle method from the import library
        random.shuffle(self.deck)

    def deal(self): #when we deal a card we need remove it from the deck
        return self.deck.pop()


#Step 4: Create a Hand Class
#In addition to holding Card objects dealt from the Deck, the Hand class may be used to calculate the value of those cards using the values dictionary defined above
class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces

    def add_card(self,card):
        #add the card from the deal method in the Deck class to our hand or the CPU's hand
        #since we are adding Card(suit, rank), we can use the rank to increase the value of the hand
        self.cards.append(card)
        self.value += values[card.rank]

        #track aces
        if card.rank == "Ace":
            self.aces += 1



    def adjust_for_ace(self):
        #if the sum of the cards in your hand is greater than 21 and you have an Ace, we need to change it's value to a 1
        if(self.value > 21 and "Ace" in self.cards):
            self.value -= 10

        #track aces
        self.aces -= 1




#Step 5: Create a Chips Class
class Chips:

    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0

    def win_bet(self):
        #need to increase your total by the amount you bet
        self.total += self.bet

    def lose_bet(self):
        #need to decrease your total by the amount you bet
        self.total -= self.bet



#Step 6: Write a function for taking bets
def take_bet(chips):

    while True:
        try:
            chips.bet = int(input("How much do you want to wager this hand? \n"))
        except BaseException:
            print("You didn't enter a proper amount")
        else:
            if(chips.bet > chips.total):
                print("You can't wager {}. That is more than you have in your chip stack.".format(chips.bet))
            else:
                print("You are wagering {}".format(chips.bet))
                break





#Step 7: Write a function for taking hits
def hit(deck,hand):
    #everytime we call this function a card is popped from the deck
    hit_card = deck.deal()

    #add card to hand
    hand.add_card(hit_card)

    #adjust for an Ace if we have one
    hand.adjust_for_ace()



#Step 8: Write a function prompting the Player to Hit or Stand
def hit_or_stand(deck,hand):
    global playing #one player will continue to hit and then the dealer will go

    while True:
        hitOrStand = input("Do you want to hit or stand? Enter hit or stand: \n".lower())
        if(hitOrStand == "hit"):
            #call the hit function
            hit(deck, hand)
        elif(hitOrStand == "stand"):
            #stop taking cards and give up control
            playing = False
            break
        else:
            print("You either have to hit or stand. Please make a choice: \n")
            continue
        break




#Step 9: Write functions to display cards
#Note: this solution is not mine, it was provide by the TA. All other code was generated by me
def show_some(player,dealer): # function that accepts two parameters
    print("\nDealer's Hand:")
    print(" <card hidden>") # one card will be hidden
    print('',dealer.cards[1])# it will show the second card in the dealer's hand
    print("\nPlayer's Hand:", *player.cards, sep='\n ')# *player.cards means that we're going to print every card inside of the attribute cards, from player, and sep='\n ' means that every element will be printed and separated by a new line

def show_all(player,dealer): # function that accepts two parameters
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')# *dealer.cards means that we're going to print every card inside of the attribute cards, from dealer, and sep='\n ' means that every element will be printed and separated by a new line
    print("Dealer's Hand =",dealer.value) # print's the value of the cards in the dealer's hand
    print("\nPlayer's Hand:", *player.cards, sep='\n ')# *player.cards means that we're going to print every card inside of the attribute cards, from player, and sep='\n ' means that every element will be printed and separated by a new line
    print("Player's Hand =",player.value) #prints the value of the cards in player's hand.


#Step 10: Write functions to handle end of game scenarios
def player_busts(player,dealer,chips):
    print("Player busts and loses!!! \n")
    #decrease chip count
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player beats the dealer!!! \n")
    #increase chip count
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Dealer busts and loses!!! \n")
    #decrease chip count
    chips.win_bet()

def dealer_wins(player,dealer,chips):
    print("Dealer Wins!!! \n")
    #increase chip count
    chips.lose_bet()

def push():
    print("It's a tie!!! \n")


#Code to play the game and integrate everything
while True:
    # Print an opening statement
    print("Welcome to the table. Let's begin the game: ")

    # Create & shuffle the deck, deal two cards to each player
    print("Let's shuffle the deck and deal out the cards: \n")
    playingDeck = Deck()
    playingDeck.shuffle()

    #create the player and dealer hands
    playerHand = Hand()
    dealerHand = Hand()

    #deal out 4 cards
    card1 = playingDeck.deal()
    card2 = playingDeck.deal()
    card3 = playingDeck.deal()
    card4 = playingDeck.deal()

    #give the player and dealer 2 cards
    playerHand.add_card(card1)
    dealerHand.add_card(card2)
    playerHand.add_card(card3)
    dealerHand.add_card(card4)

    # Set up the Player's chips
    playerChips = Chips() #default value is 100 if you look above in the class definition

    # Prompt the Player for their bet
    take_bet(playerChips)


    # Show cards (but keep one dealer card hidden)
    show_some(playerHand, dealerHand)


    while playing:

        # Prompt for Player to Hit or Stand
        hit_or_stand(playingDeck, playerHand)


        # Show cards (but keep one dealer card hidden)
        show_some(playerHand, dealerHand)


        # If player's hand exceeds 21, run player_busts() and break out of loop
        if(playerHand.value > 21 ):
            player_busts(playerHand, dealerHand, playerChips)
            # Show cards (but keep one dealer card hidden)
            show_some(playerHand, dealerHand)
            break
    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if(playerHand.value <= 21):
        while(dealerHand.value < 17):
            hit(playingDeck, dealerHand)

        # Show all cards
        show_all(playerHand, dealerHand)

        # Run different winning scenarios
        if(dealerHand.value > 21):
            dealer_busts(playerHand, dealerHand, playerChips)
        elif( (dealerHand.value > playerHand.value) and dealerHand.value <=21 ):
            dealer_wins(playerHand, dealerHand, playerChips)
        elif( (playerHand.value > dealerHand.value) and playerHand.value <=21):
            player_wins(playerHand, dealerHand, playerChips)
        else:
            push()

    # Inform Player of their chips total
    print("\nPlayer's chip count is: {}".format(playerChips.total))


    # Ask to play again
    playAgain = input("Do you want to play again? Enter Y or N: \n".lower())
    if(playAgain == 'y'):
        playing = True
    else:
        print("Thank you for playing!!!")
        break

