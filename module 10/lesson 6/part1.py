import turtle

turtle.Screen().bgcolor("pink")

sc=turtle.Screen()
sc.setup(600,600)

turtle.title("this is an octagon")

board=turtle.Turtle()
board.speed(1)
n=8

for i in range(n):
    board.forward(50)
    board.left(360/n)