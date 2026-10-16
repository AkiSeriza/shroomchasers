from classes import Entity

#Enemy Subclass
class Enemy(Entity):
    def __init__(self, position, turnlimit,symbol):
        super().__init__(position, symbol)
        self.target = None
        self.turnlimit = turnlimit
        self.currentturn = 0
    
    def changetarget(self, newtarget: Entity):
        self.target = newtarget


class Mario(Enemy):
    def __init__(self, position):
        super().__init__(position,2, "M")
    
    def getmovement(self):
        if self.currentturn == self.turnlimit:
            self.isturn  = False        
        xdir = self.position[0] - self.target.position[0]
        if xdir > 0:
            return (-1,0)
        if xdir < 0:
            return (1,0)
        ydir = self.position[1] - self.target.position[1]
        if ydir > 0:
            return (0,-1)
        if ydir < 0:
            return (0,1)

class Luigi(Enemy):
    def __init__(self, position):
        super().__init__(position,1, "L")

    def getmovement(self):
        if self.currentturn == self.turnlimit:
            self.isturn  = False        
        xdir = self.position[0] - self.target.position[0]
        if xdir > 0:
            return (-1,0)
        if xdir < 0:
            return (1,0)
        ydir = self.position[1] - self.target.position[1]
        if ydir > 0:
            return (0,-1)
        if ydir < 0:
            return (0,1)

class Jem(Enemy):
    def __init__(self, position):
        super().__init__(position,2,"J")

    def getmovement(self):
        if self.currentturn == self.turnlimit:
            self.isturn  = False     
        ydir = self.position[1] - self.target.position[1]
        if ydir > 0:
            return (0,-1)
        if ydir < 0:
            return (0,1)   
        xdir = self.position[0] - self.target.position[0]
        if xdir > 0:
            return (-1,0)
        if xdir < 0:
            return (1,0)


        

class Player(Entity):
    def __init__(self, position, ):
        super().__init__(position, "+")

    def getmovement(self, command):
        movements = {
            "W":(-1,0),
            "A":(0,-1),
            "S":(1,0),
            "D":(0,1)
        }
        plannedmove = movements.get(command.upper())
        return plannedmove