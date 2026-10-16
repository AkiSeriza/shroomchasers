import classes as Game
import entitytypes as Entity
FEATURES = {
    "#": "Rock",
    "^": "Trap",
    "G": "Goal",
}

ENTITIES = {
    "M": Entity.Mario,
    "J": Entity.Jem,
    "L": Entity.Luigi,
}

def mapgenerator(level: str):
    if level == None:
        ValueError
    partiallyparsed = level.split("\n")
    dimensions = partiallyparsed[0].split(" ")
    rows, columns = [int(x) for x in dimensions]
    heightmap = partiallyparsed[1:rows+1]
    entitymap = partiallyparsed[rows+1:]
    heightmap = [[int(y) for y in x.split(" ")] for x in heightmap]
    entitymap = [[y for y in x.split(" ")] for x in entitymap]
    entities:list[Entity.Enemy] = []
    cells = {}
    for i in range(rows):
        for j in range(columns):
            cell = Game.Cell(f"{i},{j}", heightmap[i][j])
            current_envi = entitymap[i][j]
            if current_envi in FEATURES:
                cell.addfeature(FEATURES[current_envi])
            elif current_envi in ENTITIES:
                entitytype: Game.Entity = ENTITIES[current_envi]
                enemy = entitytype([i,j])
                entities.append(
                    enemy
                )
            elif current_envi == "+":
                player = Entity.Player([i,j])
            cells[(i,j)] = cell
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