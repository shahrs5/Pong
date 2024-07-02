import random
from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_move = 4
        self.y_move = 4
        self.speed = 0.02


    def start(self):
        self.x_move = random.randrange(-5,6,10)
        self.y_move = random.randrange(-5, 6, 10)
        print(f"x : {self.x_move} y: {self.y_move}")

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move

        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move = self.y_move * -1

    def bounce_x(self):
        self.x_move = self.x_move * -1
        self.speed *= 0.8
    def restart(self):
        self.x_move *= -1
        self.goto(0,0)
        self.speed = 0.02