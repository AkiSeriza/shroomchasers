from classes import TileFeature
from entitytypes import Player

class Rock(TileFeature):
    def __init__(self):
        super().__init__("#",False)

class Trap(TileFeature):
    def __init__(self, passable=True):
        super().__init__("^",passable)

    def onTouch(self,entity, game):
        if isinstance(entity, Player):
            game.islost = True

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