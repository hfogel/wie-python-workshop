# ------------------------------------------------------------------------------ #
# ----------------- WIE Winnipeg's High School Python Workshop ----------------- #
# ------------------------- Main Program for Pong Game ------------------------- #
# -- adapted from: www.geeksforgeeks.org/create-pong-game-using-python-turtle -- #
# ------------------------------------------------------------------------------ #

# Import required library
import turtle

# Create a screen for the game
screen = turtle.Screen() # creates screen
screen.title("Pong game") # displays title on screen
screen.bgcolor("black") # sets background colour
screen.setup(width=575, height=325) # sets screen size

# Create the left paddle
left_pad = turtle.Turtle()
left_pad.speed(0)   # not moving when the game starts
left_pad.shape("square")
left_pad.color("white") # sets paddle color
left_pad.shapesize(stretch_wid=3, stretch_len=0.5)    # stretch out a square to make a rectangular shape
left_pad.penup()    # don't draw a path when moving
left_pad.goto(-250, 0)  # start on left side of screen

# Create the right paddle
right_pad = turtle.Turtle()
right_pad.speed(0)
right_pad.shape("square")
right_pad.color("white")
right_pad.shapesize(stretch_wid=3, stretch_len=0.5)
right_pad.penup()
right_pad.goto(250, 0)  # start on right side of screen

# Create the ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("blue")
ball.penup()
ball.goto(0, 0)

# initial speed and direction for the ball to move:
################### INPUT HERE ###########################
ball.speed(4) # sets your ball speed
##########################################################
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
scoreboard.goto(0, 120)
scoreboard.write("Left_player : 0 Right_player: 0",
                 align="center", font=("Courier", 14, "normal"))


# Functions to move the paddles up and down:

################### INPUT HERE ###########################
paddle_speed = 40; # sets how far you can move your paddle with one key press
##########################################################

def paddleA_up():
    y = left_pad.ycor() 
    y += paddle_speed 
    left_pad.sety(y)


def paddleA_down():
    y = left_pad.ycor()
    y -= paddle_speed
    left_pad.sety(y)


def paddleB_up():
    y = right_pad.ycor()
    y += paddle_speed
    right_pad.sety(y)


def paddleB_down():
    y = right_pad.ycor()
    y -= paddle_speed
    right_pad.sety(y)


# Keyboard bindings - our way to interact with the game
screen.listen()
screen.onkeypress(paddleA_up, "e")
screen.onkeypress(paddleA_down, "x")
screen.onkeypress(paddleB_up, "Up")
screen.onkeypress(paddleB_down, "Down")

while True:
    screen.update()

    # Moves the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Make sure the ball doesn't go off the top or bottom of the screen:
    if ball.ycor() > 150:
        ball.sety(150)
        ball.dy *= -1

    if ball.ycor() < -150:
        ball.sety(-150)
        ball.dy *= -1

    # Check if anyone has scored:
    if ball.xcor() > 300:
        ball.goto(0, 0)
        ball.dy *= -1
        left_player_score += 1
        scoreboard.clear()
        scoreboard.write("Left_player : {} Right_player: {}".format(
            left_player_score, right_player_score), align="center",
            font=("Courier", 14, "normal"))

    if ball.xcor() < -300:
        ball.goto(0, 0)
        ball.dy *= -1
        right_player_score += 1
        scoreboard.clear()
        scoreboard.write("Left_player : {} Right_player: {}".format(
            left_player_score, right_player_score), align="center",
            font=("Courier", 14, "normal"))

    # Check for a collision between the right paddle and the ball:
    
    ################### INPUT HERE ###########################
    paddle_hit = 80 # sets the "hit" zone of your paddle.
    ##########################################################
    
    if (ball.xcor() > 245 and ball.xcor() < 255) \
            and (ball.ycor() < right_pad.ycor() + paddle_hit and ball.ycor() > right_pad.ycor() - paddle_hit):
        ball.setx(245)
        ball.dx *= -1
              
    # Check for a collision between the left paddle and the ball:
    if (ball.xcor() < -245 and ball.xcor() > -255) \
            and (ball.ycor() < left_pad.ycor() + paddle_hit and ball.ycor() > left_pad.ycor() - paddle_hit):
        ball.setx(-245)
        ball.dx *= -1

