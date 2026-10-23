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


""" 

This Dog class has two instance methods:

.description() returns a string displaying the name and age of the dog.
.speak() has one parameter called sound and returns a string containing the dog’s name and the sound that the dog makes.
Save the modified Dog class to a file called dog.py and press F5 to run the program. Then open the interactive window and type the following to see your instance methods in action:

>>> miles = Dog("Miles", 4)

>>> miles.description()
'Miles is 4 years old'

>>> miles.speak("Woof Woof")
'Miles says Woof Woof'

>>> miles.speak("Bow Wow")
'Miles says Bow Wow'
In the above Dog class, .description() returns a string containing information about the Dog instance miles. When writing your own classes, it’s a good idea to have a method that returns a string containing useful information about an instance of the class. However, .description() isn’t the most Pythonic way of doing this.



 """

# Learn from mistakes based from the last project


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age 

    def __str__(self):
        return f"Dog {self.name} is {self.age} years old"

    def speak(self, sound):
        return f"damn: {sound}"

class BullDog(Dog):

    def __init__(self, kill_count):
        self.kill_count = kill_count


    def speak(self):
        return super().speak("BARFFFFF")

cupcake = BullDog( 4)


print(cupcake.speak())



# Classes
    # constructor
    # methods

# Functions
# Variables



# SCREEN
""" 
use tabulate

"""


# FLOW