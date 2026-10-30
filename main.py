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


import time
import random
import keyboard

class GameMatrix:
    def __init__(self, dimension):
        self.dimension = dimension
        self.matrix = [[0] * dimension for _ in range(self.dimension)]
        self.score = 0 

    def display_game_grid_and_blocks(self):
        pass


    # spawn two blocks initially
    def start_game(self):
        self.spawn_random_number(self.generate_random_number())
        self.spawn_random_number(self.generate_random_number())
        pass 

    # movements
    def slide_right(self):
        self.merge_blocks_to_the_right()
        self.spawn_random_number()

    def slide_left(self):
        self.merge_blocks_to_the_left()
        self.spawn_random_number()

    def slide_up(self):
        self.merge_blocks_up()
        self.spawn_random_number()

    def slide_down(self):
        self.merge_blocks_down()
        self.spawn_random_number()

    
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
               
                j = 0
                while j < self.dimension:
                    for k in range(j + 1, self.dimension):
                            if (self.matrix[i][j] > 0 and self.matrix[i][k] > 0) and (self.matrix[i][j] != self.matrix[i][k]): # skip different numbers greater than 0
                                  break
                            elif (self.matrix[i][j] > 0 and self.matrix[i][k] > 0) and self.matrix[i][j] == self.matrix[i][k]: # merge
                                  self.matrix[i][j] = self.matrix[i][j] + self.matrix[i][k] # merge the block
                                  self.matrix[i][k] = 0 # remove the merged number
                                  break 
                            elif self.matrix[i][j] == 0 and self.matrix[i][k] > 0:
                                  self.matrix[i][j] = self.matrix[i][k] # move the number to the empty space
                                  self.matrix[i][k] = 0 # remove the moved number
                    j += 1   
            pass 

    def merge_blocks_down(self):
          # if there's a merge:
            # self.add_score()

            for i in range(self.dimension):
               
                j = self.dimension - 1
                while j > 0:
                    for k in range(j - 1, -1, -1):
                            if (self.matrix[j][i] > 0 and self.matrix[k][i] > 0) and (self.matrix[j][i] != self.matrix[k][i]): # skip different numbers greater than 0
                                  break
                            elif (self.matrix[j][i] > 0 and self.matrix[k][i] > 0) and self.matrix[j][i] == self.matrix[k][i]: # merge
                                  self.matrix[j][i] = self.matrix[j][i] + self.matrix[k][i] # merge the block
                                  self.matrix[k][i] = 0 # remove the merged number
                                  break  
                            elif self.matrix[j][i] == 0 and self.matrix[k][i] > 0:
                                  self.matrix[j][i] = self.matrix[k][i] # move the number to the empty space
                                  self.matrix[k][i] = 0 # remove the moved number
                    j -= 1   
            pass 
    
    def merge_blocks_up(self):
          # if there's a merge:
            # self.add_score()

            for i in range(self.dimension):
               
                j = 0
                while j < self.dimension:
                    for k in range(j + 1, self.dimension):
                            if (self.matrix[j][i] > 0 and self.matrix[k][i] > 0) and (self.matrix[j][i] != self.matrix[k][i]): # skip different numbers greater than 0
                                  break
                            elif (self.matrix[j][i] > 0 and self.matrix[k][i] > 0) and self.matrix[j][i] == self.matrix[k][i]: # merge
                                  self.matrix[j][i] = self.matrix[j][i] + self.matrix[k][i] # merge the block
                                  self.matrix[k][i] = 0 # remove the merged number
                                  break  
                            elif self.matrix[j][i] == 0 and self.matrix[k][i] > 0:
                                  self.matrix[j][i] = self.matrix[k][i] # move the number to the empty space
                                  self.matrix[k][i] = 0 # remove the moved number
                    j += 1   
            pass 
    

    # compute score
    def add_score(self):
          pass 

    def generate_random_number(self):
          random_number = random.randint(1, 100)

          if (random_number > 0) and (random_number < 91): # ranges from 1 to 90 (90 percent chance)
               return 2
          else: # ranges from 91 to 100 (10 percent chance)
               return 4

    # only ONE! either a 2 or 4
    def spawn_random_number(self, random_number):

          # record all the empty cells in one array
          empty_cells = []
          for i in range(self.dimension):
               for j in range(self.dimension):
                    if self.matrix[i][j] == 0:
                         empty_cells.append([i, j]) 

          # generate a random number based from the length of the empty cells array
          random_location = random.randint(0, len(empty_cells) - 1)

          a, b = empty_cells[random_number]
          self.matrix[a][b] = random_number

    def two_thousand_forty_eight_block_exist():
          pass 

    def player_is_out_of_moves():
          pass

    def display_matrix(self):
         for row in self.matrix:
              for number in row:
                   print(f"{number:^3}", end = "")
              print()     
          


def main():
    # ask the player for the dimesion
    while True:
        try:
            dimension = int(input("Enter dimension size: "))
            if dimension < 3 or dimension > 8:
                raise ValueError("dimension should be less than 9 and greater than 2")
            else: 
                break 
        except Exception as e:
            print(e)
            time.sleep(2)
            print("\033[1A\r\x1b[2K" * 2, end ="")

    gameMatrix = GameMatrix(dimension)
    gameMatrix.start_game()
    
        
    while True:
        gameMatrix.display_matrix()

        print("\n use arrow keys to slide...")

        

        # ask the player a move (left, right, down and up arrow key)
        key_pressed = keyboard.read_event()

        if key_pressed.name == "left":
            gameMatrix.slide_left()
        elif key_pressed.name == "rigt":
            gameMatrix.slide_right()
        elif key_pressed.name == "up":
            gameMatrix.slide_up()
        elif key_pressed.name == "down":   
            gameMatrix.slide_down()


        # if player_is_out_of_moves():
            # game over
        # elif two_thousand_forty_eight_block_exist():
            # winner !


        # clear the screen then display the grid again and ask the player a move


main()

    
# Functions
# Variables



# SCREEN
""" 
use tabulate
"""


# FLOW