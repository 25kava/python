import math
import random


class base:
    def __init__(self, map: list, pos: list, goalCords: list, color, id: str):
        self.map = map
        self.pos = pos
        self.color = color
        self.viableSteps = []
        self.stepLog = []
        self.end = goalCords
        self.id = id
        self.steps = 0

    def filterWalls(self) -> list[str]:
        self.viableSteps = ['up', 'down', 'left', 'right']
        x, y = self.pos

        up = self.map[y-1][x] != 1
        down = self.map[y+1][x] != 1
        left = self.map[y][x-1] != 1
        right = self.map[y][x+1] != 1

        if not up:
            self.viableSteps.remove('up')
        if not down:
            self.viableSteps.remove('down')
        if not left:
            self.viableSteps.remove('left')
        if not right:
            self.viableSteps.remove('right')

        return self.viableSteps


class DFS(base):

    def notVisited(self) -> list[str]:
        x, y = self.pos

        _up = self.map[y-1][x] != self.id
        _down = self.map[y+1][x] != self.id
        _left = self.map[y][x-1] != self.id
        _right = self.map[y][x+1] != self.id

        if not _up:
            self.viableSteps.remove('up')
        if not _down:
            self.viableSteps.remove('down')
        if not _left:
            self.viableSteps.remove('left')
        if not _right:
            self.viableSteps.remove('right')

        # print(f"Filtered visited: {self.viableSteps}")
        return self.viableSteps

    def decideNextStep(self) -> None:
        if len(self.viableSteps) > 1:
            self.nextStep = random.choice(self.viableSteps)
        elif len(self.viableSteps) == 1:
            self.nextStep = self.viableSteps[0]
        else:
            self.nextStep = 'BT'

        # print(f"Took step: ['{self.nextStep}']\n")
        self.steps += 1

    def takeNextStep(self) -> list:
        self.filterWalls()
        self.notVisited()
        self.decideNextStep()

        # print(f"Filtered walls: {self.viableSteps}")

        x, y = self.pos

        if self.nextStep == 'up':
            self.pos = [x, y-1]
        elif self.nextStep == 'down':
            self.pos = [x, y+1]
        elif self.nextStep == 'left':
            self.pos = [x-1, y]
        elif self.nextStep == 'right':
            self.pos = [x+1, y]
        else:
            self.pos = self.backtrack()

        if self.nextStep != 'BT':
            self.stepLog.append(self.pos)

        return self.pos

    def backtrack(self) -> list:
        try:
            self.pos = self.stepLog.pop()
        except:
            exit("\nNo possible path! Try changing the position of the goal cords!")

        self.filterWalls()
        possible = self.notVisited()

        if possible:
            return self.pos

        return self.pos


class GoalBiasDFS(DFS):

    def decideNextStep(self) -> None:
        if len(self.viableSteps) > 1:
            self.nextStep = self.decideBias(self.viableSteps)
        elif len(self.viableSteps) == 1:
            self.nextStep = self.viableSteps[0]
        else:
            self.nextStep = 'BT'

        # print(f"Took step: ['{self.nextStep}']\n")
        self.steps += 1

    def calcHypo(self, x1: int, x2: int, y1: int, y2: int):
        return math.sqrt(((x1 - x2)**2) + ((y1 - y2)**2))

    def decideBias(self, steps: list[str]) -> str:
        x, y = self.pos
        endX, endY = self.end

        smallest = 10e10
        smallestIndex = None

        for index, candidate in enumerate(steps):
            if candidate == "up":
                temp = self.calcHypo(endX, x, endY, y-1)
            if candidate == "down":
                temp = self.calcHypo(endX, x, endY, y+1)
            if candidate == "left":
                temp = self.calcHypo(endX, x-1, endY, y)
            if candidate == "right":
                temp = self.calcHypo(endX, x+1, endY, y)

            if temp < smallest:
                smallest = temp
                smallestIndex = index

        # print(f"Bias chose: ['{steps[smallestIndex]}']")
        return steps[smallestIndex]
