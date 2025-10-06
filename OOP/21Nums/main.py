from comp import *
import os

compWin = 0
playerWin = 0

compStart = False

comp = AI("comp")
player = AI("player")

sum = 0

gameLoops = 1000

while gameLoops >= 1:
    nums = []
    sum = 0
    gameLoops -= 1
    while sum < 21:
        sum = 0
        
        nums = comp.addNum(nums)
        for num in nums:
            sum += num

        if sum == 21:
            print("Player wins")
            playerWin += 1
            break

        sum = 0

        nums = player.addNum(nums)

        for num in nums:
            sum += num

        if sum == 21:
            print("Computer wins")
            compWin += 1
            break
        
        print(sum)

os.system("cls")
print(f"Computer wins : {compWin}\nPlayer wins : {playerWin}")