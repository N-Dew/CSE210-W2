import random

#main class that plays the game

"""module that directs the game and organizes the other classes parts"""
class Game:
    """ Directing the hilo game process. The game is to control the sequence of play including keeping track of the score.
    Attributes:
        is_playing (boolean): Whether or not the game is being played.
        score (int): The accumulated score for the entire game.
        card (int): A randomly selected card out of 13 total distinct cards (2 for each round)
    """
    # At the start of each game it will reset the variables so the game can be re-played.
    def __init__(self):
        """ Constructs a new Game by creating variable.
        Args:
            self (Game): an instance of Game.
        """
        self.is_playing = True
        self.score = 300
        self.previous = 0
        self.selected = 0

    # Starts the game by running the main game loop "is_playing".
    def start_game(self):
        """ Starts the game by running the main game loop is_playing.
        Args:
            self (Game): An instance of Game.
        """
        card = Card()
        self.selected = card.select_card()
        while self.is_playing:
            self.get_user_input()
            self.do_updates()

    # Ask the user if they want to guess higher or lower. Updates score
    # depending on whether the user guessed correctly.
    def get_user_input(self):
        """ Ask the user if they want to guess higher or lower. 
        Updates score depending on whether the user guessed correctly.
        Args:
            self(Game): An instance of Game.
        """
        print()
        input_loop = ""
        while input_loop != True:
            print(f"The Card is : {self.selected}")
            pick_card = input("Higher or Lower? [h, l]  ")
            if pick_card.lower() == "h" or pick_card.lower() == "l":
                pick_card = pick_card
                input_loop = True
            else:
                print()
                print("Invalid input, please try again (h or l)")
                print()
                input_loop = False

        card = Card()
        self.previous = self.selected

        self.selected = card.select_card()
        while True:
            if self.previous != self.selected:
                break
            else:
                self.selected = card.select_card()
        self.update_score(pick_card)

    # Updates the score based on user's h or l answer.
    def update_score(self, pick_card):
        """
        Update score on based on user's answer.
        Args:
            self(Game): An instance of Game.
            pick_card(str): the user's answer
        """
        if pick_card.lower() == "h" and self.selected > self.previous:
            print(f"Next Card is: {self.selected}")
            print("You selected higher and the card was higher")
            self.score += 100
        elif pick_card.lower() == "l" and self.selected < self.previous:
            print(f"Next Card is: {self.selected}")
            print("You selected lower and the card was lower")
            self.score += 100
        else:
            print(f"Next Card is: {self.selected}")
            self.score -= 75

    # Check score to see if it is 0 or less and print game over, print out the score, 
    # and ask the user if they would like to play again.
    def do_updates(self):
        """
        Check score to see if it is 0 or less and print game over, print out the score, and ask the user if they would like to play again.
        Args:
            self(Game): An instance of Game.
        """
        
        if not self.is_playing:
            return

        if self.score <= 0:
            print("Game Over")
            self.is_playing = False

        print(f"Your score is: {self.score}")
        play_loop = ""
        
        while play_loop != True:
            play_again = input("Play again ? [y/n]: ")
            print()
            if play_again.lower() == "y":
                self.is_playing = True
                return
            elif play_again.lower() == "n":
                self.is_playing = False
                print('Thanks for playing, Goodbye.')
                print()
                return
        print()

# ------------------------------------------------------------

# pulls a new random number

""" Card module for implementing the card class
"""
class Card:
    """
    A rectangular paper with a different number on it's face.
    Card is to pull the next card out of the deck
    Attributes:
        selected (int): The number on the current card displayed.
    """
    # pulls a new random number
    def __init__(self):
        """
        Creates a new Card.
        Args:
            self: (Card): An instance of Card.
        """
        self.selected = 0

    # Select a random number between 1 and 13 and return the card number.
    def select_card(self):
        """
        Select a random card between 1 and 13 and return the card number.
        Args:
            self: (Card): An instance of Card.
        """
        self.selected = random.randint(1, 13)
        return self.selected

# ------------------------------------------------------------
    
"""Module that starts the game"""
print()
print("Welcome to Hi-Lo!")
print()
game = Game()
game.start_game()
