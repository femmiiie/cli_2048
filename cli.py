def print_board(board:list)->None:
    for i in board:
        for j in i:
            print(j, end=" ")
        print()