# Author: Chinmay Dali, Kartikey Singh
# Date: Nov 20, 2023
# Description: In this file we structure the data for the all the creatures in the field for the game.


from Creature import Creature
from Veggie import Veggie

class Captain(Creature):
    def __init__(self, x, y):
        """
        Initialize a Captain object with specified x and y coordinates.
        
        :param : the x-coordinate of the Captain on the field.
        : type x: int
        :param : the y-coordinate of the Captain on the field.
        : type y: int
        """
        super().__init__(x, y, "V")  # "V" is the symbol for the Captain
        self.__collected_veggies = []  # A list to store, collected vegetables

    def addVeggie(self, veggie):
        """
        Add a Veggie object to the list of collected vegetables.

        :param : Veggie, the vegetable to be added to the collection.
        : type veggie: Veggie Object
        """
        if isinstance(veggie, Veggie):
            self.__collected_veggies.append(veggie)

    def get_collected_veggies(self):
        """
        Get the list of collected Veggie objects.

        :return: list of Veggie objects that have been collected.
        """
        return self.__collected_veggies

    def dropVeggie(self):
        """
        If the snake ever attempts to move into the same position as the
        captain, the captain loses the last five vegetables that were added to their basket
        """
        
        self.__collected_veggies = self.__collected_veggies[:-5]
            
