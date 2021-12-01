from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.color('white')
        self.ht()
        self.penup()
        self.goto(0, 255)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"{self.left_score} : {self.right_score}", move=False, align='center', font=('Arial', 30, 'normal'))

    def change_left(self):
        self.clear()
        self.left_score += 1
        self.update_scoreboard()

    def change_right(self):
        self.clear()
        self.right_score += 1
        self.update_scoreboard()
