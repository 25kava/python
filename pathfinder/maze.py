from player import *

import sys
import time
import pygame

pygame.init()

maze = []
goalCords = [39, 39]
startCords = [1, 1]

window = pygame.display.set_mode((820, 820))
tileSize = 20

Black = (0,0,0)
White = (220,220,220)
Blue = (50,150,255)
Red = (255,80,80)
Grey = (120,120,120)



with open("maze.txt", "r") as f:
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

pathfinder = Player(startCords)

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
            
            pygame.draw.rect(window, color, (col_idx*tileSize, row_idx*tileSize, tileSize, tileSize))
        
        pygame.draw.rect(window, finderCol, (finderPos[0]*tileSize, finderPos[1]*tileSize, tileSize, tileSize))

    pygame.display.update()
        


running = True
while running:
    while pathfinder.isDeadEnd(maze):
        print("Dead end!")
        finderPos = pathfinder.backtrack()
        print(pathfinder.steps)
        sys.exit()
    
    finderPos = pathfinder.nextStep(maze)
    maze[finderPos[1]][finderPos[0]] = 4
    finderCol = Red
    
    drawMap()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit("Cya")