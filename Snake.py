# Author: Chinmay Dali, Kartikey Singh
# Date: Nov 20, 2023
# Description: A snake creature that will move in 4 directions in the field, interacting with other creatures


from Creature import Creature
class Snake(Creature):
    def __init__(self, x, y):
        super().__init__(x, y, 'S')
