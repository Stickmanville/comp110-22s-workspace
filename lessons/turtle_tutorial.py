from turtle import Turtle, colormode, done
leo: Turtle = Turtle()
colormode(255)

leo.penup()
leo.goto(-150, -120)
leo.pendown()
leo.color("blue")

leo.speed(50)
leo.hideturtle()
leo.begin_fill()

i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i = i + 1

leo.end_fill()

bob: Turtle = Turtle()

bob.speed(100)

side_length: int = 300

i = 0
while (i < 100):
    bob.forward(side_length)
    bob.left(122)
    i = i + 1
    side_length = side_length * 0.97
    
done()