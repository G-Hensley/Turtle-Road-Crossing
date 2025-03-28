from turtle import Turtle

# Constants for the player's starting position and movement distance
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

# Player class to manage the player's turtle
class Player(Turtle):

    # Initialize the Player object
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape('turtle')
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)

    # Move the player's turtle forward
    def move(self):
        self.forward(MOVE_DISTANCE)

    # Move the player's turtle to the starting position
    def new_level(self):
        self.goto(STARTING_POSITION)

