from turtle import Turtle

WIDTH = 20
HEIGHT = 100


# X_POS = 350
# Y_POS = 0


# x_cor, y_cor

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


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('blue')
        self.goto(0, 0)

    def move_ball(self):
        self.seth(45)
        self.forward(20)
