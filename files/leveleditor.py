import classes as Game
import entitytypes as Entity
import tilefeatures as Tiles

FEATURES = {
    "#": Tiles.Rock,
    "^": Tiles.Trap,
    "G": Tiles.Goal,
    ".": Tiles.Normal,
    "P": Tiles.Portal
}

ENTITIES = {
    "M": Entity.Mario,
    "J": Entity.Jem,
    "L": Entity.Luigi,
    "A": Entity.Aki,
    "W": Entity.Waluigi,
    "H": Entity.Honami
}

def mapgenerator(level: str):
    if level == None:
        raise ValueError
    partiallyparsed = level.split("\n")
    dimensions = partiallyparsed[0].split(" ")
    rows, columns = [int(x) for x in dimensions]
    heightmap = partiallyparsed[1:rows+1]
    entitymap = partiallyparsed[rows+1:]
    heightmap = [[int(y) for y in x.split(" ")] for x in heightmap]
    entitymap = [[y for y in x.split(" ")] for x in entitymap]
    entities:list[Entity.Enemy] = []
    cells = {}
    portals = []
    for i in range(rows):
        for j in range(columns):
            cell = Game.Cell(f"{i},{j}", heightmap[i][j])
            current_envi = entitymap[i][j]
            if current_envi in FEATURES:
                feature = FEATURES[current_envi]()
                cell.addfeature(feature)
                if isinstance(feature, Tiles.Portal):
                    portals.append((i, j, feature))
            elif current_envi in ENTITIES:
                cell.addfeature(Tiles.Normal())
                entitytype: Game.Entity = ENTITIES[current_envi]
                enemy = entitytype([i,j])
                entities.append(
                    enemy
                )
            elif current_envi == "+":
                cell.addfeature(Tiles.Normal())
                player = Entity.Player([i,j])
            cells[(i,j)] = cell
    if len(portals) not in (0, 2):
        raise ValueError("A level must contain either zero or exactly two portals")
    if portals:
        first_position = portals[0][:2]
        second_position = portals[1][:2]
        portals[0][2].link(second_position)
        portals[1][2].link(first_position)
    grid = Game.Grid(cells,[rows, columns])
    grid.enumeratecells()
    for i in entities:
        i.changetarget(player)
    return grid, player, entities



if __name__ == "__main__":
    print(mapgenerator(
    """4 4
    1 1 1 1
    1 1 1 1
    1 1 1 1
    1 1 1 1
    + . . .
    . . . .
    . . . .
    . . . M
    """))