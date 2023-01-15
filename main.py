import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
turtle = Player()
screen.listen()
car = CarManager()
score = Scoreboard()
screen.onkeypress(turtle.move, "Up")
score.update_scoreboard()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move()
    # Detect collision with car
    for cars in car.car_list:
        if cars.distance(turtle) < 26:
            score.game_over()
            game_is_on = False
    # Detect level up
    if turtle.ycor() > 280:
        turtle.reset_position()
        score.update_scoreboard()
        car.increase_movement()
screen.exitonclick()