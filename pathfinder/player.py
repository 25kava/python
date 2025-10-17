import random
import time
import math


class PlayerV2:
    def __init__(self, pos: list, goalCords: list):
        self.pos = pos
        self.viableStep = []
        self.steps = []
        self.end = goalCords

    def filterWalls(self, map: list[int, int]) -> list[str]:
        self.viableStep = ['up', 'down', 'left', 'right']
        x, y = self.pos

        up = map[y-1][x] != 1
        down = map[y+1][x] != 1
        left = map[y][x-1] != 1
        right = map[y][x+1] != 1

        if not up:
            self.viableStep.remove('up')
        if not down:
            self.viableStep.remove('down')
        if not left:
            self.viableStep.remove('left')
        if not right:
            self.viableStep.remove('right')

        return self.viableStep

    def notVisited(self, map: list[int, int]) -> list[str]:
        x, y = self.pos
        temp = self.viableStep.copy()

        _up = map[y-1][x] != 4
        _down = map[y+1][x] != 4
        _left = map[y][x-1] != 4
        _right = map[y][x+1] != 4

        if not _up:
            self.viableStep.remove('up')
        if not _down:
            self.viableStep.remove('down')
        if not _left:
            self.viableStep.remove('left')
        if not _right:
            self.viableStep.remove('right')

        if len(self.viableStep) == 0:
            return self.viableStep
        else:
            return self.viableStep

    def decideNextStep(self) -> None:
        if len(self.viableStep) > 1:
            self.nextStep = self.decideBias(self.viableStep)
        elif len(self.viableStep) == 1:
            self.nextStep = self.viableStep[0]
        else:
            self.nextStep = 'BT'

    def calcHypo(self, x1: int, x2: int, y1: int, y2: int):
        return math.sqrt(((x1 - x2)**2) + ((y1 - y2)**2))

    def decideBias(self, steps: list[str]) -> str:
        x, y = self.pos
        endX, endY = self.end

        smallest = 10e10
        smallestIndex = None

        for index, candidate in enumerate(steps):
            if candidate is "up":
                temp = self.calcHypo(endX, x, endY, y-1)
            if candidate is "down":
                temp = self.calcHypo(endX, x, endY, y+1)
            if candidate is "left":
                temp = self.calcHypo(endX, x-1, endY, y)
            if candidate is "right":
                temp = self.calcHypo(endX, x+1, endY, y)

            if temp < smallest:
                smallest = temp
                smallestIndex = index

        return steps[smallestIndex]

    def takeNextStep(self, map: list) -> list:
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
            self.pos = self.backtrack(map)

        if self.nextStep != 'BT':
            self.steps.append(self.pos)

        return self.pos

    def backtrack(self, map: list) -> list:

        self.pos = self.steps.pop()
        self.filterWalls(map)
        possible = self.notVisited(map)

        if possible:
            return self.pos

        return self.pos
