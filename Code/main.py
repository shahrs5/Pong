from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

SCREENWIDTH = 800

screen = Screen()
screen.setup(width = SCREENWIDTH, height = 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()

scoreboard = Scoreboard()
player1 = Paddle((SCREENWIDTH / 2) - 50)
player2 = Paddle((-SCREENWIDTH / 2) + 50)
ball = Ball()
ball.start()

screen.onkeypress(player1.up, "Up")
screen.onkeyrelease(player1.up, "Up")
screen.onkeypress(player1.down, "Down")
screen.onkeyrelease(player1.down, "Down")
screen.onkeypress(player2.up, "w")
screen.onkeyrelease(player2.up, "w")
screen.onkeypress(player2.down, "s")
screen.onkeyrelease(player2.down, "s")

game_over = False

while not game_over:
    screen.update()
    time.sleep(ball.speed)
    scoreboard.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.xcor() > 340 and ball.distance(player1) < 50 or ball.xcor() < -340 and ball.distance(player2) < 50:
        ball.bounce_x()

    if ball.xcor() > 400:
        scoreboard.scoreOne += 1
        ball.restart()

    elif ball.xcor() < -400:
        scoreboard.scoreTwo += 1
        ball.restart()

    if scoreboard.check_game_over():
        game_over = True
        if scoreboard.scoreOne == 10:
            scoreboard.player_one_win()
        else:
            scoreboard.player_two_win()




screen.exitonclick()