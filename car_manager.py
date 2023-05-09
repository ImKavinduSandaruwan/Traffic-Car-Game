from turtle import Turtle
import random
CAR_MOVEMENT = 10
CAR_SPEED_INCREASE = 0.1


class CarManager:

    def __init__(self):
        self.speed = CAR_MOVEMENT
        self.all_cars = []
        self.create_car()

    def create_car(self):
        if random.randint(0, 8) == 5:
            new_car = Turtle(shape="turtle")
            new_car.penup()
            new_car.setheading(90)
            new_car.shapesize(stretch_len=2, stretch_wid=2)
            start_x = random.randint(-260, 260)
            start_y = 280
            new_car.goto(start_x , start_y)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(self.speed)

    def increase_game_speed(self):
        self.speed += CAR_SPEED_INCREASE

