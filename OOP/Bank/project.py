from acts import *
import os, random

os.system("cls;")

teo = account(random.randint(50, 5000), "Teo")
ludvig = account(random.randint(50, 5000), "Ludvig")
arvid = account(random.randint(50, 5000), "Arvid")

teo.deposit(21)
teo.withdraw(6000)


input("\n")