from turtle import Turtle

X = -300
Y = 210
DISTANCE = 10


class Invader:

    def __init__(self, n):
        self.invaders = []
        self.show_invaders(n)
        self.head = self.invaders[0]

    def show_invaders(self, number):
        global X, Y
        for i in range(number):
            self.make_invader((X, Y))
            X += 65

    def make_invader(self, position):
        invader = Turtle("square")
        invader.color("white")
        invader.speed(0)
        invader.shapesize(stretch_wid=1, stretch_len=1)
        invader.penup()
        invader.goto(position)
        self.invaders.append(invader)

    def remove(self, invader):
        self.invaders.remove(invader)
        invader.goto(1000, 1000)
