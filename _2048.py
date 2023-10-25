import sys
import random

class Board:
    def __init__(self, seed)->None:
        self.val = 0
        self.row = 0
        self.col = 0

        random.seed = seed

        self.init_board()
        self.actdict = {
            'w' : self.up_move(),
            'a' : self.left_move(),
            's' : self.down_move(),
            'd' : self.right_move()
        }


    def init_board(self)->None:
        self.board = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]


    def generate_rand(self)->None:
        #Makes random value either 2 or 4 like real 2048
        self.val = random.randint(1, 2) * 2

        #Generates random tile to place val onto
        #Regenerates if tile is tile is taken
        self.col = random.randint(0, 3)
        self.row = random.randint(0, 3)
        while not self.has_val(self.col, self.row):
            self.col = random.randint(0, 3)
            self.row = random.randint(0, 3)

    
    def has_val(self, col:int, row:int)->bool:
        if self.board[row][col] == 0:
            return True
        return False


#Random number insertion
    def insert(self)->None:
        self.generate_rand()
        self.board[self.row][self.col] = self.val


#Handlers for all 4 move types
    def left_move(self):
        pass


    def right_move(self):
        pass


    def up_move(self):
        pass


    def down_move(self):
        pass


#Checking for winner or loser
    def check_win(self)->bool:
        for i in self.board:
            if 2048 in i:
                print("You have won!")
                exit()
        return False
    
    def check_loss(self)->bool:
        for i in self.board:
            if 0 in i:
                return False
        print("You lose!")
        exit()

#Advances board state
    def advance_state(self)->None:
        self.get_action()
        self.check_win()
        self.check_loss()


#Get input from user and calls appropriate move function
    def get_action(self)->None:
        while True:
            opt = input("Choose an action: ")
            try:
                self.actdict[opt]
                return
            except:
                print("Invalid Move!")

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
    game.loop(board)

if __name__ == "__main__":
    main()

    