inpt = input("Skriv dina rommerska siffror här : ").lower()
total = 0

for letr in inpt:
    if letr == "i":
        total += 1
    elif letr == "v":
        total += 5
    elif letr == "x":
        total += 10
    elif letr == "l":
        total += 50
    elif letr == "c":
        total += 100
    elif letr == "d":
        total += 500
    elif letr == "m":
        total += 1000
    else:
        print(f"Letter {letr} is not a roman numeral !")

print(f"\nYour roman numerals sum to a total value of {total}")

#TODO: Orkar inte lägga till att exempelvis IV är 4. Så XIV, 14, blir istället samma som XVI, 16.
