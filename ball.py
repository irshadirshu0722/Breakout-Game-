

from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.speed("fastest")
        self.shapesize(1)
        self.penup()
        self.goto(0,-200)
        self.movex = 20
        self.movey = 20
    def move(self):
        x,y = self.pos()
        self.goto(x+self.movex,y+ self.movey)
    def left_right_hit(self):
        self.movex*=-1
    def upper_paddle_hit(self):
        self.movey*=-1
    def restart(self):
        self.goto(0, -200)
        self.movex = 20
        self.movey = 20


