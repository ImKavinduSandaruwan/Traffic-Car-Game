from turtle import Turtle
LINES_STARTING_POSITIONS = [(-90, -280), (90, -280), (270, -280), (-270, -280)]


class Road:

    def __init__(self):
        self.create_road_lines()

    def create_road_lines(self):
        """Using for loop I created three road line objects"""
        for i in range(4):
            new_line = Turtle()
            self.create_line(new_line, LINES_STARTING_POSITIONS[i])

    def create_line(self, line_number, positions):
        """This will create line. But we need to give start location"""
        line_number.penup()
        line_number.goto(positions)
        line_number.setheading(90)
        for i in range(15):
            line_number.pendown()
            line_number.forward(20)
            line_number.penup()
            line_number.forward(20)
        line_number.hideturtle()
