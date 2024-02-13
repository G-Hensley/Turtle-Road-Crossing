from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []

    def create_cars(self):
        rand_num = random.randint(1, 6)
        if rand_num == 1:
            new_car = Turtle()
            new_car.shape('square')
            new_car.shapesize(1, 2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.goto(x=320, y=random.randint(-220, 220))
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            new_x = car.xcor() - STARTING_MOVE_DISTANCE
            car.goto(x=new_x, y=car.ycor())


