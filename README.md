# Shroom

lmaooooooooooooooooooooooooooooooooooooooooooooooooo

## Overview

This project is still in an early stage and acts more like a foundation for a game engine than a complete playable game. It includes:

- grid and cell structures
- player movement handling
- entity and feature definitions
- level parsing from text-based map input
- a starting point for a level editor

## Project structure

- `main.py` – intended main entry point for the game
- `files/classes.py` – core game classes and map generation logic
- `files/leveleditor.py` – level editor or editor-related functionality scaffold

## Current gameplay model

The core model is built around these main concepts:

- `Cell`: represents a tile with a name, height, and optional feature
- `Grid`: stores the cell map and can enumerate it
- `Player`: tracks position and movement commands
- `Entity`: represents NPCs or non-player objects on the grid
- `Game`: manages the game loop and player interactions

## Running the project

At the moment, the repository does not yet have a complete game loop wired through `main.py`, so the main logic is being developed in the `files` module.

## Example map format

The parser expects a level in a simple block format:

```text
4 4
1 2 3 4
2 2 3 4
2 4 3 4
1 2 3 4
+ . . .
. # . .
. . ^ .
L # . G
```

This format includes:

- first line: grid dimensions (`rows columns`)
- next rows: height map values
- remaining rows: entity / tile symbols on the map

## Notes

This is a prototype and may change significantly as the game design evolves. The current code establishes the building blocks for a larger text-based action or exploration game.
