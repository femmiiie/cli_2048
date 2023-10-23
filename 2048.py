#creates 4x4 2048 board
def board_init()->list:
    return [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]


def main(*args):
    #
    if args[0] == "cli":
        import cli as game
    elif args[0] == "gui":
        import gui as game

    