import random
import time
import os

os.system('cls')

cards = ["Ace", "King", "Queen", "Jack", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
suits = ["Hearts", "Diamonds", "Spades", "Clubs"]

def drawCard():
    return deck.pop(0)

def buildDeck():
    deck = []
    for suit in suits:
        for card in cards:
            deck.append(f"{card} of {suit}")
    random.shuffle(deck)
    return deck

def getHandValue(hand):
    total = 0
    aces = 0

    for card in hand:
        rank = card.split()[0]
        if rank.isdigit():
            total += int(rank)
        elif rank == "Ace":
            total += 11
            aces += 1
        else:  
            total += 10

    while total > 21 and aces > 0:
        total -= 10
        aces -= 1

    return total



input("BLACKJACK (Press enter to play...) : ")
print("You have 3000 dallahs to play with!")
money = 3000
game = True

while game:
    val = 0
    check = True
    playing = True
    deck = buildDeck()

    while check:
        bet = int(input("How much do you want to bet? : "))
        if bet > money:
            print("You don't have enough money, brokie") 
        else:
            check = False

    dealerCards = [drawCard(), drawCard()]
    playerCards = [drawCard(), drawCard()]

    while playing:
        
        os.system("cls")

        print(f"Current dallahs : {money - bet}")

        print(f"Dealer has two cards, one hidden and the other {dealerCards[1]}")

        val = getHandValue(playerCards)
        print(f"\nYou have : \n")
        for card in playerCards:
          print(card)
        print(f"Total value : {val}")


        if val == 21:
          print(f"Congrats, you got a blackjack!")
          playing = False
          time.sleep(2.5)
          os.system("cls")
          break
        elif val > 21:
            print(f"Daum, imagine lmaoooo. Goodbye {bet} dallahs!")
            money -= bet
            playing = False
            time.sleep(2.5)
            os.system("cls")
            break
        else:
            pass


        action = input("\nWhat do you do now?\n[S (Stand) | H (Hit)] : \n").lower()
        if action == "h":
            playerCards.append(drawCard())
            print(f"You drew {playerCards[-1]}")
            time.sleep(0.7)
        elif action == "s":
            playing = False
            time.sleep(0.7)
            os.system("cls")


    print("Let's see what the dealer does...")
    input("Press enter to continume")

    print(f"\nThe dealer's cards were : ")
    for card in dealerCards:
        time.sleep(0.7)
        print(card)

    time.sleep(0.7)

    val = getHandValue(dealerCards)

    print(f"With a total value of {val}")

    print("\n")

    time.sleep(2)

    input("Press enter to continue")
    os.system("cls")

    while val < 17:
        os.system("cls")
        print("The dealer draws another card!")
        time.sleep(0.7)
        dealerCards.append(drawCard())
        print(f"The dealer drew a {dealerCards[-1]}")
        val = getHandValue(dealerCards)

        time.sleep(0.7)
      
        print(f"\nThe dealer's cards are : ")
        for card in dealerCards:
          time.sleep(0.7)
          print(card)

          time.sleep(0.3)
        

        print(f"With a total value of {val} \n")
        time.sleep(2)


    if val > 21:
        print("The dealer busted")

    elif val == 21:
        print("The dealer got blackjack")


    else:
        print("\nThe dealer stands\n")

    input("Press enter to continue...")

    os.system("cls")

    print(f"You got {getHandValue(playerCards)}\nThe dealer got {val}")
    
    
    if val > 21 and getHandValue(playerCards) > 21:
        print("Hah, noone won. Both busted. Goodbye to your dallahs!")

    elif val > 21 and getHandValue(playerCards) <= 21 or val < getHandValue(playerCards) and getHandValue(playerCards) <= 21:
        print(f"You won! Your bet of {bet} dallahs has been doubbled!")
        money += bet
    
    elif val == getHandValue(playerCards):
        if val == 21:
            print(f"You both got a blackjack, so it's a tie. Your bet of {money} dallahs has been returned")

        else:
            print(f"It's a tie. Your bet of {money} dallahs has been returned")


    else:
        print("Haha, dealer won. Sämst!!")


    print(f"Current dallah balance : {money}")
    r = input("Want to play again? (y/n)").lower()
    if r == "y":
        continue
    else:
        play = False


os.system("cls")
print("Ok, cya")