import random

class Player:
    def __init__(self, pos: list):
        self.pos = pos
        self.steps = []

    def isDeadEnd(self, map: list) -> bool:
        cases = 0
        und = 0
        x, y = self.pos

        up = map[y-1][x] != 1
        down = map[y+1][x] != 1
        left = map[y][x-1] != 1
        right = map[y][x+1] != 1

        if up != True: cases +=1
        if down != True: cases +=1
        if left != True: cases +=1
        if right != True: cases +=1
        
        if map[y-1][x] != 4: und +=1
        if map[y+1][x] != 4: und +=1
        if map[y][x-1] != 4: und +=1
        if map[y][x+1] != 4: und+=1

        if cases >= 3 and self.pos != [1,1 or [39,39]]:
            while und == 0:
                return True
        else:
            return False
        
    def nextStep(self, map: list) -> list:
        print("pos:", self.pos, "maze size:", len(map), len(map[0]))

        x, y = self.pos
        self.steps.append(self.pos)

        up = map[y-1][x] != 1
        down = map[y+1][x] != 1
        left = map[y][x-1] != 1
        right = map[y][x+1] != 1

        _up = map[y-1][x] != 4
        _down = map[y+1][x] != 4
        _left = map[y][x-1] != 4
        _right = map[y][x+1] != 4
        

        print(f"{up} | {down} | {left} | {right}")
        print(f"{_up} | {_down} | {_left} | {_right}")

        moved = False

        dirs = ['up', 'down', 'left', 'right']
        dir = dirs[random.randint(0, 3)]

        if _up and up:
            self.pos = [x, y-1]; moved = True
        elif _down and down:
            self.pos = [x, y+1]; moved = True
        elif _left and left:
            self.pos = [x-1, y]; moved = True
        elif _right and right:
            self.pos = [x+1, y]; moved = True

        if not moved:
            if up and dir:
                self.pos = [x, y-1]; moved = True
            elif down and dir:
                self.pos = [x, y+1]; moved = True
            elif left:
                self.pos = [x-1, y]; moved = True
            elif right:
                self.pos = [x+1, y]; moved = True

        print(self.pos)
        return self.pos

    def steps(self) -> list:
        return self.steps