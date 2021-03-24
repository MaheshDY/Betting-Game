'''To bet on the position of the cards(Jack, King and Queen) for virtual cash.

For example- The user bets that the king card is in the 1st position if it's true then the user gets 5 times the bet amount or else loses the bet amount. The user can bet and guess each time until the user has cash. The cards keep shuffling each time.'''

import random
cash = 100

def betting(bet):
    global cash
    cards=['K','Q','J']

    random.shuffle(cards) # shuffle the cards randomly
    print("Cards shuffled...")

    position=int(input("Your bet on position of the 'King' card is.."))
    if position>=0 and position<3:
        if cards[position]=='K':
            cash=cash+bet*5
            print("\tYou Won!!, cards position: {} and total cash: ${}\n".format(cards,cash))
        else:
            cash=cash-bet
            print("\tYou Lose!!, cards position:{} and total cash:${}\n".format(cards,cash))
    else:
        print("invalid option\n")

while cash>0:
    bet=int(input("Enter the Bet amount:$"))
    if bet<=0 or bet >cash:
        print("Invalid bet amount...\n")
        continue
    betting(bet)
