amount = int(input("Antal deltagare? -> "))

last2 = int(0)
last1 = int(0)
current = int(1)

sequence = int(0)

while amount > 0:
    amount = amount - current
    last2 = last1
    last1 = current
    current = last1 + last2
    sequence = sequence + 1
print(f"Antal öar -> {sequence}")

#Tack Emir