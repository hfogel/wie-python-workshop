# ------------------------------------------------------------------------------ #
# ----------------- WIE Winnipeg's High School Python Workshop ----------------- #
# ------------------------- Main Program for Pong Game ------------------------- #
# -- adapted from: www.geeksforgeeks.org/create-pong-game-using-python-turtle -- #
# ------------------------------------------------------------------------------ #

# Import required library
import turtle

# Create a screen for the game
screen = turtle.Screen()
screen.title("Pong game")
screen.bgcolor("black")
screen.setup(width=1000, height=600)

# Create the left paddle
left_pad = turtle.Turtle()
left_pad.speed(0)   # not moving when the game starts
left_pad.shape("square")
left_pad.color("white")
left_pad.shapesize(stretch_wid=6, stretch_len=2)    # stretch out a square to make a rectangular shape
left_pad.penup()    # don't draw a path when moving
left_pad.goto(-400, 0)  # start on left side of screen

# Create the right paddle
right_pad = turtle.Turtle()
right_pad.speed(0)
right_pad.shape("square")
right_pad.color("white")
right_pad.shapesize(stretch_wid=6, stretch_len=2)
right_pad.penup()
right_pad.goto(400, 0)  # start on right side of screen

# Create the ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("blue")
ball.penup()
ball.goto(0, 0)
# initial speed and direction for the ball to move:
ball.speed(40)
ball.dx = 5
ball.dy = -5

# Initialize the score
left_player_score = 0
right_player_score = 0

# Display the score
scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.color("blue")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(0, 260)
scoreboard.write("Left_player : 0 Right_player: 0",
                 align="center", font=("Courier", 24, "normal"))


# Functions to move the paddles up and down:
def paddleA_up():
    y = left_pad.ycor()
    y += 20
    left_pad.sety(y)


def paddleA_down():
    y = left_pad.ycor()
    y -= 20
    left_pad.sety(y)


def paddleB_up():
    y = right_pad.ycor()
    y += 20
    right_pad.sety(y)


def paddleB_down():
    y = right_pad.ycor()
    y -= 20
    right_pad.sety(y)


# Keyboard bindings - our way to interact with the game
screen.listen()
screen.onkeypress(paddleA_up, "e")
screen.onkeypress(paddleA_down, "x")
screen.onkeypress(paddleB_up, "Up")
screen.onkeypress(paddleB_down, "Down")

while True:
    screen.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Make sure the ball doesn't go off the top or bottom of the screen:
    if ball.ycor() > 280:
        ball.sety(280)
        ball.dy *= -1

    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1

    # Check if anyone has scored:
    if ball.xcor() > 500:
        ball.goto(0, 0)
        ball.dy *= -1
        left_player_score += 1
        scoreboard.clear()
        scoreboard.write("Left_player : {} Right_player: {}".format(
            left_player_score, right_player_score), align="center",
            font=("Courier", 24, "normal"))

    if ball.xcor() < -500:
        ball.goto(0, 0)
        ball.dy *= -1
        right_player_score += 1
        scoreboard.clear()
        scoreboard.write("Left_player : {} Right_player: {}".format(
            left_player_score, right_player_score), align="center",
            font=("Courier", 24, "normal"))

    # Check for a collision between the right paddle and the ball:
    if (ball.xcor() > 360 and ball.xcor() < 370) \
            and (ball.ycor() < right_pad.ycor() + 40 and ball.ycor() > right_pad.ycor() - 40):
        ball.setx(360)
        ball.dx *= -1
              
    # Check for a collision between the left paddle and the ball:
    if (ball.xcor() < -360 and ball.xcor() > -370) \
            and (ball.ycor() < left_pad.ycor() + 40 and ball.ycor() > left_pad.ycor() - 40):
        ball.setx(-360)
        ball.dx *= -1

