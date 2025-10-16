try:

    lis = [int(input("Vad är första talet i tallinjen? : ")), int(input("Vad är andra talet i tallinjen? : "))]
    lis.sort()
    check = int(input(f"Säg ett till tal, så ska jag kolla vart talet ligger i tallinjen {lis[0]} - {lis[1]} : "))

    mid  = (lis[0] + lis[1]) / 2

    if check == mid:
        print("Ditt tal är precis i mitten av tallinjen")
    elif check == lis[0] or check == lis[1]:
        print(f"Ditt tal är precis på gränsen av tallinjen")
    elif check > lis[1]:
        print("Ditt tal är ut till höger av tallinjen")
    elif check < lis[0]:
        print("Ditt tal är ut till vänster av tallinjen")
    else:
        print("Ditt befinner sig i tallinjen, i den", end=" ")
        if check > mid:
            print("högra kvadranten")
        else:
            print("vänstra kvadranten")

except:
    print("Skriv in ett tal, inte bokstäver eller blanksteg!")