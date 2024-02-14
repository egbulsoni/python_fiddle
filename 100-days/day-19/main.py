from turtle import Turtle, Screen

screen = Screen()
turtle = Turtle()

def move_forward():
    turtle.forward(10)


def move_backwards():
    turtle.backward(10)


def turn_left():
    turtle.left(10)


def turn_right():
    turtle.right(10)

screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.exitonclick()