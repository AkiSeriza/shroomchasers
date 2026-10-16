from classes import Entity, Grid
from random import shuffle

#Enemy Subclass
class Enemy(Entity):
    def __init__(self, position, turnlimit,symbol):
        super().__init__(position, symbol)
        self.target = None
        self.turnlimit = turnlimit +1
        self.currentturn = 0
    
    def changetarget(self, newtarget: Entity):
        self.target = newtarget


class Mario(Enemy):
    def __init__(self, position):
        super().__init__(position,2, "M")
    
    def getmovement(self, grid: Grid):
        if self.currentturn >= self.turnlimit:
            self.isturn  = False        
            return (0,0)
        xdir = self.position[0] - self.target.position[0]
        ydir = self.position[1] - self.target.position[1]
        potentialmoves = []
        if xdir > 0:
            potentialmoves.append((-1,0))
        elif xdir < 0:
            potentialmoves.append((1,0))
        if ydir >= 0:
            potentialmoves.append((0,-1))
        if ydir < 0:
            potentialmoves.append((0,1))
        for move in potentialmoves:
            validity, newpos = grid.checkifvalidmove(self.position, move)
            if validity:
                return move
        return (0,0)

class Luigi(Enemy):
    def __init__(self, position):
        super().__init__(position,1, "L")

    def getmovement(self, grid: Grid):
        if self.currentturn >= self.turnlimit:
            self.isturn  = False        
            return (0,0)      
        xdir = self.position[0] - self.target.position[0]
        ydir = self.position[1] - self.target.position[1]
        potentialmoves = []
        if xdir > 0:
            potentialmoves.append((-1,0))
        elif xdir < 0:
            potentialmoves.append((1,0))
        if ydir >= 0:
            potentialmoves.append((0,-1))
        if ydir < 0:
            potentialmoves.append((0,1))
        for move in potentialmoves:
            validity, newpos = grid.checkifvalidmove(self.position, move)
            if validity:
                return move
        return (0,0)

class Jem(Enemy):
    def __init__(self, position):
        super().__init__(position,2,"J")

    def getmovement(self, grid: Grid):
        if self.currentturn >= self.turnlimit:
            self.isturn  = False        
            return (0,0)        
        xdir = self.position[0] - self.target.position[0]
        ydir = self.position[1] - self.target.position[1]
        potentialmoves = []
        if ydir > 0:
            potentialmoves.append((0,-1))
        if ydir < 0:
            potentialmoves.append((0,1))
        if xdir >= 0:
            potentialmoves.append((-1,0))
        elif xdir < 0:
            potentialmoves.append((1,0))
        for move in potentialmoves:
            validity, newpos = grid.checkifvalidmove(self.position, move)
            if validity:
                return move
        return (0,0)

#Standard BFS
class Aki(Enemy):
    def __init__(self, position):
        super().__init__(position, 1, "A")

    def getmovement(self, grid: Grid):
        if self.currentturn >= self.turnlimit:
            self.isturn = False        
            return (0, 0)        
        
        if self.position == self.target.position:
            return (0, 0)
        queue = []
        visited = {tuple(self.position)}
        cardinal_directions = [
            (0, -1), 
            (0, 1),   
            (-1, 0),  
            (1, 0)   
        ]
        for move in cardinal_directions:
            validity, newpos = grid.checkifvalidmove(self.position, move)
            if validity:
                tuple_pos = tuple(newpos)
                if tuple_pos not in visited:
                    visited.add(tuple_pos)
                    queue.append((newpos, move))
        while queue:
            current_pos, first_step = queue.pop(0)
            if current_pos == self.target.position:
                return first_step
                
            for move in cardinal_directions:
                validity, next_pos = grid.checkifvalidmove(current_pos, move)
                if validity:
                    tuple_next = tuple(next_pos)
                    if tuple_next not in visited:
                        visited.add(tuple_next)
                        queue.append((next_pos, first_step))
        return (0, 0)

class Waluigi(Enemy):
    def __init__(self, position):
        super().__init__(position, 3, "W")
        
    def getmovement(self, grid: Grid):
        if self.currentturn >= self.turnlimit:
            self.isturn = False        
            return (0, 0)    
        cardinal_directions = [
            (0, -1), 
            (0, 1),   
            (-1, 0),  
            (1, 0)   
        ]    
        shuffle(cardinal_directions)
        for move in cardinal_directions:
            validity, newpos = grid.checkifvalidmove(self.position, move)
            if validity:
                return move
        return (0,0)
        

class Player(Entity):
    def __init__(self, position, ):
        super().__init__(position, "+")
        

    def getmovement(self, command):
        movements = {
            "W":(-1,0),
            "A":(0,-1),
            "S":(1,0),
            "D":(0,1),
            "X":(0,0)
        }
        plannedmove = movements.get(command.upper())
        return plannedmove