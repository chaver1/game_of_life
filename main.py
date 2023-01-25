#import_statements
from random import Random

board = [[1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1], 
        [1, 1, 1, 1, 1, 1, 1], 
        [1, 1, 1, 1, 1, 1, 1], 
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1]] #7x7 Board


#SET-UP METHODS
def dead_state(width, height):
    dead_array = [] * height
    for i in range(height):
        dead_array[i] = [0] * width
        return dead_array

def random_state(width, height, probability_param: float =0.5):
    state: list[list[int]] = dead_state(width, height)
    for i in range(len(state)):
        random_num = random.Random(0, 1)
        if random_num >= probability_param:
            state[i][i] = 0
        else: 
            state[i][i] = 1
        return state
    
def print_state(board, width=False, height=False):
    if width > 0 and height > 0:
        print("This is a board of width and height")
    print(board)
    
def pretty_print_state():
    pass

#GAME-METHODS
def next_board_state(initial_state: int): #stablish rules
    for i in range(len(initial_state)):
        pass

#DRIVER CODE
if __name__ == "__main__":
    pass

#TEMP-TEST-CODE
print(dead_state(5,4))
