from turtle import *
from paddle import Paddle
from ball import Ball
from  time import sleep
from Block import Block
import winsound
screen = Screen()
screen.title("breakout Game")
screen.setup(1700,900)
screen.bgcolor("black")

blocks = Block()
paddle = Paddle()
ball = Ball()

right_hold = False
left_hold = False
def rightmove():
    global right_hold

    if paddle.xcor()<700:
        paddle.moveRight()

    if right_hold:
        screen.ontimer(rightmove, 100)
def rightmovestart():
    global right_hold
    right_hold=True
    rightmove()

def rightmovestop():
    global right_hold
    right_hold=False

def leftmove():
    global left_hold
    if paddle.xcor()>-700:
        paddle.moveLeft()

    if left_hold:
        screen.ontimer(leftmove, 100)
def leftmovestart():
    global left_hold
    left_hold=True
    leftmove()

def leftmovestop():
    global left_hold
    left_hold=False

screen.listen()


screen.onkeypress(rightmovestart,"Right")
screen.onkeyrelease(rightmovestop,"Right")
screen.onkeypress(leftmovestart,"Left")
screen.onkeyrelease(leftmovestop,"Left")
# print(paddle.xcor())
blockremoved = 0
totalblock = len(blocks.blocks)
# print(paddle.color()[0]=="white")
is_game=True
while is_game:
    sleep(0.04)
    ball.move()
    screen.tracer(0)

    if ball.ycor()<-450:
        ball.restart()
    if ball.xcor()>800 or ball.xcor()<-800:
        ball.left_right_hit()
    if ball.ycor() > 400:

        ball.upper_paddle_hit()
    if paddle.distance(ball)<170 and ball.ycor()<-380 and ball.ycor()>-420:

        if paddle.distance((ball))<40:
            ball.movex =20 if ball.movex>0 else -20

        elif paddle.distance((ball))<80:
            ball.movex+=3
        elif paddle.distance((ball)) < 100:
            ball.movex += 5
        elif paddle.distance((ball)) < 150:
            ball.movex += 8


        ball.upper_paddle_hit()

    for block in blocks.blocks:
        if ball.distance(block)<70 and block.color()[0]!="black":
            print(ball.distance(block))
            block.color("black")
            blockremoved+=1
            winsound.Beep(500,100)
            ball.upper_paddle_hit()
            if blockremoved == totalblock:
                blocks.Gameover()
                is_game = False
                break



    screen.update()



screen.exitonclick()
