from FieldInhabitant import FieldInhabitant

class Creature(FieldInhabitant):
    def __init__(self, x, y, symbol):
        """
        Initialize a Creature object with specified x and y coordinates and a symbol.

        :param x: int, the x-coordinate of the creature on the field.
        :param y: int, the y-coordinate of the creature on the field.
        :param symbol: str, a single character representing the creature on the field.
        """
        super().__init__(symbol)
        self.__x = x
        self.__y = y

    def get_x(self):
        """
        Get the x-coordinate of the creature.

        :return: int, the x-coordinate of the creature.
        """
        return self.__x

    def set_x(self, x):
        """
        Set or update the x-coordinate of the creature.

        :param x: int, the new x-coordinate of the creature.
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

        :param y: int, the new y-coordinate of the creature.
        """
        self.__y = y

    # Additional methods and functionalities specific to the Creature can be added here.

