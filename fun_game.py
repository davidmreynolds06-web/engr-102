# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name:  Deep Patel
#        Chris Voelkel
#        Karl Nolte
#        David Reynolds
# Section: 412
# Assignment: Lab Topic 13
# Date: 5 December 2025
# As a team, we have gone through all required sections of the
# tutorial, and each team member understands the material

import random as r


wins = 0
losses = 0
draws = 0


card_library = {"2": 2,
                "3": 3,
                "4": 4,
                "5": 5,
                "6": 6,
                "7": 7,
                "8": 8,
                "9": 9,
                "10": 10,
                "J": 10,
                "Q": 10,
                "K": 10,
                "A": 11}




def dealingforuser(users_hand, userlist):  # this deals for the player


    users_key = r.choice(list(card_library.keys()))


    userlist.append(users_key)


    users_hand += card_library[users_key]


    print(f"This is what the user currently drew: {" ".join(userlist)}")
    print(f"This is the users total: {users_hand}")


    return users_hand, userlist




def dealingfordealer(dealers_hand, dealerlist):  # this deals for the user


    dealers_key = r.choice(list(card_library.keys()))


    dealerlist.append(dealers_key)


    dealers_hand += card_library[dealers_key]


    print(f"This is what the dealer currently drew: {" ".join(dealerlist)}")
    print(f"This is the dealers total: {dealers_hand}")


    return dealers_hand, dealerlist




def hitorstand():  # this determines if the user will stand or hit


    doyouhit = input("Do you hit(h) or stand(s)? ")


    if doyouhit == "h":
        return True
    else:
        return False




def results(dealers_hand, users_hand):


    global wins, losses, draws


    if users_hand > dealers_hand or dealers_hand > 21:
        print("You Win")
        wins += 1
    elif dealers_hand == 21 or dealers_hand > users_hand:
        print("You lose")
        losses += 1
    else:
        print("Draw")
        draws += 1




def score():


    print(f"You have {wins} wins")
    print(f"You have {losses} losses")
    print(f"You have {draws} draws")




def over21orequal21(users_hand):
    global wins, losses, draws
    if users_hand == 21:
        wins += 1
        print("You win")
        return True
    elif users_hand > 21:
        losses += 1
        print("You lose")
        return True




def main():


    user = 0
    dealer = 0
    user_list = []
    dealer_list = []
    roundskipper = 0


    while True:


        user, user_list = dealingforuser(user, user_list)


        if over21orequal21(user):
            break


        if roundskipper == 0:
            dealer, dealer_list = dealingfordealer(dealer, dealer_list)
            roundskipper += 1


        if hitorstand():
            continue


        else:
            dealer, dealer_list = dealingfordealer(dealer, dealer_list)
            if dealer >= 17:
                results(dealer, user)
            else:
                while dealer < 17:
                    dealer, dealer_list = dealingfordealer(dealer, dealer_list)


                results(dealer, user)
            break




print("1. Show rules\n2. Play game\n3. Show score\n4. Quit")




while True:
    try:
        choice = int(input("Chose an option(1,2,3,4): "))
    except:
        print("That is an invalid option, try again")
        continue
    if choice == 1:
        print("""
    BLACKJACK RULES (Simplified)


    - The goal is to have a hand total closer to 21 than the dealer without going over.


    - Card values:
      2-10 = their number
      J, Q, K = 10
      A = 11


    - Player turn:
      You automatically draw one card each round.
      After seeing your cards and total, choose:
        h = hit (draw another card)
        s = stand (stop drawing)


    - If your total is exactly 21, you win immediately.
    - If your total goes over 21, you lose immediately.


    - Dealer turn:
      The dealer draws one card at the beginning.
      After you stand, the dealer draws until reaching a total of 17 or higher.


    - Final outcome:
      If the dealer goes over 21, you win.
      If the dealer's total is higher than yours, you lose.
      If your total is higher than the dealer's, you win.
      If both totals are the same, the game is a draw.
    """)
    elif choice == 2:
        main()
    elif choice == 3:
        score()
    elif choice == 4:
        print("Come play another time")
        break
