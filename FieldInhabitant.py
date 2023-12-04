# Author: Chinmay Dali, Kartikey Singh
# Date: Nov 20, 2023
# Description: In this file we structure the data for the all the creatures in the field for the game.

class FieldInhabitant:
    def __init__(self, symbol):
        """
        Constructor for the FieldInhabitant class.
        :param symbol: A character representing the text symbol for the field inhabitant.
        :type symbol: str
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
        :type symbol: str
        """
        self.__symbol = symbol
