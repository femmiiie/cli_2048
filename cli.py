from time import sleep
from _2048 import Board

def update(board:list)->None:
    for i in board:
        for j in i:
            print(j, end=" ")
        print()
    print()

def intro()->None:
    print("Welcome to the CLI version of 2048!")
    print("Objective: combine like values to reach 2048 without running out of space")
    print("Controls:")
    print(" w: up")
    print(" a: left")
    print(" s: down")
    print(" d: right\n")
    sleep(2)


def loop(board:Board)->None:
    intro()

    while True:
        board.insert()
        update(board.board)
        board.advance_state()
        update(board.board)
        sleep(1)