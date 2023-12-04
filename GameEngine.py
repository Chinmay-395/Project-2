# Author: Chinmay Dali, Kartikey Singh
# Date: Nov 20, 2023
# Description: In this file we structure the data for the all the creatures in the field for the game.


import random
import os
import pickle
from Veggie import Veggie
from Captain import Captain
from Rabbit import Rabbit
from Snake import Snake

class GameEngine:
    __NUMBEROFVEGGIES = 30
    __NUMBEROFRABBITS = 5
    __HIGHSCOREFILE = "highscore.data"

    def __init__(self):
        """
        Initialize the GameEngine with the necessary components for the game.
        """
        self.__field = []  # A 2D list representing the game field
        self.__rabbits = []  # List of Rabbit objects in the game
        self.__captain = None  # A single Captain object
        self.__possible_veggies = []  # List of possible Veggie objects in the field
        self.__score = 0  # The player's current score
        self.__snake = None # the snake is a single object in the entire game
        self.__temp = None # this member variable will store object where-ever location overlap happen

        

    def initVeggies(self):
        """
        Initialize the game field with vegetables. The user is prompted for the name of the veggie file.
        The field is initialized to a 2D list based on the file, and Veggie objects are added at random locations.
        """
        while True:
            #this is for debugging purposes
            # veggie_file ="/home/chinmay/Coding/Courses/AAI-Engineering-Python/project-2/VeggieFile1.csv" #currently only for debugging
            veggie_file = input("Enter the name of the veggie file: ")
            try:
                with open(veggie_file, 'r') as file:
                    lines = file.readlines()
                    the_field_line = lines[0].strip().split(',')
                    field_dimensions = [int(the_field_line[1]),int(the_field_line[2])]#the x,y plane
                    
                    self.__field = [[None]*field_dimensions[1] for _ in range(field_dimensions[0])]
                    
                    # Initialize the list of possible vegetables
                    for line in lines[1:]:
                        name, symbol, points = line.strip().split(',')
                        the_veggie_obj = Veggie(name, symbol, int(points))
                        self.__possible_veggies.append(the_veggie_obj)

                    # Randomly place vegetables on the field
                    for _ in range(GameEngine.__NUMBEROFVEGGIES):
                        veggie = random.choice(self.__possible_veggies)
                        while True:
                            #If a chosen random location is occupied by another Veggie object, repeatedly
                            #choose a new location until an empty location is found
                            x, y = random.randint(0, field_dimensions[0] - 1), random.randint(0, field_dimensions[1] - 1)
                            if self.__field[x][y] is None:
                                self.__field[x][y] = veggie
                                break
                    break#this will break out of the loop for incorrect file names
            except FileNotFoundError:
                print("File not found. Please try again.")

    def initCaptain(self):
        """
        Initialize the Captain in the game. A random location is chosen for the Captain object.
        If the chosen location is occupied, a new location is selected until an empty one is found.
        """
        field_width = len(self.__field)
        field_height = len(self.__field[0])
        print(f" wid: {field_width} hei:{field_height}")
        while True:
            x, y = random.randint(0, field_width - 1), random.randint(0, field_height - 1)
            print("x, y ",x, "\t",y)
            if self.__field[x][y] is None:
                self.__captain = Captain(x, y)
                self.__field[x][y] = self.__captain
                break

    def initRabbits(self):
        """
        Initialize Rabbit objects in the game. For each Rabbit, a random location is chosen.
        If the chosen location is occupied, a new location is selected until an empty one is found.
        The Rabbit objects are then added to a list of Rabbits and assigned to their locations in the field.
        """
        field_width = len(self.__field)
        field_height = len(self.__field[0])

        for _ in range(GameEngine.__NUMBEROFRABBITS):
            while True:
                x, y = random.randint(0, field_width - 1), random.randint(0, field_height - 1)
                if self.__field[x][y] is None:
                    rabbit = Rabbit(x, y)
                    self.__rabbits.append(rabbit)
                    self.__field[x][y] = rabbit
                    break
    
    def initSnake(self):
        """
        Initialize Snake objects in the game. A random location is chosen.
        If the chosen location is occupied, a new location is selected until an empty one is found.
        The Rabbit objects are then added to a list of Rabbits and assigned to their locations in the field.
        """
        field_width = len(self.__field)
        field_height = len(self.__field[0])

        while True:
            x, y = random.randint(0, field_width - 1), random.randint(0, field_height - 1)
            if self.__field[x][y] is None:
                self.__snake = Snake(x, y)
                self.__field[x][y] = self.__snake
                break

    

    def initializeGame(self):
        """
        Initialize the entire game including vegetables, Captain, and Rabbits.
        """
        self.initVeggies()
        self.initCaptain()
        self.initRabbits()
        self.initSnake()

    def remainingVeggies(self):
        """
        Count the number of Veggie objects remaining on the field.

        :return: int, the count of remaining Veggie objects.
        """
        count = 0
        for row in self.__field:
            for item in row:
                if isinstance(item, Veggie):
                    count += 1
        return count

    def intro(self):
        """
        Display the introduction to the game, including the welcome message, game premise, goals,
        and information about the vegetables, Captain, and rabbits.
        """
        print("Welcome to Captain Veggie!")
        print("The rabbits have invaded your garden and you must harvest ")
        print("as many vegetables as possible before the rabbits eat them ")
        print("all! Each vegetable is worth a different number of points")
        
        
        print("In this game, you are Captain Veggie, trying to collect as many vegetables as possible while avoiding rabbits and snakes.")
        print("Your goal is to gather vegetables from the garden, each worth different point values, and achieve the highest score.\n")

        print("so go for the high score!")
        
        print("List of Possible Vegetables:")
        for veggie in self.__possible_veggies:
            print(f"- {veggie.__str__()}")
            # print(f" - {veggie.get_symbol()}: {veggie.get_name()}, Points: {veggie.get_points()}")

        print("\nGame Characters:")
        print(f" - Captain Veggie's Symbol: 'V'")
        print(f" - Rabbit's Symbol: 'R'")
        print("\nGood luck, and watch out for those rabbits!")

    def printField(self):
        """
        Display the contents of the field in a 2D grid format with a border around the entire grid.
        """
        # Print the top border
        print("#" + "#" * (len(self.__field[0]) * 2) + "#")

        for row in self.__field:
            # Print the row contents with left and right borders
            print("#" + " ".join(item.get_symbol() if item else " " for item in row) + "#")

        # Print the bottom border
        print("#" + "#" * (len(self.__field[0]) * 2) + "#")
        
    def getScore(self):
        """
        This will return the current points earned by the user
        that takes in no parameters and returns the current score
        
        :Returns (int): the current score accumulated by the user
        """
        # for veg in self.__captain.get_collected_veggies():
        #     if isinstance(veg, Veggie):
        #         self.__score += veg.get_points()
        return self.__score

    def moveRabbits(self):
        """
        Move each Rabbit object in the list of rabbits up to 1 space in a random x,y direction.
        Rabbits cannot move outside the field boundaries or into spaces occupied by other Rabbits or the Captain.
        If a Rabbit moves into a space occupied by a Veggie, the Veggie is removed and the Rabbit takes its place.
        """
        #the rabbit could move 1 space up, down, left, right, any diagonal direction,
        #or possibly not move at all
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1), (0, 0)]  # Includes all 8 directions and no move
        field_width = len(self.__field)
        field_height = len(self.__field[0])

        for rabbit in self.__rabbits:
            dx, dy = random.choice(directions)
            new_x, new_y = rabbit.get_x() + dx, rabbit.get_y() + dy
            #Rabbit object attempts to move outside the boundaries of field it will
            #forfeit its move
            if 0 <= new_x < field_width and 0 <= new_y < field_height: # Check for field boundaries
                # If a Rabbit object attempts to move into a space occupied by another Rabbit
                # object or a Captain object it will forfeit its move
                # Check for other Rabbits or the Captain or Snake at the new location
                if not (isinstance(self.__field[new_x][new_y], Rabbit) or 
                        isinstance(self.__field[new_x][new_y], Captain) or 
                        isinstance(self.__field[new_x][new_y], Snake)
                        ):
                    # If a Rabbit object moves into a space occupied by a Veggie object, that
                    # Veggie object is removed from field, and the Rabbit object will take its
                    # place in field
                    # If moving to a Veggie, remove it from the field
                    if isinstance(self.__field[new_x][new_y], Veggie):
                        # print(f"RABBIT ATE THE VEGGIE AT X:{new_x} and Y:{new_y}")
                        self.__field[new_x][new_y] = None

                    # Move the rabbit
                    self.__field[rabbit.get_x()][rabbit.get_y()] = None  # Set previous location to None
                    rabbit.set_x(new_x)
                    rabbit.set_y(new_y)
                    self.__field[new_x][new_y] = rabbit
    
    def capMovedIntoSnake(self, x, y):
        """
        If the captain object moved into the space of snake, instead of making the spce None
        it should be stored since snake object currently occupies it. 
        This is done to avoid disappearnce of snake object when captain moves into it's position
        
        :param x: The x cordinate where the captain should move into
        :type int:
        :param y: The y cordinate where the captain should move into
        :type int:
        :returns: nothing
        """
        self.__temp = self.__snake
        cap_prev_pos_x = self.__captain.get_x()
        cap_prev_pos_y = self.__captain.get_y()
        self.__captain.set_x(x)
        self.__captain.set_y(y)
        self.__field[x][y] = self.__captain
        self.__field[cap_prev_pos_x][cap_prev_pos_y] = None  # Set previous location to None
    def moveCptVertical(self, vertical_movement):
        """
        Move the Captain vertically based on the input movement value.
        
        :param vertical_movement: int, the vertical movement value for the Captain.
        """
        new_x = self.__captain.get_x()+ vertical_movement
        new_y = self.__captain.get_y() 
        # print(f"CAPS NEW POS X: {new_x} Y:{new_y}")
        # Check if new position is within field boundaries
        if 0 <= new_x < len(self.__field) and 0 <=new_y<len(self.__field[0]):
            current_object = self.__field[new_x][new_y]

            # Check if new position has a Rabbit object
            if isinstance(current_object, Rabbit):
                print("You should not step on the rabbits. Stay where you are.")
                
            elif (isinstance(current_object, Snake)):
                # print("Moved into place occupied by snake.(Vertical)")
                self.capMovedIntoSnake(new_x,new_y)
                
            elif (current_object is None):
                self.__field[self.__captain.get_x()][self.__captain.get_y()] = None  # Set previous location to None
                self.__captain.set_x(new_x)
                self.__field[new_x][new_y] = self.__captain

            # Check if new position has a Veggie object
            elif isinstance(current_object, Veggie):
                self.__field[self.__captain.get_x()][self.__captain.get_y()] = None  # Set previous location to None
                self.__captain.set_x(new_x)
                self.__captain.addVeggie(current_object)
                print(f"Yummy! A delicious vegetable {current_object.get_name()}")
                self.__score += current_object.get_points()
                self.__field[new_x][new_y] = self.__captain

            else:
                #this signifies that the position is occupied by object which is not part of the game
                print("Captain movement is incorrect")
                exit(-1)

    def moveCptHorizontal(self, horizontal_movement):
        """
        Move the Captain horizontally based on the input movement value.
        
        :param horizontal_movement: int, the horizontal movement value for the Captain.
        """
        new_x = self.__captain.get_x() 
        new_y = self.__captain.get_y()+ horizontal_movement
        # print(f"CAPS NEW POS X: {new_x} Y:{new_y}")
        # Check if new position is within field boundaries
        if 0 <= new_x < len(self.__field) and 0 <=new_y<len(self.__field[0]):
            current_object = self.__field[new_x][new_y]
            
            # Check if new position has a Rabbit object
            if isinstance(current_object, Rabbit):
                print("You should not step on the rabbits. Stay where you are.")
                
            elif isinstance(current_object, Snake):
                # print("Moved into place occupied by snake.(Horizontal)")
                self.capMovedIntoSnake(new_x,new_y)
                
            elif (current_object is None):
                self.__field[self.__captain.get_x()][self.__captain.get_y()] = None  # Set previous location to None
                self.__captain.set_y(new_y)
                self.__field[new_x][new_y] = self.__captain    

            # Check if new position has a Veggie object
            elif isinstance(current_object, Veggie):
                self.__field[self.__captain.get_x()][self.__captain.get_y()] = None  # Set previous location to None
                self.__captain.set_y(new_y)
                self.__captain.addVeggie(current_object)
                print(f"Yummy! A delicious vegetable {current_object.get_name()}")
                self.__score += current_object.get_points()
                self.__field[new_x][new_y] = self.__captain
                
            # Check if new position is empty
            else:
                print("Captains movement is incorrect")
                exit(-1)


            

    def moveCaptain(self):
        """
        Prompt the user for a direction to move the Captain (Up, Down, Left, Right).
        Move the Captain based on the user input and the game's rules.
        """
        
        while True:
            direction = input("Move Captain (W/A/S/D): ").upper()
            if direction == "W":
                if self.__captain.get_x() -1 >= 0:  # Check if move is within upper boundary
                    self.moveCptVertical(-1)
                else:
                    print("Cannot move that way. The edge of the field is there.")
                break

            elif direction == "S":
                if self.__captain.get_x() + 1 < len(self.__field):  # Check if move is within lower boundary
                    self.moveCptVertical(1)
                else:
                    print("Cannot move that way. The edge of the field is there.")
                break

            elif direction == "A":
                if self.__captain.get_y()-1 >= 0:  # Check if move is within left boundary
                    self.moveCptHorizontal(-1)
                else:
                    print("Cannot move that way. The edge of the field is there.")
                break

            elif direction == "D":
                if self.__captain.get_y()+1 < len(self.__field[0]):  # Check if move is within right boundary
                    self.moveCptHorizontal(1)
                else:
                    print("Cannot move that way. The edge of the field is there.")
                break

            else:
                print("Invalid input. Please use 'W or w', 'A or a', 'S or s', OR 'D or d' for movement.")


    def resetSnake(self):
        """
        Reset the snake to a new random, unoccupied position on the field.
        """
        field_width = len(self.__field)
        field_height = len(self.__field[0])
        
        while True:
            x, y = random.randint(0, field_width - 1), random.randint(0, field_height - 1)
            if self.__field[x][y] is None:
                if self.__temp is None:
                    self.__field[self.__snake.get_x()][self.__snake.get_y()] = None  # Clear the old position
                else:
                    print("Do not clear the old position where captains is ")# self.__field[self.__temp.get_x()][self.__temp.get_y()] = None  # Clear the old position
                self.__snake.set_x(x)
                self.__snake.set_y(y)
                self.__field[x][y] = self.__snake
                break
        
        if self.__temp is not None:
            # self.__snake = self.__temp
            self.__temp = None
        
    def moveSnake(self):
        """
        The snake can only move up, down, left, or right (not diagonally), cannot move out of the field, 
        and cannot move into a space occupied by a vegetable or a rabbit. When the snake moves, it must always try to move closer
        to the captain object’s position. If the snake ever attempts to move into the same position as the
        captain, the captain loses the last five vegetables that were added to their basket and the snake is
        reset to a new random, unoccupied position on the field.
        """
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0),(0,0)]
        best_move = None
        min_distance = 1e9

        # Find the move that brings the snake closest to the captain
        for dx, dy in directions:
            if self.__temp is None:
                new_x, new_y = self.__snake.get_x() + dx, self.__snake.get_y() + dy
            else:# that means captain moved into the snake position
                new_x, new_y = self.__temp.get_x() + dx, self.__temp.get_y() + dy
            if 0 <= new_x < len(self.__field) and 0 <= new_y < len(self.__field[0]):  # Check if within field
                # if not (isinstance(self.__field[new_x][new_y], Veggie) or isinstance(self.__field[new_x][new_y], Rabbit)):
                distance = abs(new_x - self.__captain.get_x()) + abs(new_y - self.__captain.get_y())
                if distance < min_distance:
                    min_distance = distance
                    best_move = (new_x, new_y)
                    
        

        if best_move:
            final_x, final_y = best_move
            #forfiet the move if rabbit and veggie
            # print(f"THE NEW LOCATION OF THE SNAKE IS X:{final_x} Y:{final_y}")
            if (isinstance(self.__field[final_x][final_y], Rabbit)) or (isinstance(self.__field[final_x][final_y], Veggie)):
                final_x, final_y = self.__snake.get_x(), self.__snake.get_y()
                self.__field[final_x][final_y] = self.__snake
                pass
            # If snake moves to captain's position
            elif (isinstance(self.__field[final_x][final_y], Captain)):
                #captain moved into the position of snake
                # if min_distance == 0 or ((final_x == self.__captain.get_x()) and (final_y==self.__captain.get_y())):
                #     print(f"Cap moved into snake at X:{final_x} Y:{final_y}")
                    
                # else:    
                #     print(f"Snake moved to captain with snake at X:{final_x} Y:{final_y}")
                the_veggie_list = self.__captain.get_collected_veggies()
                for _ in range(5):# Removes the last 5 element
                    if len(the_veggie_list)>0:
                        the_dropped_veg = the_veggie_list.pop()  
                        self.__score -= the_dropped_veg.get_points()
                        print(f"Dropped veggie {the_dropped_veg} ")
                self.__captain.dropVeggie()  # Remove the last 5 veggies
                
                self.resetSnake()  # to reset snake to a new random position
            else: # the only thing that is remaining is None in the else case
                # Move the snake
                self.__field[self.__snake.get_x()][self.__snake.get_y()] = None  # Clear the old position
                self.__snake.set_x(final_x)
                self.__snake.set_y(final_y)
                self.__field[final_x][final_y] = self.__snake
                    
                        
    def gameOver(self):
        """
        Display the game over message, list all harvested vegetables, and show the player's final score.
        """
        print("\nGame Over!")
        print("Congratulations on completing the game.")
        print("\nVegetables Harvested:")

        if self.__captain.get_collected_veggies():
            for veggie in self.__captain.get_collected_veggies():
                print(f" - {veggie.get_name()}")
        else:
            print("No vegetables were harvested.")

        print(f"\nYour Final Score: {self.__score}")

    def highScore(self):
        """
        Manage and update the high scores. Read from and write to a highscore.data file, 
        update the list with the current player's score, and display the high scores.
        """
        high_scores = []

        # Check if the highscore file exists and read it
        if os.path.exists(GameEngine.__HIGHSCOREFILE):
            with open(GameEngine.__HIGHSCOREFILE, 'rb') as file:
                high_scores = pickle.load(file)

        # Get player initials
        initials = input("Enter your initials: ")[:3]

        # Update the high scores list
        new_score = (initials, self.__score)
        if not high_scores:
            high_scores.append(new_score)
        else:
            high_scores.append(new_score)
            high_scores.sort(key=lambda x: x[1], reverse=True)  # Sort the list in descending order of scores

        # Display the high scores
        print("\nHigh Scores:")
        for score in high_scores:
            print(f"{score[0]}: {score[1]}")

        # Write the updated high scores back to the file
        with open(GameEngine.__HIGHSCOREFILE, 'wb') as file:
            pickle.dump(high_scores, file)