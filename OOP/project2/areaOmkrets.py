from formerLib import *
import os, time

os.system('cls;')

shapeCheck = True
floatCheck = True
unitCheck = True

while (shapeCheck):
    try:
        shape = input("Vilken form vill du räkna area / omkrets på? (Rektangel / Triangel / Cirkel)? : ").lower()
        if not shape in ("rektangel", "triangel", "cirkel"):
            raise customException("Välj en korrekt form (Rektangel / Triangel / Cirkel)")
        
        shapeCheck = False
        os.system('cls')

    except (customException) as error:
        print (f"Program interrupted : {error}")
        time.sleep(2.75)
        os.system('cls')

while (floatCheck):
    if (shape == "cirkel"):
        try:
            rad = float(input(f"Vad är radien av din {shape}? : "))
            floatCheck = False
        except ValueError as error:
            print (f"Program interrupted : {error}")
            time.sleep(2.75)
            os.system('cls')
    else:
        try:
            bas = float(input(f"Vad är basen av din {shape}? : "))
            hojd = float(input(f"Vad är höjden av din {shape}? : "))
            floatCheck = False
            os.system('cls')
        except ValueError as error:
            print (f"Program interrupted : {error}")
            time.sleep(2.75)
            os.system('cls')

while (unitCheck):
    try:
        unit = input("Välj en enhet (mm / cm / dm / m) : ")
        if not unit in ("mm", "cm", "dm", "m"):
            raise customException("Välj en korrekt enhet (mm, cm, dm, m)")
        
        unitCheck = False
        os.system('cls')
    except (ValueError, customException) as error:
        print (f"Program interrupted : {error}")
        time.sleep(2.75)
        os.system('cls')

if shape != "cirkel":
    print(f"Din {shape} har alltså en bas på {bas:.2f} {unit} och höjd på {hojd:.2f} {unit}")
else:
    print(f"Din {shape} har alltså en radie på {rad:.2f} {unit} / diameter på {rad*2:.2f} {unit}")

input("")

if shape == "rektangel":
    calculation = rektangel(hojd, bas, unit)
elif shape == "triangel":
    calculation = triangel(hojd, bas, unit)
    print("(Om den är rätvinklig)")
else:
    calculation = cirkel(rad, unit)

calculation.calcArea()
calculation.calcOmkrets()
print("")