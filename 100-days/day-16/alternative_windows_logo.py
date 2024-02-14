from turtle import *

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.pencolor("red")
# timmy.penup()
timmy.forward(100)
timmy.left(90)
timmy.forward(100)
timmy.left(90)
timmy.forward(100)
timmy.left(90)
timmy.forward(100)

# left upper window
mini_window = 75
timmy.penup()
timmy.right(90)
timmy.forward(50)
timmy.pendown()
timmy.forward(mini_window)
timmy.right(90)
timmy.forward(mini_window)
timmy.right(90)
timmy.forward(mini_window)
timmy.right(90)
timmy.forward(mini_window)

# left lower window
timmy.penup()
timmy.forward(50)

timmy.pendown()
timmy.forward(100)
timmy.right(90)
timmy.forward(100)
timmy.right(90)
timmy.forward(100)
timmy.right(90)
timmy.forward(100)

# right lower window
timmy.penup()
timmy.forward(50)

timmy.pendown()
timmy.forward(mini_window)
timmy.right(90)
timmy.forward(mini_window)
timmy.right(90)
timmy.forward(mini_window)
timmy.right(90)
timmy.forward(mini_window)

my_screen = Screen()
my_screen.exitonclick()

