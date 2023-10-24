import turtle


def draw_hexagon(size):
    my_turtle = turtle.Turtle()

    for _ in range(6):
        my_turtle.forward(size)
        my_turtle.right(60)


def get_num_hexagons():
    num = int(input())
    if num >= 4 and num <= 20:
        return num
    else:
        print('Кол-во должно быть от 4 до 20')
        get_num_hexagons()
