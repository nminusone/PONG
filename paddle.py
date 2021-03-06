from turtle import Turtle

WIDTH = 20
HEIGHT = 100


class Paddle(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.shape('square')
        self.x_init = x_cor
        self.y_init = y_cor
        self.color('white')
        self.penup()
        self.goto(self.x_init, self.y_init)

        self.shapesize(5, 1, 1)
        self.pad_pos = 0

    def right_up(self):
        self.pad_pos = self.ycor() + 20
        self.goto(350, self.pad_pos)

    def right_down(self):
        self.pad_pos = self.ycor() - 20
        self.goto(350, self.pad_pos)

    def left_up(self):
        self.pad_pos = self.ycor() + 20
        self.goto(-350, self.pad_pos)

    def left_down(self):
        self.pad_pos = self.ycor() - 20
        self.goto(-350, self.pad_pos)


