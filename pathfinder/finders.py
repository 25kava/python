import math
import random
import keyboard
import time
from collections import deque


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
        self.queue = []  # Används bara av BFS

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


class Player(DFS):
    def decideNextStep(self):
        if len(self.viableSteps) > 1:
            check = True
            while check:
                if keyboard.is_pressed("w") and 'up' in self.viableSteps:
                    self.nextStep = 'up'
                    check = False
                    time.sleep(0.15)
                elif keyboard.is_pressed("s") and 'down' in self.viableSteps:
                    self.nextStep = 'down'
                    check = False
                    time.sleep(0.15)
                elif keyboard.is_pressed("a") and 'left' in self.viableSteps:
                    self.nextStep = 'left'
                    check = False
                    time.sleep(0.15)
                elif keyboard.is_pressed("d") and 'right' in self.viableSteps:
                    self.nextStep = 'right'
                    check = False
                    time.sleep(0.15)

        elif len(self.viableSteps) == 1:
            self.nextStep = self.viableSteps[0]
        else:
            self.nextStep = 'BT'

        self.steps += 1
        time.sleep(0.05)


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


class BFS(base):

    def takeNextStep(self):
        x, y = self.pos

        for _x, _y in [(x, y-1), (x, y+1), (x-1, y), (x+1, y)]:
            if self.map[_y][_x] not in (1, self.id):
                self.queue.append([_x, _y])

        self.pos = self.queue.pop(0)
        self.steps += 1

        if self.pos == self.end:
            return self.pos

        return self.pos
