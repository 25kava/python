import random
import time
import os

os.system('cls;')

rightNum = int(input("Säg ett nummer mellan 1 och 100 : "))
compGuess = None

highest = 100
lowest = 1

atps = 0


while rightNum > 100 or rightNum < 1:
    print("Jag sa mellan 1 och 100 nöt")
    rightNum = int(input("\nSäg ett nummer mellan 1 och 100 : "))
    

while compGuess != rightNum:

    atps += 1
    

    compGuess = random.randint(lowest, highest)

    if compGuess == rightNum:
        break
    
    os.system('cls;')
    atps += 1
    hl = input(f"Är nummret högre eller lägre än {compGuess} (H / L) : ").lower()
    
    if hl == "h" and rightNum > compGuess:

        lowest = compGuess + 1
    
    elif hl == "l" and rightNum < compGuess:

        highest = compGuess -1

    elif hl not in ("h", "l"):
        print("Skriv (H / L), inget annat!")
        time.sleep(1.5)
        atps -= 1

    else:
        print("Sluta ljug nöt")
        time.sleep(1.5)
        atps -= 1

print(f"\nNummret är {compGuess}!\nYay, jag gissade rätt!\nDet tog mig {atps} försök")