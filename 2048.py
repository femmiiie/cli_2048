import sys
import random

class Board:
    def __init__(self, seed)->None:
        #inits empty board
        self.board = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
        random.seed = seed
        self.val = 0
        self.row = 0
        self.col = 0

    def generate_rand(self)->None:
        pass

    def insert(self)->None:
        pass


def main():
    #intialize board
    board = Board(1234)
    
    #import based on cli arguments
    #if no args provided, defaults to gui
    try:
        if sys.argv[1] == "cli":
            import cli as game
        elif sys.argv[1] == "gui":
            import gui as game
        else:
            print("Usage: 2048.py [cli, gui]")
            exit()
    except:
        import gui as game

    #send into respective loops based on import
    #game.loop()

if __name__ == "__main__":
    main()

    