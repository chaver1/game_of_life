#Rules of Game of Life
"""
1. Any live cell with <=1 live neighbors becomes dead due to underpop
2. Any life cell with 2 or 3 live neighbors stays alive
3. Any live cell with >3 live neighbors becomes dead due to overpop
4. Any dead cell with exactly 3 live neighbors becomes alive by reproduct

"""
class Game():
    def __init__(self, width: int, height: int):
        self.width = width 
        self.height = height
    
    #SET-UP METHODS
    def dead_state(self):
        self.dead_array = [] * self.height
        for i in range(self.height):
            self.dead_array[i] = [0] * self.width
        return self.dead_array

    def random_state(self, probability_param: float =0.5):
        state = dead_state(self.width, self.height)
        for i in range(len(state)):
            random_num = Random.random(0, 1)
            if random_num >= probability_param:
                state[i] = 0
            else: 
                state[i] = 1
        return state
    
    def print_state(self):
        print("This is a board of width and height")
        print(random_state(self.width, self.height))
    
    def pretty_print_state(self):
        pass

    #GAME-METHODS
    def next_board_state(self, initial_state: int): #stablish rules
        self.initial_state = initial_state

        for i in range(len(self.initial_state)):
            pass
#dataclass to store various states of the board for different games
class Boards():
    def __init__(self):
        pass