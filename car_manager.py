from turtle import Turtle
import random
import time
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.car_list = []
        self.car_xcor = 300
        self.shape("blank")
        self.movement_speed = STARTING_MOVE_DISTANCE

    def move(self):
        for car in self.car_list:
            car.forward(self.movement_speed)

    def create_car(self):
        new_car = Turtle()
        new_car.shape("square")
        new_car.penup()
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color(random.choice(COLORS))
        new_car.setheading(180)
        new_car.setposition(self.car_xcor, random.randrange(-250, 250, 75))
        self.car_list.append(new_car)
        self.car_xcor += random.randrange(30, 50, 10)

    def increase_movement(self):
        self.movement_speed += MOVE_INCREMENT


