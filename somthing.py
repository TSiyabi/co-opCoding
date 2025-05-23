import time
import turtle
x = input("this code does somthing wanna see it? yes/no: ")
if x == "yes":
    print("ok here it is")
    time.sleep(5)
    print("so why are you still here?")
    time.sleep(5)
    print("I mean, I already done somthing, so why are you still here?")
    time.sleep(360)
    print("fine, I will show you the somthing")
    time.sleep(5)

    # Set up the screen
    screen = turtle.Screen()
    screen.title("Pong")
    screen.bgcolor("black")
    screen.setup(width=800, height=600)
    screen.tracer(0)

    # Paddle A
    paddle_a = turtle.Turtle()
    paddle_a.speed(0)
    paddle_a.shape("square")
    paddle_a.color("white")
    paddle_a.shapesize(stretch_wid=5, stretch_len=1)
    paddle_a.penup()
    paddle_a.goto(-350, 0)

    # Paddle B
    paddle_b = turtle.Turtle()
    paddle_b.speed(0)
    paddle_b.shape("square")
    paddle_b.color("white")
    paddle_b.shapesize(stretch_wid=5, stretch_len=1)
    paddle_b.penup()
    paddle_b.goto(350, 0)

    # Ball
    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape("square")
    ball.color("white")
    ball.penup()
    ball.goto(0, 0)
    ball.dx = 0.2
    ball.dy = 0.2

    # Score
    score_a = 0
    score_b = 0
    score = turtle.Turtle()
    score.speed(0)
    score.color("white")
    score.penup()
    score.hideturtle()
    score.goto(0, 260)
    score.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

    # Functions
    def paddle_a_up():
        y = paddle_a.ycor()
        if y < 250:
            y += 20
        paddle_a.sety(y)

    def paddle_a_down():
        y = paddle_a.ycor()
        if y > -250:
            y -= 20
        paddle_a.sety(y)

    def paddle_b_up():
        y = paddle_b.ycor()
        if y < 250:
            y += 20
        paddle_b.sety(y)

    def paddle_b_down():
        y = paddle_b.ycor()
        if y > -250:
            y -= 20
        paddle_b.sety(y)

    # Keyboard bindings
    screen.listen()
    screen.onkeypress(paddle_a_up, "w")
    screen.onkeypress(paddle_a_down, "s")
    screen.onkeypress(paddle_b_up, "Up")
    screen.onkeypress(paddle_b_down, "Down")

    # Main game loop
    while True:
        screen.update()

        # Move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Border checking
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1

        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1

        # Scoring
        if ball.xcor() > 390:
            ball.goto(0, 0)
            ball.dx *= -1
            score_a += 1
            score.clear()
            score.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))

        if ball.xcor() < -390:
            ball.goto(0, 0)
            ball.dx *= -1
            score_b += 1
            score.clear()
            score.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))

        # Paddle collisions
        if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
            ball.setx(340)
            ball.dx *= -1

        if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
            ball.setx(-340)
            ball.dx *= -1
else:
    print("ok bye")
    exit()
