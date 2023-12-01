# Author: Chinmay Dali, Kartikey Singh
# Date: Nov 20, 2023
# Description: In this file we structure the data for the all the creatures in the field for the game.


from Creature import Creature
import random

class Rabbit(Creature):
    def __init__(self, x, y):
        """
        Initialize a Rabbit object with specified x and y coordinates.

        :param x: int, the x-coordinate of the Rabbit on the field.
        :param y: int, the y-coordinate of the Rabbit on the field.
        """
        super().__init__(x, y, "R")  # "R" is the symbol for the Rabbit

    def move(self, field_size):
        """
        Move the Rabbit randomly to an adjacent position on the field.

        :param field_size: tuple, the size of the field as (width, height).
        """
        dx, dy = random.choice([(-1, 0), (1, 0), (0, -1), (0, 1)])  # Randomly choose a direction
        new_x = max(0, min(self.get_x() + dx, field_size[0] - 1))  # Ensure the new position is within the field boundaries
        new_y = max(0, min(self.get_y() + dy, field_size[1] - 1))
        self.set_x(new_x)
        self.set_y(new_y)

  
