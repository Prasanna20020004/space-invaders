from turtle import Turtle

X = -300
Y = 20


class Protector:

    def __init__(self, n):
        self.protectors = []
        self.show_protectors(n)

    def show_protectors(self, number):
        global X, Y
        for i in range(int(number / 10)):
            for j in range(10):
                self.make_protector((X, Y))
                X += 65
            Y -= 25
            X = -300

    def make_protector(self, position):
        protector = Turtle("square")
        protector.color("white")
        protector.speed(0)
        protector.shapesize(stretch_wid=1, stretch_len=3)
        protector.penup()
        protector.goto(position)
        self.protectors.append(protector)

    def remove(self, protector):
        protector.goto(1000, 1000)
        self.protectors.remove(protector)
