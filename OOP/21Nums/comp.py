import random

class AI:
    def __init__(self, id: str) -> None:
        self.numChoice = 0
        self.id = id

    def addNum(self, nums: list) -> list:
        total = sum(nums)
        
        if total + 1 in [4, 8, 12, 16, 18, 21]:
            self.numChoice = 1
        else:
            self.numChoice = random.randint(1,2)

        nums.append(self.numChoice)
        return nums


if __name__ == "__main__":
    nums = []
    comp = AI("comp")
    player = AI("player")

    total = 0
    turn = 1

    while total < 21:
        print(f"\nTurn {turn}")
        nums = comp.addNum(nums)
        total = sum(nums)
        if total >= 21:
            print("Computer wins!")
            break

        nums = player.addNum(nums)
        total = sum(nums)
        if total >= 21:
            print("Player wins!")
            break

        turn += 1