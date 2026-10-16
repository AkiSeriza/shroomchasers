from classes import Entity

#Enemy Subclass
class Enemy(Entity):
    def __init__(self, position):
        super().__init__(position)
        self.target = None

    def changetarget(self, newtarget: Entity):
        self.target = newtarget


class Mario(Enemy):
    def __init__(self, position):
        super().__init__(position)

    def getmovement(self):
        self.isturn =  False
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

        

class Player(Entity):
    def __init__(self, position):
        super().__init__(position)

    def getmovement(self, command):
        movements = {
            "W":(-1,0),
            "A":(0,-1),
            "S":(1,0),
            "D":(0,1)
        }
        plannedmove = movements.get(command.upper())
        return plannedmove