# Understand how the game works
""" 4 x 4
    # Initially: two values are in the grid -> location is random
        # 2 being 90%
        # 4 being 10%
    
    # Possible moves 
        # Slide up
        # slide down
        # slide left
        # slide right
    
        # Two scenarios -> Blocks that move | blocks that stay
            # Blocks stay if it's on the corder of the grid || there is a block adjacent to it that can't move
            # Blocks move if there are cells to move into

    # Merging of N pairs
        # they are adjacent to each other
        # they are the same value
        # they move, and in the same direction


    # Every slide a new value is spawned randomly
        # either a 2 or 4, same percentage 2 being 90% and 4 being 10 percent
    
    # Every time the user slides -> a single number spawns -> each spawn on the grid is random

    # You win if you have a tile/value of 2048

"""


# Learn OOP 

# TODO Learn from mistakes based from the last project



 # TODO: Double check if the logic of the merging is correct
# Classes
    # constructor
    # methods


class GameMatrix:
    def __init__(self, dimension):
        self.dimension = dimension
        self.matrix = [[4, 2, 4, 2, 4, 0, 0 , 0], 
                       [16, 8, 4, 2, 0, 0, 0, 0], 
                       [2, 2, 4, 4, 6, 0, 0 , 0], 
                       [6, 2, 2, 8, 8, 0, 0 , 0], 
                       [2, 2, 9, 2, 0, 0, 0 , 0],
                       [2, 2, 9, 2, 0, 0, 0 , 0],
                       [2, 2, 9, 2, 0, 0, 0 , 0],
                       [2, 2, 9, 2, 0, 0, 0 , 0]]
        self.score = 0 


    # spawn two blocks initially
    def start_game():
        # loading the matrix
        # spawn two blocks in a random location, each block is either a 2 or a 4
        pass 

    # movements
    def slide_right(self):
        self.move_blocks_to_the_right()
        self.spawn_random_number()
        pass

    def slide_left(self):
            pass

    def slide_up(self):
            pass

    def slide_down(self):
            pass

    
    # merges the blocks
    def merge_blocks_to_the_right(self):
          # if there's a merge:
            # self.add_score()

            for i in range(self.dimension):
               
                j = self.dimension - 1
                while j > 0:
                    for k in range(j - 1, -1, -1):
                            if (self.matrix[i][j] > 0 and self.matrix[i][k] > 0) and (self.matrix[i][j] != self.matrix[i][k]): # skip different numbers greater than 0
                                  break
                            elif (self.matrix[i][j] > 0 and self.matrix[i][k] > 0) and self.matrix[i][j] == self.matrix[i][k]: # merge
                                  self.matrix[i][j] = self.matrix[i][j] + self.matrix[i][k] # merge the block
                                  self.matrix[i][k] = 0 # remove the merged number
                                  break 
                            elif self.matrix[i][j] == 0 and self.matrix[i][k] > 0:
                                  self.matrix[i][j] = self.matrix[i][k] # move the number to the empty space
                                  self.matrix[i][k] = 0 # remove the moved number
                    j -= 1   
            pass 
    
    def merge_blocks_to_the_left(self):
          # if there's a merge:
            # self.add_score()

            for i in range(self.dimension):
               
                j = self.dimension - 1
                while j > 0:
                    for k in range(j - 1, -1, -1):
                            if (self.matrix[i][j] > 0 and self.matrix[i][k] > 0) and (self.matrix[i][j] != self.matrix[i][k]): # skip different numbers greater than 0
                                  break
                            elif (self.matrix[i][j] > 0 and self.matrix[i][k] > 0) and self.matrix[i][j] == self.matrix[i][k]: # merge
                                  self.matrix[i][j] = self.matrix[i][j] + self.matrix[i][k] # merge the block
                                  self.matrix[i][k] = 0 # remove the merged number
                                  break 
                            elif self.matrix[i][j] == 0 and self.matrix[i][k] > 0:
                                  self.matrix[i][j] = self.matrix[i][k] # move the number to the empty space
                                  self.matrix[i][k] = 0 # remove the moved number
                    j -= 1   
            pass 


    # compute score
    def add_score(self):
          pass 

    # only ONE! either a 2 or 4
    def spawn_random_number():
          pass 

    def two_thousand_forty_eight_block_exist():
          pass 

    def player_is_out_of_moves():
          pass
          


def main():
    # ask the player for the dimesion

    # while True
        # display the n x n grid with two blocks


        # ask the player a move (left, right, down and up arrow key)
        # if left:
            # slide_left
        # elif right:
            # slide_right
        # elif up:
            # slide_up
        # elif down:   
            # slide_down  


        # if player_is_out_of_moves():
            # game over
        # elif two_thousand_forty_eight_block_exist():
            # winner !


        # clear the screen then display the grid again and ask the player a move

    threeBythree = GameMatrix(8)  

    print(f"before: {threeBythree.matrix}")

    threeBythree.merge_blocks_to_the_right()
    
    print(f"after: {threeBythree.matrix}")
        

main()
    
# Functions
# Variables



# SCREEN
""" 
use tabulate
"""


# FLOW