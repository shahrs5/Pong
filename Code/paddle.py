from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, SCREENWIDTH):
        super().__init__()
        self.shape("square")
        self.shapesize(5, 1)
        self.penup()
        self.goto(SCREENWIDTH, 0)
        self.color("white")

    def up(self):
        x_pos = self.xcor()
        y_pos = self.ycor()
        self.setpos(x_pos, y_pos + 20)

    def down(self):
        x_pos = self.xcor()
        y_pos = self.ycor()
        self.setpos(x_pos, y_pos - 20)