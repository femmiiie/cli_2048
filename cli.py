from time import sleep

def print_board(board:list)->None:
    for i in board:
        for j in i:
            print(j, end=" ")
        print()

def intro()->None:
    print("Welcome to the CLI version of 2048!")
    print("Objective: combine like values to reach 2048 without running out of space")
    print("Controls:")
    print(" w: up")
    print(" a: left")
    print(" s: down")
    print(" d: right")
    sleep(3)


def loop()->None:
    pass