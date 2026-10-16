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
        if tuple(position) in self.cells:
            return self.cells[tuple(position)]
        else: return None

    def checkifvalidmove(self,position,movement):
        current_cell = self.getcell(position)
        new_position = [position[0] + movement[0], position[1] + movement[1]]
        print(new_position)
        new_cell = self.getcell(new_position)
        if new_cell.height > current_cell.height + 1:
            return False, 0
        if new_cell.feature == "Rock":
            return False, 0
        return True, new_position


class Item:
    def __init__(self):
        pass

class Entity:
    #Core Entitity unit, see entitytypes.py for behaviours
    def __init__(self, position):
        self.position = position
        self.isturn = False

    def changeposition(self, newpos):
        self.position = newpos

    #Returns a tuple which tells you which direction it wants to go
    def getmovement(self):
        pass

class Game:
    def __init__(self, grid, player, entities):
        self.grid: Grid= grid
        self.player: Entity = player
        self.entities: list[Entity] = entities
        self.isplaying = True

    def startgame(self):
        
        while self.isplaying:
            self.player.isturn = True
            while self.player.isturn:
                playermove = self.player.getmovement(input())
                validity, newpos = self.grid.checkifvalidmove(self.player.position, playermove)
                if not validity:
                    print("Invalid Move")
                    continue
                self.player.changeposition(newpos) #resolves turn
                self.player.isturn = False
            for currententity in self.entities:
                currententity.isturn = True
                while currententity.isturn == True:
                    enemymove = currententity.getmovement()
                    print(enemymove)
                    validity, newpos = self.grid.checkifvalidmove(currententity.position, enemymove)
                    if validity:
                        continue
                    currententity.changeposition(newpos)
            print(f"{[x for x in self.grid.cells]}; Player at {self.player.position}; Enemies: {[x.position for x in self.entities]}")
        
            


            