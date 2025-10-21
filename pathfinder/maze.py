from finders import *

import time
import pygame
import random

finders = []
sCords = None
leastSteps = 10e10


def r(low, high):
    return random.randint(low, high)


windowSize = 820
tileSize = windowSize / 41
pygame.init()
window = pygame.display.set_mode((windowSize, windowSize))

Black = (0, 0, 0)
White = (220, 220, 220)
Blue = (50, 150, 255)
Red = (255, 80, 80)
Grey = (120, 120, 120)


def generateMap():
    global maze
    maze = []

    with open(r"c:\Users\25kava\Desktop\VSCode\Python\pathfinder\maze.txt", "r") as f:
        for line in f:
            row = []
            line = line.strip()
            for char in line:
                if char == "#":
                    row.append(1)
                elif char == " ":
                    row.append(0)
                elif char == "S":
                    row.append(2)
                elif char == "E":
                    row.append(3)
            maze.append(row)


generateMap()


def drawMap():
    global startCords, goalCords
    for row_idx, row in enumerate(maze):
        for col_idx, cell in enumerate(row):
            if cell == 0:
                color = White
            elif cell == 1:
                color = Black
            elif cell == 2:
                if sCords != None:
                    startCords = sCords
                else:
                    startCords = [col_idx, row_idx]
                color = Blue
            elif cell == 3:
                color = Red
                goalCords = [col_idx, row_idx]
            else:
                color = Grey

            pygame.draw.rect(window, color, (col_idx*tileSize,
                             row_idx*tileSize, tileSize, tileSize))

    for finder in finders:
        pygame.draw.rect(
            window, finder.color, ((finder.pos[0]*tileSize), (finder.pos[1]*tileSize), tileSize, tileSize))

    pygame.display.update()


drawMap()

# pathfinder = PlayerV2(maze, startCords, goalCords, Blue, "1")
# pathfinder2 = PlayerV2(maze, [r(1, 39), r(1, 39)], goalCords, Red, "2")
# pathfinder3 = PlayerV2(maze, [r(1, 39), r(1, 39)],
#                        goalCords, (255, 165, 0), "3")
# pathfinder4 = PlayerV2(maze, [r(1, 39), r(1, 39)],
#                        goalCords, (255, 165, 165), "4")
# pathfinder5 = PlayerV2(maze, [r(1, 39), r(1, 39)],
#                        goalCords, (255, 0, 165), "5")

# finders.append(pathfinder)
# finders.append(pathfinder2)
# finders.append(pathfinder3)
# finders.append(pathfinder4)
# finders.append(pathfinder5)

dfs = DFS(maze, startCords, goalCords, Blue, "1")
finders.append(dfs)

gbdfs = GoalBiasDFS(maze, startCords, goalCords, Red, "1")
finders.append(gbdfs)

finderSPos = []

for finder in finders:
    finderSPos.append(finder.pos)


drawMap()

for index, finder in enumerate(finders):
    print("Finder", index + 1, " : ", finder)
    print()

drawMap()

for index, finder in enumerate(finders):

    t = time.time()

    drawMap()
    finder.map = maze

    while finder.pos != goalCords:

        finder.pos = finder.takeNextStep()
        maze[finder.pos[1]][finder.pos[0]] = finder.id

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)

        drawMap()

    generateMap()

    drawMap()

    print(
        f"Start position: {finderSPos[index]}\nFinder {index + 1} : Solved in {time.time() - t:.2f} seconds!\nTook {finder.steps} steps\n")

    if finder.steps < leastSteps:
        leastSteps = finder.steps
        leastStepsSTR = f"Finder {index + 1} had the least amount of steps : {leastSteps}"
print(leastStepsSTR)

exit()
