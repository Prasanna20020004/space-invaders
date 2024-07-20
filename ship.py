from turtle import Turtle


class Ship(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color("white")
        self.speed(0)
        self.goto(0, -280)

    def move_left(self):
        self.back(30)

    def move_right(self):
        self.forward(30)
