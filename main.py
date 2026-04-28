import turtle
import time
import winsound

wn = turtle.Screen()
wn.title("Pong Quest | Group 2_South 9")
wn.bgcolor("#79a68e")
wn.setup(width = 800, height = 600)
wn.tracer(0)

#Score
score_a = 0
score_b = 0
win_score = 2
game_over = False

#Paddle A, left side player
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0) #


#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)


#Ball
ball = turtle.Turtle()
ball.speed(3)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0) # Starting position of the ball
ball.dx = 0.3
ball.dy = -0.3

#Scoring system
pen = turtle.Turtle()
pen.speed(0)
pen.color("#145448")
pen.penup()
pen.hideturtle() # Hides the turtle icon
pen.goto(0, 220) # Position of the score displayed
pen.write("P1: 0  P2: 0", align="center", font=("Courier New", 38, "bold") )

#Game Over
go_pen = turtle.Turtle()
go_pen.speed(0)
go_pen.color("#145448")
go_pen.penup()
go_pen.hideturtle()

# Background pen for Game Over Popup
background_pen = turtle.Turtle()
background_pen.speed(0)
background_pen.color("#ffffff")
background_pen.penup()
background_pen.hideturtle()

# Border pen for Game Over Screen
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("#FFFFFF")
border_pen.penup()
border_pen.hideturtle()


#Functions
    #Left Paddle
def paddle_a_up():
    y = paddle_a.ycor() #.ycor means Y coordinate from the turtle module
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor() 
    y -= 20
    paddle_a.sety(y)


    #Right Paddle
def paddle_b_up():
    y = paddle_b.ycor() # X coordinate from the turtle module
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor() 
    y -= 20
    paddle_b.sety(y)


def show_game_over(winner):
    global game_over # Using global variable to control game state
    game_over = True
    # Draw filled background
    background_pen.clear()
    background_pen.begin_fill()
    background_pen.pendown()
    background_pen.goto(-200, 130) # Top-left corner
    background_pen.goto(200, 130) # Top-right corner
    background_pen.goto(200, -90) # Bottom-right corner
    background_pen.goto(-200, -90) # Bottom-left corner
    background_pen.goto(-200, 130) # Back to Top-left corner
    background_pen.end_fill()
    background_pen.penup() 
    # Draw border
    border_pen.clear()
    border_pen.pendown()
    border_pen.pensize(4) # Border thickness 
    border_pen.goto(-200, 130) # Top-left corner
    border_pen.goto(200, 130) # Top-right corner
    border_pen.goto(200, -90) # Bottom-right corner
    border_pen.goto(-200, -90) # Bottom-left corner
    border_pen.goto(-200, 130) # Back to Top-left corner
    border_pen.penup()
    # Draw text
    go_pen.clear()
    go_pen.goto(0, 40)
    go_pen.color("#9A1D1D")
    go_pen.write(f" Game Over!{winner} Wins", align="center", font=("Courier New", 26, "bold")) # Diplaying winner
    go_pen.goto(0, 2)
    go_pen.color("#3C998A")
    go_pen.write("Press 'R' to Restart", align="center", font=("Coutier New", 15, "normal")) # Restart instruction
    go_pen.goto(0, -30)
    go_pen.write("and press 'Q' to Quit", align="center", font=("Coutier New", 15, "normal")) # Quit instruction
    winsound.PlaySound('powerup.wav', winsound.SND_FILENAME | winsound.SND_ASYNC) # Playing sound effect when the game is over
    # Binding restart and quit keys on game over
    wn.onkeypress(restart_game, "r")
    wn.onkeypress(restart_game, "R")
    wn.onkeypress(quit_game, "q")
    wn.onkeypress(quit_game, "Q")

def restart_game():
    global score_a, score_b, game_over
    score_a = 0 
    score_b = 0
    pen.clear()
    pen.color("#145448")
    pen.goto(0, 220)
    pen.write("P1: 0 P2: 0", align="center", font=("Courier New", 38, "bold")) # Resetting score display
    go_pen.clear()
    background_pen.clear()
    border_pen.clear()

    # Resetting positions
    ball.goto(0, 0)
    ball.dx = 0.3 # Restting ball movement xcor
    ball.dy = -0.3 # Restting ball movement ycor
    paddle_a.goto(-350, 0) # Resetting paddle a position
    paddle_b.goto(350, 0) # Resetting paddle a position
    game_over = False

def quit_game(): # Quiting game function
    wn.bye() # Closing the game window


#Keyboard bindings
#Player consoles
wn.listen()
wn.onkeypress(paddle_a_up, "w") 
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


#Main Game Loop
while True:
    wn.update()
    time.sleep(0.001) #Delayment of the ball
    if game_over:
        # Pausing the main loop and keep processing window events until restart or quit
        while game_over:
            wn.update()
            time.sleep(0.1)
        continue

    #Movement of the ball
    ball.setx(ball.xcor() + ball.dx) # movement in xcor
    ball.sety(ball.ycor() + ball.dy) # movement in ycor
    

#Border checking
    #Up & Bottom screen
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1


    #Left & right screen
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        winsound.PlaySound('pluck.wav', winsound.SND_FILENAME | winsound.SND_ASYNC) # Playing sound effect when the player misses the ball
        pen.write("P1: {} P2: {}".format(score_a, score_b), align="center", font=("Courier New", 38, "bold") ) # Updating score display
        if score_a >= win_score:
            show_game_over("P1") # Displaying Game Over for P1


    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        winsound.PlaySound('pluck.wav', winsound.SND_FILENAME | winsound.SND_ASYNC) # Using .SND_ASYNC & .SND_FILENAME to play sound without pausing the game
        pen.write("P1: {} P2: {}".format(score_a, score_b), align="center", font=("Courier New", 38, "bold") )
        if score_b >= win_score:
            show_game_over("P2") # Displaying Game Over for P2



#Paddle and Ball Collisions
    #Right Paddle
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40): # Checks if the ball is within the paddle range
        ball.setx(340) # Prevents the ball from going inside the paddle
        ball.dx *= -1 # Reversing the balls direction
        winsound.PlaySound('pixie.wav', winsound.SND_FILENAME | winsound.SND_ASYNC) # Playing sound effect when the ball hits the paddle
        
    #Left Paddle
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound('pixie.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
