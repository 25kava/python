import time
import os

os.system("cls")
amt = int(input("Hur många deltagare ska med? : "))
fib = [0, 1]
start = time.time()

for e in range(2, amt + 2):
    fib.append(fib[-1] + fib[-2])

for i in range(1, amt + 1):
    print(f"På ö {i} finns det {fib[i]} deltagare om den är full")

saknas = fib[amt] - amt
print(f"På den sista ön saknas det {saknas} deltagare för att den ska vara full")

print(f"Total tid {(time.time() - start)}")

#Funkar inte, orkar inte fixa
