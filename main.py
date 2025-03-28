import time
from turtle import Screen
from scoreboard import Scoreboard
from car_manager import CarManager
from player import Player

# Screen setup and configuration
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing")
screen.bgcolor('black')
user = Player()
score_board = Scoreboard()

# Event listener setup
screen.listen()
screen.onkeypress(fun=user.move, key="Up")

# Initialize car manager and game variables
car_manager = CarManager()
car_speed = 0.07
score_board.update_score()
counter = 0
game_is_on = True

# Main game loop
while game_is_on:
    time.sleep(car_speed)
    screen.update()
    car_manager.create_cars()
    car_manager.move()

    # Check for collision with cars
    for car in car_manager.all_cars:
        if user.distance(car) < 25:
            score_board.game_over()
            game_is_on = False

    # Check if player has reached the top of the screen
    if user.ycor() >= 280:
        user.new_level()
        score_board.level += 1
        score_board.update_score()
        car_speed *= 0.8

# Exit the game when the player clicks the screen
screen.exitonclick()
