from turtle import Turtle
FONT = ("Courier", 24, "normal")

# Scoreboard class to manage the scoreboard
class Scoreboard(Turtle):

    # Initialize the Scoreboard object
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("chartreuse")
        self.penup()
        self.goto(-280, 260)
        self.level = 1

    # Update the scoreboard
    def update_score(self):
        self.clear()
        self.write(arg=f"Level: {self.level}", font=FONT)

    # Display the game over message
    def game_over(self):
        self.goto(-80, 260)
        self.write(arg="Game Over.", font=FONT)
