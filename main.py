from random import randint
from typing import List 

#*TYPE ANNOTATION GLOBAL(S); DO NOT MODIFY
Matrix = List[List[int]]

###SET-UP Subroutines###
def dead_state(width: int, height: int) -> Matrix:
    state = [[0]] * height
    for i in range(len(state)):
        state[i] = [0] * width
    
    return state

def random_state(width: int, height: int, probability_param: float =0.5) -> Matrix:
    state = dead_state(width, height)

    for i in range(len(state)):
        for j in range(len(state[i])):
            random_num = randint(0, 1)
            if random_num >= probability_param:
                state[i][j] = 0
            else:
                state[i][j] = 1

    return state

def print_state(board_state: Matrix) -> None:
    print(f"This board_state is of length{len(board_state)} and width{len(board_state[0])}")
    print(board_state)

def render(board_state: Matrix) -> None:     #O(n^2) time complexity, consider refactoring for efficiency 
    print("-" * len(board_state))
    for i in range(len(board_state[0])):
        x = "|"
        for j in range(len(board_state)):
            if j == 1: 
                x = x + "#"
            else:
                x = x + "_"
        x = x + "|"
        print(x)
    print("-" * len(board_state))

###GAME-FUNCTIONS###
def board_transform(initial_state: Matrix) -> Matrix:
    new_state = dead_state(len(initial_state), len(initial_state[0]))
    for i in range(len(initial_state)):
        for j in range(len(initial_state)):
            pass

    return new_state

    """#*THINKING ON THIS FXN THUS FAR
    Basic logic here should be around evaluating the alive/dead status
    of cells j-1 and j+1 for a given cell j. Since the width of each line
    is identical, we know that a given [j] within a given row[i] have the
    same positioning. In other words we are also concerned with the alive/dead
    status of cell j both in row i-1 and row i+1. So in total. we are concerned
    relative to a cell [i][j], of [i][j-1], [i][j+1], [i-1][j], [i+1][j]. Though
    this will only hold true for internal cells where all of the above positions
    exist. If they don't exist, then you have to exclude the potential neighbors
    which do not exist
    """

#DRIVER CODE
if __name__ == "__main__":
    pass

print(random_state(3,5))