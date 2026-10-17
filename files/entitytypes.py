from classes import Entity, Grid
from random import shuffle
from ai import bfs

#Enemy Subclass
class Enemy(Entity):
    def __init__(self, position, turnlimit,symbol):
        self.state = None
        super().__init__(position, symbol)
        self.target = None
        self.turnlimit = turnlimit +1
        self.currentturn = 0
        self.istrapped = False
    
    def changetarget(self, newtarget: Entity):
        self.target = newtarget


class Honami(Enemy):
    def __init__(self, position):
        super().__init__(position, 1, "H")
        self.state = 0

    def getmovement(self, grid: Grid):
        if self.currentturn >= self.turnlimit:
            self.isturn  = False        
            return (0,0)
        return bfs(self,grid)
    
    def afterturn(self):
        if not self.istrapped:
            self.state = (self.state + 1) % 3
            self.turnlimit = self.state +1
        
    

    

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
        if ydir > 0:
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
        if ydir > 0:
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
        if xdir > 0:
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
        return bfs(self,grid)

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