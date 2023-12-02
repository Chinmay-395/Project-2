# Author: Chinmay Dali, Kartikey Singh
# Date: Nov 20, 2023
# Description: In this file we structure the data for the all the creatures in the field for the game.


from Creature import Creature
from Veggie import Veggie

class Captain(Creature):
    def __init__(self, x, y):
        """
        Initialize a Captain object with specified x and y coordinates.
        
        :param x: int, the x-coordinate of the Captain on the field.
        :param y: int, the y-coordinate of the Captain on the field.
        """
        super().__init__(x, y, "V")  # "V" is the symbol for the Captain
        self.__collected_veggies = []  # A list to store, collected vegetables

    def addVeggie(self, veggie):
        """
        Add a Veggie object to the list of collected vegetables.

        :param veggie: Veggie, the vegetable to be added to the collection.
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
        print("Captain in contact with snake ")
        for _ in range(5):# Removes the last 5 element
            the_dropped_veg = self.__collected_veggies.pop()  
            print(f"Dropped veggie {the_dropped_veg} ")
        
            

    # def display_status(self):
    #     """
    #     Display the current status of the Captain, including collected veggies.
    #     """
    #     print(f"Captain's Position: ({self.get_x()}, {self.get_y()})")
    #     print("Collected Veggies:")
    #     for veggie in self.__collected_veggies:
    #         print(f" - {veggie}")

