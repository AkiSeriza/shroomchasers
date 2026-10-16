##Entrypoint
import classes as Game
from leveleditor import mapgenerator

map = """4 4
1 1 1 1
1 1 1 1
1 2 3 4
1 1 1 4
. . . +
. # . .
L . . .
. . . ."""

if __name__ == "__main__":
    grid, player, entities = mapgenerator(map)
    initial_game = Game.Game(grid, player, entities)
    current_game:Game.Game = initial_game
    current_game.startgame()


