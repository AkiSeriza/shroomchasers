from classes import TileFeature
from entitytypes import Player, Enemy

class Rock(TileFeature):
    def __init__(self):
        super().__init__("#",False)

class Trap(TileFeature):
    def __init__(self, passable=True):
        super().__init__("^",passable)

    def onTouch(self,entity, game):
        if isinstance(entity, Player):
            game.islost = True

        if isinstance(entity, Enemy):
            entity:Enemy
            entity.turnlimit = 0
            self.passable = False

class Goal(TileFeature):
    def __init__(self, passable=True):
        super().__init__("G", passable)

    def onTouch(self, entity, game):
        print("Touched Goal")
        if isinstance(entity, Player):
            game.iswon = True

class Normal(TileFeature):
    def __init__(self, passable=True):
        super().__init__(".", passable)

    def onTouch(self, entity, game):
        pass