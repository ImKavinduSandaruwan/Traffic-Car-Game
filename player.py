from turtle import Turtle
PLAYER_STARTING_POSITION = (0, -270)


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(PLAYER_STARTING_POSITION)
        self.setheading(90)
        self.shape('turtle')
        self.shapesize(stretch_wid=2, stretch_len=2)
        self.color("red")

    def move_right(self):
        new_x = self.xcor() + 10
        new_y = self.ycor()
        self.goto(new_x, new_y)

    def move_left(self):
        new_x = self.xcor() - 10
        new_y = self.ycor()
        self.goto(new_x, new_y)
