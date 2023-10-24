import turtle


def draw_hexagon(tr, size):
    '''function, that draw a single hexagon by size'''

    my_turtle = tr
    for _ in range(6):
        my_turtle.forward(size)
        my_turtle.right(60)
    my_turtle.left(90)


def get_num_hexagons():
    '''function, that ask and checks num of hexagons from user, then return that num'''
    num = int(input())
    if num >= 4 and num <= 20:
        return num
    else:
        print('Кол-во должно быть от 4 до 20')
        get_num_hexagons()


if __name__ == '__main__':
    width, height = 300, 300
    turtle.screensize(canvwidth=width, canvheight=height)

    num = get_num_hexagons()

    tr = turtle.Turtle()
    tr.penup()
    tr.goto(-width, height)
    tr.pendown()
    draw_hexagon(tr, (width // num) // 2)


    turtle.mainloop()
