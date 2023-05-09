from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        self.speed = 0
        super().__init__()
        self.update_score()

    def update_score(self):
        self.clear()
        self.penup()
        self.goto(-260, 260)
        self.hideturtle()
        self.write(f"Score {int(self.speed)}", align="left", font=("Courier", 20, "bold"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=("Courier", 20, "bold"))

    def increase_speed(self):
        self.speed += 0.2
        self.update_score()


class Dev(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(180, -288)
        self.color("black")
        self.write(f"Developed by Shaggy", align="center", font=("Courier", 10, "bold"))
        self.hideturtle()