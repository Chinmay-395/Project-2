# Author: Chinmay Dali, Kartikey Singh
# Date: Nov 20, 2023
# Description: In this file we structure the data for the all the creatures in the field for the game.

# FieldInhabitant.py

class FieldInhabitant:
    def __init__(self, symbol):
        """
        Constructor for the FieldInhabitant class.
        :param symbol: A character representing the text symbol for the field inhabitant.
        """
        self.__symbol = symbol

    def get_symbol(self):
        """
        Getter for the symbol of the field inhabitant.
        :return: The symbol representing the field inhabitant.
        """
        return self.__symbol

    def set_symbol(self, symbol):
        """
        Setter for the symbol of the field inhabitant.
        :param symbol: The new symbol for the field inhabitant.
        """
        self.__symbol = symbol
