import time
import os
import random

phrase = "Typewriter test"

os.system("cls") 

for char in phrase:
    print(char, end="", flush=True)
    time.sleep(random.uniform(0.07, 0.15))