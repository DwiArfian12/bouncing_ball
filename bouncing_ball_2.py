import turtle

wn = turtle.Screen()
wn.title("Bouncing Ball Simulation 2 | by Dwi Arfian")
wn.bgcolor("black")
wn.tracer(0)

ball = turtle.Turtle()
ball.shape("circle")
ball.color("green")
ball.penup()
ball.speed(0)
ball.goto(0, 200)
ball.dy = 0
ball.dx = 2

gravity = 0.1

while True:
    wn.update()
    ball.dy -= gravity

    ball.sety(ball.ycor() + ball.dy)
    ball.setx(ball.xcor() + ball.dx)

    if ball.xcor() > 300 or ball.xcor() < -300:
        ball.dx *= -1

    if ball.ycor() < -300:
        ball.dy *= -1