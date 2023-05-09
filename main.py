from turtle import Screen
from road import Road
from player import Player
import time
from car_manager import CarManager
from score import Score, Dev

# Setup Screen object
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Traffic Car Game (By Kavindu Sandaruwan)")
screen.tracer(0)

road = Road()  # Creating road object
player = Player()  # Crating player object
car = CarManager()  # Creating car objects
score = Score()  # Creating scoreboard object
dev = Dev()  # Creating developer

screen.listen()
screen.onkey(key="Right", fun=player.move_right)
screen.onkey(key="Left", fun=player.move_left)

is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move()

    car.increase_game_speed()
    score.increase_speed()

    # Detect collision with cars
    for i in car.all_cars:
        if i.distance(player) < 30:
            is_game_on = False
            score.game_over()

screen.exitonclick()
