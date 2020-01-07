import random

def aho():
    for i in range(100):
        if i % 3 == 0:
            print("アホ")
        else:
            print(i)

def show_input():
    val = input("enter something: ")
    print(val)

def compare_hundred():
    val = input("enter number: ")
    
    if int(val) == 100:
        print("exactly 100")
    elif int(val) < 100:
        print("less than 100")
    else:
        print("greater than 100")

def janken():
    janken_list = ["rock", "paper", "scissors"]
    user_result = input("enter rock, paper, or scissors: ")

    ai_result = janken_list[random.randint(0, 2)]

    print("computer chose " + ai_result + "\nyou chose " + user_result)

    if user_result == ai_result:
        print("tie")

    elif user_result == "rock":
        if ai_result == "paper":
            print("you lose")
        else:
            print("you win")
    
    elif user_result == "paper":
        if ai_result == "scissors":
            print("you lose")
        else:
            print("you win")

    elif user_result == "scissors":
        if ai_result == "rock":
            print("you lose")
        else:
            print("you win")

def blackjack():
    dealt = blackjack_check(random.randint(1, 13), 0)
    total = dealt
    dealer_dealt = blackjack_check(random.randint(1, 13), 0)
    dealer_total = dealer_dealt

    print("you're at: " + str(total) + "\ndealer is at: " + str(dealer_total))

    choice = input("\nhit or stay: ")

    if choice == "stay":
        while dealer_total <= 15 and dealer_total < total:
            dealer_dealt = blackjack_check(random.randint(1, 13), 0)
            dealer_total += dealer_dealt
            print("dealer got: " + str(dealer_dealt) + "\ndealer total: " + str(dealer_total))

        print("you're at: " + str(total) + "\ndealer is at: " + str(dealer_total))

        if total > dealer_total and total <= 21:
            print("\nyou win")
        else:
            print("\nyou lose")

    while choice == "hit":
        if total > 21:
            print("you busted")
            break

        if dealer_total <= 15:
            dealer_dealt = blackjack_check(random.randint(1, 13), 0)
            dealer_total += dealer_dealt

        dealt = blackjack_check(random.randint(1, 13), 0)
        total += dealt

        print("you're at: " + str(total) + "\ndealer is at: " + str(dealer_total))
        choice = input("\n\nhit or stay: ")

        if choice == "stay":
            while dealer_total <= 15 and dealer_total < total:
                dealer_dealt = blackjack_check(random.randint(1, 13), 0)
                dealer_total += dealer_dealt
                print("dealer got: " + str(dealer_dealt) + "\ndealer total: " + str(dealer_total))

            print("you're at: " + str(total) + "\ndealer is at: " + str(dealer_total))

            if total > dealer_total and total <= 21:
                print("\nyou win")
            else:
                print("\nyou lose")
    


def blackjack_check(val, total):
    if int(val) >= 10:
        return 10

    if int(val) == 1 and int(total) <= 10:
        return 11

    if int(val) == 1 and int(total) > 10:
        return 1

    return int(val)

blackjack()
#janken()
#compare_hundred()
#show_input()
#aho()