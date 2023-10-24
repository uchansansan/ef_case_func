import turtle


def draw_hexagon(size):
    my_turtle = turtle.Turtle()

    for _ in range(6):
        my_turtle.forward(size)
        my_turtle.right(60)
