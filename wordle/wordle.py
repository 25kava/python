from words import * 
import random
from termcolor import colored

gen = Words()
words_list = gen.genWords()

game = True
while game:

    word = random.choice(words_list)
    print("Jag tänker på ett femsiffrigt ord!")
    choice = ""

    while choice != word:

        choice = input("Gissa ordet: ").lower()

        if choice == word:
            print("Grattis, du vann!\n")
            break

        for cletter, wletter in zip(choice, word):
            if cletter == wletter:
                print(colored(f"{cletter}", "green"), end=" ")
            elif cletter in word:
                print(colored(f"{cletter}", "yellow"), end=" ")
            else:
                print(colored(f"{cletter}", "red"), end=" ")
        print("\n")