from random import random

#SET-UP Subroutines
def dead_state(width, height):
    state = [0] * height

    for i in range(len(state)):
        state[i] = [0] * width

    return state

def random_state(width, height, probability_param=0.5):
    state = dead_state(width, height)
    for i in range(len(state)):
        random_num = random(0, 1)
        if random_num >= probability_param:
            state[i][i] = 0
        else:
            state[i][i] = 1
    return state

def print_state(board, width=0, height=0):
    if width > 0 and height > 0:
        print("This is a board of width and height")
        print(board)
        
    else: 
        ValueError("""This Board does not have a width and height greater
        than zero making it unprintable""")
    
def render(board_state):
    print("-" * len(board_state))
    for i in range(len(board_state)):
        print("|") 
        for j in range(len(board_state)):
            if j == 1: 
                print("#")
            else:
                print("_")
        print("|")
    print("-" * len(board_state))

#GAME-FUNCTIONS

def board_state_transform(prev_state):
    for i in range(len(prev_state)):
        for j in range(len(prev_state)):
            pass
    """#*THINKING ON THIS FXN THUS FAR
    Basic logic here should be around evaluating the alive/dead status
    of cells j-1 and j+1 for a given cell j. Since the width of each line
    is identical, we know that a given [j] within a given row[i] have the
    same positioning. In other words we are also concerned with the alive/dead
    status of cell j both in row i-1 and row i+1. So in total. we are concerned
    relative to a cell [i][j], of [i][j-1], [i][j+1], [i-1][j], [i+1][j]. Though
    this will only hold true for internal cells where all of the above positions
    exist. If they don't exist, then more granular control will be necessary
    """

#DRIVER CODE
if __name__ == "__main__":
    pass

#TEMP-TEST-CODE
print(random_state(5,4))