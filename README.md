# Shroom Chasers

A small, text-based grid game prototype. Move around the map, avoid the enemies and traps, and try to reach a goal. It is still a work in progress, so expect rough edges.

## Run it

The project uses Python's standard library, so no extra packages are needed. From the repository root, run:

```powershell
python files/main.py
```

Use **W**, **A**, **S**, and **D** to move up, left, down, and right.

## Map format

Levels are defined as text in `files/main.py`. A level starts with its row and column counts, followed by the height map and then the tile map. Each row contains space-separated values.

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

| Symbol | Meaning |
| --- | --- |
| `.` | Normal floor |
| `#` | Rock |
| `^` | Trap |
| `G` | Goal |
| `+` | Player start |
| `L`, `M`, `J` | Enemies |

Rocks cannot be crossed. Touching a trap loses the game, and reaching a goal wins. Enemies move toward the player.

## Project layout

- `files/main.py` – sample level and game entry point
- `files/classes.py` – grid, cell, entity, and game-loop classes
- `files/entitytypes.py` – player and enemy movement
- `files/tilefeatures.py` – tile features and their effects
- `files/leveleditor.py` – parses text maps into grids, players, and enemies

This is an early prototype rather than a finished game, and the code and map format may change as it grows.
