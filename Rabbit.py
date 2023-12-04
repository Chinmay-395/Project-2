# Author: Chinmay Dali, Kartikey Singh
# Date: Nov 20, 2023
# Description: In this file we structure the data for the all the creatures in the field for the game.


from Creature import Creature
# import random

class Rabbit(Creature):
    def __init__(self, x, y):
        """
        Initialize a Rabbit object with specified x and y coordinates.

        :param x: the x-coordinate of the Rabbit on the field.
        : type x: int
        :param y: the y-coordinate of the Rabbit on the field.
        : type y: int
        """
        super().__init__(x, y, "R")  # "R" is the symbol for the Rabbit


