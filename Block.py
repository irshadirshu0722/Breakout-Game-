from turtle import Turtle

import random
class Block():
    def __init__(self):
        self.blocks =set()
        self.color = ["green", "white", "blue", "purple"]
        self.CreateBlock()


    def CreateBlock(self):
        blockposy =300
        blockposx = -780
        for i in range(52):
            new_block = Turtle()
            new_block.penup()
            new_block.shape("square")
            new_block.speed("fastest")

            new_block.shapesize(2,6)


            new_block.goto(blockposx,blockposy)
            new_block.color(random.choice(self.color))
            blockposx+= 130
            # print(blockposx)
            if blockposx==910:
                blockposx=-780
                blockposy-=80


            self.blocks.add(new_block)
    def Gameover(self):
        board = Turtle()
        board.hideturtle()
        board.goto(0,0)
        board.penup()
        board.color("white")
        board.write(arg=f"Gmae Over",align="center",font=("Arial",24,"normal"))







