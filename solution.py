import turtle


def draw_hexagon(size):
    '''function, that draw a single hexagon by size'''
    my_turtle = turtle.Turtle()

    for _ in range(6):
        my_turtle.forward(size)
        my_turtle.right(60)


def get_num_hexagons():
    '''function, that ask and checks num of hexagons from user, then return that num'''
    num = int(input())
    if num >= 4 and num <= 20:
        return num
    else:
        print('Кол-во должно быть от 4 до 20')
        get_num_hexagons()


if __name__ == '__main__':
    turtle.screensize(canvwidth=500, canvheight=500)
    draw_hexagon(10)
    turtle.mainloop()