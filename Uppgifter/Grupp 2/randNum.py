import random
playing = True


while True:
    randNum = random.randint(1, 100)
    while playing:
        guess = int(input("Vad gissar du : "))
        if randNum == guess:
            print("Grattis, du vann!!!!!!")
            game = False
            break
        elif randNum > guess:
            print(f"Talet är större än {guess} ! ")
        else:
            print(f"Talet är mindre än {guess} ! ")
        
        guess = input("Vill du spela igen? [Y / N]").lower()
        if guess == "y":
            pass
        else:
            playing = False

    break

print("Okej hejdå!!")