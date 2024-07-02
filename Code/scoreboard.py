import turtle
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.scoreOne = 0
        self.scoreTwo = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,250)

    def increase_score_one(self):
        self.scoreOne += 1

    def increase_score_two(self):
        self.scoreTwo += 1

    def player_one_win(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"Gameover! Player One Wins", False, align="center", font=("Comic Sans MS", 12, "bold"))

    def player_two_win(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"Gameover! Player Two Wins", False, align="center", font=("Comic Sans MS", 12, "bold"))

    def check_game_over(self):
        if self.scoreOne == 10 or self.scoreTwo == 10:
            return True

    def update(self):
        self.clear()
        self.write(f"{self.scoreOne}         ", False, align="center", font=("Comic Sans MS", 30, "bold"))
        self.write(f"         {self.scoreTwo}", False, align="center", font=("Comic Sans MS", 30, "bold"))
