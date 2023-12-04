# Author: Chinmay Dali, Kartikey Singh
# Date: Nov 20, 2023
# Description: The game includes a field wherein veggies are the points the user collects. 

from FieldInhabitant import FieldInhabitant

class Veggie(FieldInhabitant):
    def __init__(self, name, symbol, points):
        """
        Constructor for the Veggie class.
        :param name: A string representing the name of the vegetable.
        :type name: str
        :param symbol: A character representing the text symbol for the vegetable.
        :type symbol: str
        :param points: An integer representing the number of points the vegetable is worth.
        :type points: int
        """
        super().__init__(symbol) #symbol from `fieldInhabitants` class
        self.__name = name  #name
        self.__points = points #points value

    def __str__(self):
        """
        Overrides the string representation of the Veggie object.
        :return: A string representing the Veggie in an easy to read format.
        """
        
        return f"{self.get_symbol()}: {self.__name}, {self.__points} points"

    # Getter and Setter for name
    def get_name(self):
        """
        This will fetch the name of the veggie
        :return name of the veggie
        :type : str
        """
        return self.__name

    def set_name(self, name):
        """
        This will set the name of the veggie
        
        :param name: name of the veggie given by the user
        :type name: str
        :return: nothing
        """
        self.__name = name

    # Getter and Setter for points
    def get_points(self):
        """
        This will fetch the points that a user can earn for collecting the veggie
        :return points: of the veggie
        :type (str)
        """
        return self.__points

    def set_points(self, points):
        """
        This will set the name of the veggie
        
        :param name: name of the veggie given by the user
        :type name: str
        :return: nothing
        """
        self.__points = points
