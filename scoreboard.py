from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.add_points()

    def add_points(self):
        self.goto(-100, 200)
        self.clear()
        self.write(self.l_score, align='center', font=('Courier', 80, 'normal'))
        self.goto(100, 200)
        self.write(self.r_score, align='center', font=('Courier', 80, 'normal'))

    def l_point(self):
        self.l_score += 1
        self.add_points()

    def r_point(self):
        self.r_score += 1
        self.add_points()


