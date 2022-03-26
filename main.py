import turtle as tt
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = tt.Screen()

screen.setup(800, 600)
screen.title("Ping-Pong")
screen.bgcolor("black")
screen.tracer(0)


right_paddle = Paddle((350,0))
left_paddle = Paddle((-350,0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkeypress(right_paddle.go_up, "Up")
screen.onkeypress(right_paddle.go_down, "Down")
screen.onkeypress(left_paddle.go_up, "w")
screen.onkeypress(left_paddle.go_down, "s")


game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Bounce the ball if collison detected with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    
    # Detect contact with rigt paddle
    if ball.distance(right_paddle) <50 and ball.xcor() > 320:
        ball.bounce_x()
    elif ball.xcor() > 380:
        ball.reset_position()
        score.increase_left()


    # Detect contact with left paddle
    if ball.distance(left_paddle) <50 and ball.xcor() < -320:
        ball.bounce_x()
    elif ball.xcor() < -380:
        ball.reset_position()
        score.increase_right()

    # End the game 
    if score.l_score == 10 or score.r_score == 10:
        game_on = False
        score.end_game()
        

screen.exitonclick()