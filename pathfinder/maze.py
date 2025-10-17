from player import *

import sys
import time
import pygame


maze = []

window = pygame.display.set_mode((820, 820))
tileSize = 20

Black = (0, 0, 0)
White = (220, 220, 220)
Blue = (50, 150, 255)
Red = (255, 80, 80)
Grey = (120, 120, 120)


with open(r"c:\Users\25kava\Desktop\VSCode\Python\pathfinder\maze.txt", "r") as f:
    for line in f:
        row = []
        line = line.strip()
        for char in line:
            if char == "#":
                row.append(1)
            elif char == " ":
                row.append(0)
            elif char == "A":
                row.append(2)
            elif char == "B":
                row.append(3)
        maze.append(row)

goalCords = [39, 39]
startCords = [1, 1]

pathfinder = PlayerV2(startCords, goalCords)


def drawMap():
    for row_idx, row in enumerate(maze):
        for col_idx, cell in enumerate(row):
            if cell == 0:
                color = White
            elif cell == 1:
                color = Black
            elif cell == 2:
                color = Blue
            elif cell == 3:
                color = Red
            elif cell == 4:
                color = Grey

            pygame.draw.rect(window, color, (col_idx*tileSize,
                             row_idx*tileSize, tileSize, tileSize))

    pygame.draw.rect(
        window, finderCol, (finderPos[0]*tileSize, finderPos[1]*tileSize, tileSize, tileSize))

    pygame.display.update()


finderPos = None

pygame.init()
t = time.time()
running = True

while running:
    while finderPos != [39, 39]:
        pathfinder.filterWalls(maze)
        pathfinder.notVisited(maze)
        nextStep = pathfinder.decideNextStep()
        finderPos = pathfinder.takeNextStep(maze)

        maze[finderPos[1]][finderPos[0]] = 4
        finderCol = Red
        drawMap()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    running = False

print(f"Exit found in {time.time() - t:.2f} seconds!")
pygame.quit()
sys.exit()
