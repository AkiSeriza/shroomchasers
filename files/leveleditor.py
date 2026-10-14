import classes as Game
FEATURES = {
    "#": "Rock",
    "^": "Trap",
    "G": "Goal",
}

ENTITIES = {
    "M": "Mario",
    "J": "Jem",
    "L": "Luigi",
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
    entities, cells = [], {}
    for i in range(rows):
        for j in range(columns):
            cell = Game.Cell(f"{i},{j}", heightmap[i][j])
            current_envi = entitymap[i][j]
            if current_envi in FEATURES:
                cell.addfeature(FEATURES[current_envi])
            elif current_envi in ENTITIES:
                entities.append(
                    Game.Entity([i, j], ENTITIES[current_envi])
                )
            elif current_envi == "+":
                player = Game.Player([i, j])
            cells[(i,j)] = cell
    grid = Game.Grid(cells)
    grid.enumeratecells()
    return grid, player, entities




print(mapgenerator(
"""4 4
1 2 3 4
2 2 3 4
2 4 3 4
1 2 3 4
+ . . .
. # . .
. . ^ .
L # . G
"""))