import time
import random as rnd
from turtle import Screen, Turtle
from protector import Protector
from invaders import Invader
from bullet import Bullet
from ship import Ship

user_bullets = []
invader_bullets = []


def game_over():
    over = Turtle()
    over.hideturtle()
    over.teleport(0, 150)
    over.color("red")
    over.write("Game Over", font=("Arial", 30, "bold"))


def make_user_bullet():
    x = ship.xcor()
    y = ship.ycor()
    new_bullet = Bullet()
    new_bullet.teleport(x, y)
    new_bullet.left(90)
    user_bullets.append(new_bullet)


def make_invader_bullet():
    random_invader = rnd.choice(invader.invaders)
    a = random_invader.xcor()
    b = random_invader.ycor()
    new_invader_bullet = Bullet()
    new_invader_bullet.teleport(a, b)
    new_invader_bullet.right(90)
    invader_bullets.append(new_invader_bullet)


screen = Screen()
screen.title("Space Invaders")
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.tracer(0)

protector = Protector(30)
invader = Invader(10)
ship = Ship()

screen.listen()
screen.onkey(key="Up", fun=make_user_bullet)
screen.onkey(key="Left", fun=ship.move_left)
screen.onkey(key="Right", fun=ship.move_right)

game_on = True
while game_on:
    screen.update()
    time.sleep(0.01)

    for bullet in user_bullets:
        bullet.forward(20)
        if bullet.ycor() > 290:
            bullet.goto(1000, 1000)
            user_bullets.remove(bullet)

        for a_protector in protector.protectors:
            if bullet.distance(a_protector) < 30:
                protector.remove(a_protector)

        for a_invader in invader.invaders:
            if bullet.distance(a_invader) < 30:
                invader.remove(a_invader)

        if len(invader.invaders) == 0:
            game_over()
            game_on = False

    r = rnd.randint(1, 100)
    if r == 50:
        make_invader_bullet()

    for i_bullet in invader_bullets:
        i_bullet.forward(20)
        if i_bullet.ycor() < -290:
            i_bullet.goto(1000, 1000)
            invader_bullets.remove(i_bullet)

        for obstacle in protector.protectors:
            if i_bullet.distance(obstacle) < 30:
                protector.remove(obstacle)

        if ship.distance(i_bullet) < 15:
            game_over()
            ship.goto(1000, 1000)
            game_on = False

screen.exitonclick()
