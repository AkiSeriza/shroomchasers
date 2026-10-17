# Shroom Chasers

A small, text-based grid game. Move around the map, avoid enemies and traps, and reach a goal to win.

## Run it

The project uses Python's standard library, so no extra packages are needed. From the repository root, run:

```powershell
python files/main.py
```

Use **W**, **A**, **S**, and **D** to move up, left, down, and right. Use **X** to stay in place for a turn.

## Map format

Levels are defined as text in `files/main.py`. A level starts with its row and column counts, followed by a height map and a tile map. Both maps must have the declared number of rows and columns. Values in each row are separated by spaces.

```text
4 4
1 1 1 1
1 1 1 1
1 1 1 1
1 1 1 1
+ . . .
. # . .
. . ^ .
L . . G
```

The first four rows after the dimensions are the cell heights. The next four rows describe the tiles:

| Symbol                       | Meaning                                                                       |
| ---------------------------- | ----------------------------------------------------------------------------- |
| `.`                          | Normal floor                                                                  |
| `#`                          | Rock; impassable                                                              |
| `^`                          | Trap; touching it loses the game as the player, and traps enemies             |
| `G`                          | Goal; reaching it wins                                                        |
| `P`                          | Portal; use exactly two per level, and entering either sends you to the other |
| `+`                          | Player start                                                                  |
| `H`, `A`, `M`, `L`, `J`, `W` | Enemies                                                                       |

Movement is limited by the height map: a move is blocked if the destination is more than one height level above the current cell. Enemies take their turns after the player.

## Project layout

- `files/main.py` – sample level and game entry point
- `files/classes.py` – grid, cell, entity, and game-loop classes
- `files/entitytypes.py` – player and enemy movement
- `files/tilefeatures.py` – tile features and their effects
- `files/leveleditor.py` – parses text maps into grids, players, and enemies

The game is a work in progress, so its features and map format may change.
