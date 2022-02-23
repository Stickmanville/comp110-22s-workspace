"""EX04 - Turtle - Paints a simple painting. 

Function 'tree' uses other functions on lines 50-52.
Utilizes a circle function to draw the sun.
"""

__author__ = "730332997"

from turtle import Turtle, colormode, done
paint_brush: Turtle = Turtle()
colormode(255)


def triangle(color: str, size: int, x: int, y: int) -> None:
    """Paints a triangle of a given color and size at a given position."""
    paint_brush.penup()
    paint_brush.goto(x, y)
    paint_brush.pendown()
    paint_brush.color(color)
    paint_brush.speed(100)
    paint_brush.hideturtle()
    paint_brush.begin_fill()
    i: int = 0
    while (i < 3):
        paint_brush.forward(size)
        paint_brush.left(120)
        i = i + 1

    paint_brush.end_fill()
    return


def square(color: str, size: int, x: float, y: int) -> None:
    """Paints a square of a given color and size at a given position."""
    paint_brush.penup()
    paint_brush.goto(x, y)
    paint_brush.pendown()
    paint_brush.color(color)
    paint_brush.speed(100)
    paint_brush.hideturtle()
    paint_brush.begin_fill()
    i: int = 0
    while (i < 4):
        paint_brush.forward(size)
        paint_brush.left(90)
        i = i + 1

    paint_brush.end_fill()
    return


def tree(size: int, x: int, y: int) -> None:
    """Paints a tree of a given size and position using triangles and rectangles."""
    triangle("green", (4 * size), x, y)
    square("brown", size, x + 4 * size / (25 / 9), y - size)
    square("brown", size, x + 4 * size / (25 / 9), y - 2 * size)
    return


def circle(color: str, size: int, x: int, y: int) -> None:
    """Paints a circle of a given color and size at a given position."""
    paint_brush.penup()
    paint_brush.goto(x, y)
    paint_brush.pendown()
    paint_brush.color(color)
    paint_brush.speed(100)
    paint_brush.hideturtle()
    paint_brush.begin_fill()
    paint_brush.circle(size)
    paint_brush.end_fill()
    return


def main() -> None:
    """The entrypoint of my scene."""
    # TODO: Declare your Turtle variable(s) here.
    x: int = -325
    # TODO: Call the procedures you define and pass your Turtle(s) as an argument.
    i: int = 0
    square("blue", 500, -500, 0)
    square("blue", 500, 0, 0)
    square("gray", 500, -500, -500)
    square("gray", 500, 0, -500)
    circle("yellow", 40, 0, 100)
    while i < 8:
        tree(20, x, 10)
        x += 80
        i += 1
    done()
    return


if __name__ == "__main__":
    main()