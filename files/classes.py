##General Idea: THe entire game order is handled by the Game Object, instantiated each time a game is started. 

class Cell:
    def __init__(self,name, height, feature = None):
        self.name = name
        self.height = height

    def addfeature(self,feature):
        self.feature:TileFeature = feature
    
class Grid:
    def __init__(self, cells, dimensions: list[int,int]):
        self.cells: dict[tuple[int, int], Cell] = cells
        self.dimensions = dimensions

    def enumeratecells(self):
        for i in self.cells:
            print(f"Info for Cell {self.cells[i].name}: height @ {self.cells[i].height}, has a {self.cells[i].feature}")

    def getcell(self, position):
        if tuple(position) in self.cells:
            return self.cells[tuple(position)]
        else: return None

    def checkifvalidmove(self,position,movement):
        current_cell = self.getcell(position)
        print(f"Current Cell: {current_cell}")
        new_position = [position[0] + movement[0], position[1] + movement[1]]
        print(new_position)
        new_cell = self.getcell(new_position)
        if new_cell == None:
            return False, 0
        if new_cell.height > current_cell.height + 1:
            return False, 0
        if new_cell.feature.passable == False:
            return False, 0
        return True, new_position

    def displaygrid(self, entities, player):
        entitydict = {tuple(x.position): x for x in entities}
        for i in range(self.dimensions[0]):
            for j in range(self.dimensions[1]):
                current_cell = self.getcell([i,j])
                if current_cell.feature != None:
                    print(current_cell.feature[0], end=" ")
                elif player.position == [i,j]:
                    print("+", end=" ")
                elif (i,j) in entitydict:                    
                    print((entitydict[(i,j)]).symbol, end=" ")
                else:
                    print(".", end=" ")
            print()

class Item:
    def __init__(self):
        pass

class TileFeature:
    def __init__(self, passable = True):
        self.passable = passable

    def onTouch(self, entity:Entity, game:Game):
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

#Game handler
class Game:
    def __init__(self, grid, player, entities):
        self.grid: Grid= grid
        self.player: Entity = player
        self.entities: list[Entity] = entities
        self.isplaying = True
        self.iswon = False
        self.islost = False

    def startgame(self):
        
        while self.isplaying:
            if self.islost == True:
                print("You Lose")
                self.isplaying = False
                return     
            self.player.isturn = True
            while self.player.isturn:
                playermove = self.player.getmovement(input())
                print(playermove)
                validity, newpos = self.grid.checkifvalidmove(self.player.position, playermove)
                if not validity:
                    print("Invalid Move")
                    continue
                self.player.changeposition(newpos) #resolves turn
                self.player.isturn = False
                if self.iswon == True:
                    print("You Win!")
                    return               
            for currententity in self.entities:
                if currententity.position == self.player.position:
                    self.islost = True
                currententity.isturn = True
                currententity.currentturn = 0
                while currententity.isturn == True:
                    enemymove = currententity.getmovement()
                    validity, newpos = self.grid.checkifvalidmove(currententity.position, enemymove)
                    if not validity:
                        continue
                    currententity.changeposition(newpos)
                    if currententity.position == self.player.position:
                        self.islost = True
                    currententity.currentturn += 1
                    print(f"{currententity.currentturn}; {currententity.turnlimit}")
            print("------------------------:-------------------------")
            self.grid.displaygrid(self.entities,self.player)
        
            


            