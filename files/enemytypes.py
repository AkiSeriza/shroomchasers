from classes import Entity

class Mario(Entity):
    def __init__(self, position):
        super().__init__(position, "Mario")

    def turn_move(self, grid):
        pass