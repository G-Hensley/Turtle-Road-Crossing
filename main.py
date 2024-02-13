import time
from turtle import Screen
from scoreboard import Scoreboard
from car_manager import CarManager
from player import Player

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing")
screen.bgcolor('black')
user = Player()
score_board = Scoreboard()

screen.listen()
screen.onkeypress(fun=user.move, key="Up")

car_manager = CarManager()

car_speed = 0.07
score_board.update_score()
counter = 0
game_is_on = True
while game_is_on:
    time.sleep(car_speed)
    screen.update()
    car_manager.create_cars()
    car_manager.move()
    for car in car_manager.all_cars:
        if user.distance(car) < 25:
            score_board.game_over()
            game_is_on = False

    if user.ycor() >= 280:
        user.new_level()
        score_board.level += 1
        score_board.update_score()
        car_speed *= 0.8

screen.exitonclick()
