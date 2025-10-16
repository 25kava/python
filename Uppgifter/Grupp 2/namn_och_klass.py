import os
import time

os.system('cls')


play = False

listofnames = []
listofclass = []

print("Avsluta inmatningen med : stopp")
while play == False :

    namn = str(input("vad heter du? : ")).lower()
    if namn == ("stopp"):
        os.system("cls")
        print("--NAMN---Klass--")
        for namn, klas in zip(listofnames, listofclass):
            print(f"{namn} | {klas}" )

        input("Tryck enter för att fortsätta...")
        os.system('cls')
        break
    klass = str(input("vilken klass går du i? : ")).lower()

    listofnames.append(namn)
    listofclass.append(klass)
    if namn!= ("stopp"):
        pass