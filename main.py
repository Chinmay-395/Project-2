# Author: Chinmay Dali, Kartikey Singh
# Date: Nov 20, 2023
# Description: In this file we structure the data for the all the creatures in the field for the game.


from GameEngine import GameEngine

def main():
    """
    Main function to run the Veggie Garden Game. Handles the overall game flow,
    interactions, and calls the necessary functions from the GameEngine class.
    """
    # Instantiate a GameEngine object
    game = GameEngine()

    # Initialize the game
    game.initializeGame()

    # Display the game's introduction
    game.intro()

    # Initialize the number of remaining vegetables
    remaining_veggies = game.remainingVeggies()

    # Game loop
    while remaining_veggies > 0:
        print(f"\nRemaining Vegetables: {remaining_veggies}")
        print(f"Player's Score: {game.getScore()}")

        # Print out the field
        game.printField()
        
        # Move the captain
        game.moveCaptain() #ask professor about this
        
        # Move the snake
        game.moveSnake()

        # Move the rabbits
        game.moveRabbits()
        
        

        

        # Determine the new number of remaining vegetables
        remaining_veggies = game.remainingVeggies()

    # Display Game Over information
    game.gameOver()

    # Handle High Score functionality
    game.highScore()

if __name__ == "__main__":
    main()
