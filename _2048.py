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
            'w' : self.up_move,
            'a' : self.left_move,
            's' : self.down_move,
            'd' : self.right_move
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
        for i in range(1, 4):
            for j in range(0, 3):
                if self.board[j][i-1] == 0:
                    self.board[j][i-1], self.board[j][i] = self.board[j][i], self.board[j][i-1]
                elif self.board[j][i-1] == self.board[j][i]:
                    self.board[j][i-1] *= 2
                    self.board[j][i] = 0

        # for row in self.board:
        #     for i in range(len(row)):    
        #         if row[i] == row[i+1]:
        #             row[i], row[i+1] = row[0]*2, 0
        #         row.remove(0)
        #         row.append(0)
            

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
    
    #Simply checks if all of the tiles are taken up
    #Plan to make this more thorough
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
                self.actdict[opt]()
                print()
                return
            except:
                print("Invalid Move!")
        


def game_init():
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
    game_init()

    