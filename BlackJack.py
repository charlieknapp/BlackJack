#Charlie Knapp
#COMP112
#Final Project: Blackjack
'''Three goals:
If statements - Determines how hands are played with inputs
Accumulator - Keeps track of the player’s balance
Lists - To hold all of the cards and pull from it when needed'''
balance=100
cards=[2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,'Jack','Jack','Jack','Jack','Queen','Queen','Queen','Queen','King','King','King','King','Ace','Ace','Ace','Ace']
import random
def sort(x):
    '''list->list
    sorts face cards into numbers'''
    i=0
    while i<len(x):
        if x[i]=='Jack':
            x.remove(x[i])
            x.append(10)
            i-=1
        if x[i]=='Queen':
            x.remove(x[i])
            x.append(10)
            i-=1
        if x[i]=='King':
            x.remove(x[i])
            x.append(10)
            i-=1
        if x[i]=='Ace':
            x.remove(x[i])
            x.append(11)
            i-=1
        i+=1
    return x
def value(x):
    '''list->int
    adds up all numbers in a list'''
    val=0
    for num in x:
        val+=num
    return val
            
def hand(balance):
    '''float->None
    plays through a hand of Blackjack and returns the players balance'''
    b=balance
    c=cards
    print('You have $'+str(b))
    while True:
        x=input('How much would you like to bet?\n')
        if x.isdigit():
            x=float(x)
            if x>b:
                print('You do not have enough money.')
                print('Enter a lower number')
            else:
                break
        else:
            print('Error: Please enter a number')
  
    i=0
    player_cards=[]
    dealer_cards=[]
    pvalues=[]
    dvalues=[]
    while i<2:
        n=random.randint(0,len(c)-1)
        player_cards.append(c[n])
        pvalues.append(c[n])
        c.remove(c[n])
        i+=1
    i=0
    while i<1:
        n=random.randint(0,len(c)-1)
        dealer_cards.append(c[n])
        dvalues.append(c[n])
        c.remove(c[n])
        i+=1
    print('Your cards:',player_cards)
    print('Dealer cards:', dealer_cards)
    sort(pvalues)
    val=value(pvalues)
    if val==21:
        print('Blackjack!')
        b+=(x*2)
        print('Your balance is now: $'+str(b))
        while True:
            play=input('Would you like to play again?(Enter y or n)\n')
            if play=='y':
                hand(b)
                return
            elif play=='n':
                return
            else:
                print('Error: That is not a valid entry. Try again')
    while True:
        val=value(pvalues)
        if val>21:
            for card in player_cards:
                if card=='Ace':
                    try:
                        pvalues.remove(11)
                        pvalues.append(1)
                    except ValueError:
                        pass
            val=value(pvalues)
            if val>21:
                print('Bust! You lose')
                b-=x
                print('Your balance is now: $'+str(b))
                if b==0:
                    print('You are out of funds.')
                    print('Come again!')
                    return
                while True:
                    play=input('Would you like to play again?(Enter y or n)\n')
                    if play=='y':
                        hand(b)
                        return
                    elif play=='n':
                        return
                    else:
                        print('Error: That is not a valid entry. Try again')
        ans=input('Would you like to hit?(Enter y or n)\n')
        if ans=='y':
            n=random.randint(0,len(c)-1)
            player_cards.append(c[n])
            pvalues.append(c[n])
            print(c[n])
            print('Cards:',player_cards)
            sort(pvalues)
        elif ans=='n':
            break
        else:
            print('Error: That is not a valid entry. Try again')
    sort(dvalues)
    dval=value(dvalues)
    print('Dealer cards:',dealer_cards)
    while True:
        dval=value(dvalues)
        if dval<17:
            n=random.randint(0,len(c)-1)
            dealer_cards.append(c[n])
            dvalues.append(c[n])
            print('Hit...')
            print(c[n])
            sort(dvalues)
        elif dval>21:
            for card in dealer_cards:
                if card=='Ace':
                    try:
                        dvalues.remove(11)
                        dvalues.append(1)
                    except ValueError:
                        pass
            dval=value(dvalues)
            if dval>21:
                print('Bust! You win!')
                b+=x
                print('Your balance is now: $'+str(b))
                while True:
                    play=input('Would you like to play again?(Enter y or n)\n')
                    if play=='y':
                        hand(b)
                        return
                    elif play=='n':
                        return
                    else:
                        print('Error: That is not a valid entry. Try again')
        else:
            break
    print('Dealer cards:',dealer_cards)
    if val>dval:
        print('You win!')
        b+=x
        print('Your balance is now: $'+str(b))
        while True:
            play=input('Would you like to play again?(Enter y or n)\n')
            if play=='y':
                hand(b)
                return
            elif play=='n':
                return
            else:
                print('Error: That is not a valid entry. Try again')
    elif val<dval:
        print('You lose!')
        b-=x
        print('Your balance is now: $'+str(b))
        if b==0:
            print('You are out of funds.')
            print('Come again!')
            return
        while True:
            play=input('Would you like to play again?(Enter y or n)\n')
            if play=='y':
                hand(b)
                return
            elif play=='n':
                return
            else:
                print('Error: That is not a valid entry. Try again')
    else:
        print('You tied!')
        print('Your balance is still: $'+str(b))
        while True:
            play=input('Would you like to play again?(Enter y or n)\n')
            if play=='y':
                hand(b)
                return
            elif play=='n':
                return
            else:
                print('Error: That is not a valid entry. Try again')
hand(balance)
