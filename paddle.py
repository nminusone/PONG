from turtle import Turtle

WIDTH = 20
HEIGHT = 100
X_POS = 350
Y_POS = 0


class Paddle:
    def __init__(self):
        self.pad = Turtle(shape='square')
        self.pad.color('white')
        self.pad.penup()
        self.pad.goto(X_POS, Y_POS)
        self.pad.shapesize(5, 1, 1)

    def up(self):
        self.pad.goto(X_POS, Y_POS + 5)
