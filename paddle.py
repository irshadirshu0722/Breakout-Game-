

from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.speed("fastest")
        self.shapesize(1,12)
        self.penup()
        self.goto(0,-420)
    def moveLeft(self):
        x,y = self.pos()
        self.goto(x-20, y)
    def moveRight(self):
        x,y = self.pos()
        self.goto(x+20, y)