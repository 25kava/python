length = float(input("Hur lång är du? [m] : "))
weight = float(input("Hur mycket väger du [kg] : "))

if length > 3:
    length = length / 100

length = length**2

BMI = weight / length

print(f"Ditt BMI : {BMI:.2f}")

if BMI < 18.5:
    print("Du är undervikt")

elif BMI >= 18.5 and BMI <= 24.5:
    print("Du är normalvikt")

else:
    print("Du är övervikt")