##General Idea: THe entire game order is handled by the Game Object, instantiated each time a game is started. 

class Cell:
    def __init__(self,name, height):
        self.name = name
        self.height = height
        self.feature = None

    def addfeature(self,feature):
        self.feature = feature
    
class Grid:
    def __init__(self, cells):
        self.cells: dict[tuple[int, int], Cell] = cells


    def enumeratecells(self):
        for i in self.cells:
            print(f"Info for Cell {self.cells[i].name}: height @ {self.cells[i].height}, has a {self.cells[i].feature}")

    def getcell(self, position):
        return self.cells[tuple(position)]

    def checkifvalidmove(self,position,movement):
        current_cell = self.getcell(position)
        new_position = [position[0] + movement[0], position[1] + movement[1]]
        new_cell = self.getcell(new_position)
        if new_cell.height > current_cell.height + 1:
            return False
        if new_cell.feature == "Rock":
            return False
        return True

class Player:
    def __init__(self, position):
        self.position = position

    def getmovement(self, command, grid:Grid):
        movements = {
            "W": (-1, 0),
            "A": (0, -1),
            "S": (1, 0),
            "D": (0, 1)
        }
        plannedmove = movements.get(command.upper())
        validity = grid.checkifvalidmove(self.position,plannedmove)
        if not validity:
            return False
        self.changepos((self.position[0] + plannedmove[0],self.position[1] + plannedmove[1]))
        return True


    def changepos(self,newpos):
        self.position = newpos

class Item:
    def __init__(self):
        pass

class Entity:
    def __init__(self, position):
        self.position = position

    def turn_move(self):
        pass

class Game:
    def __init__(self, grid, player, entities):
        self.grid: Grid= grid
        self.player: Player = player
        self.entities: list[Entity] = entities
        self.isplaying = True

    def startgame(self):
        while self.isplaying:
            self.player.getmovement(input())