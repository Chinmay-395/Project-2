# Author: Chinmay Dali, Kartikey Singh
# Date: Nov 20, 2023
# Description: The creature class will define the co-ordinates of the inhabitants of the field inside the 
# field layout

from FieldInhabitant import FieldInhabitant

class Creature(FieldInhabitant):
    def __init__(self, x, y, symbol):
        """
        Initialize a Creature object with specified x and y coordinates and a symbol.

        :param x: the x-coordinate of the creature on the field.
        : type x:int
        :param y: the y-coordinate of the creature on the field.
        : type y:int
        :param symbol: a single character representing the creature on the field.
        : type symbol:str
        """
        super().__init__(symbol)#super class constructor is called
        self.__x = x #the x co-ordinate of the creature
        self.__y = y #the y co-ordinate of the creature

    def get_x(self):
        """
        Get the x-coordinate of the creature.

        :return: int, the x-coordinate of the creature.
        """
        return self.__x

    def set_x(self, x):
        """
        Set or update the x-coordinate of the creature.

        :param x: the new x-coordinate of the creature.
        : type x:int
        """
        self.__x = x

    def get_y(self):
        """
        Get the y-coordinate of the creature.

        :return: int, the y-coordinate of the creature.
        """
        return self.__y

    def set_y(self, y):
        """
        Set or update the y-coordinate of the creature.

        :param y: the new y-coordinate of the creature.
        : type y:int
        """
        self.__y = y
