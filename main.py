##Entrypoint
from files.leveleditor import mapgenerator
import files.classes as Game


if __name__ == "__main__":
    grid, player, entities = mapgenerator(input("Enter Level: "))
    initial_game = Game.Game(grid, player, entities)
    current_game = initial_game.copy()
    while current_game.isplaying:
        command = input("Enter Command: ")
        if command == "!":
            current_game = initial_game.copy()
            continue
        playercommand = player.getmovement(command, current_game.grid)
        if playercommand == False:
            print("Invalid Move")
            continue
        for i in current_game.entities:
            i.turn_move(current_game.grid)
