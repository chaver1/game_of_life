#import_statements
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
    

#GAME-METHODS
def next_board_state(initial_state: int): #stablish rules
    pass

#DRIVER CODE
if __name__ == "__main__":
    pass

#TEMP-TEST-CODE
print(random_state(5,4))