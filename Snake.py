# Author: Chinmay Dali, Kartikey Singh
# Date: Nov 20, 2023
# Description: A snake creature that will move in 4 directions in the field, interacting with other creatures


from Creature import Creature
class Snake(Creature):
    def __init__(self, x, y):
        """
        Initialize a Snake object with specified x and y coordinates.

        :param the x-coordinate of the Snake on the field.
        :type x: int
        :param the y-coordinate of the Snake on the field.
        :type y: int
        """
        super().__init__(x, y, "S")
