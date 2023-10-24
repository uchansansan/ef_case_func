import turtle


def draw_hexagon(tr, size, x, y, color = 'red'):
    '''function, that draw a single hexagon by size'''

    my_turtle = tr
    my_turtle.goto(x, y)
    my_turtle.pendown()
    my_turtle.fillcolor(color)
    my_turtle.begin_fill()
    my_turtle.left(150)
    for _ in range(6):
        my_turtle.forward(size)
        my_turtle.right(60)
    my_turtle.penup()
    my_turtle.end_fill()
    # my_turtle.forward(2*size)
    # my_turtle.pendown()
    # my_turtle.left(90)
    # my_turtle.penup()
    # my_turtle.right(90)
    # my_turtle.forward(size)
    # my_turtle.right(60)
    # my_turtle.forward(size)
    # my_turtle.left(60)

def get_num_hexagons():
    '''function, that ask and checks num of hexagons from user, then return that num'''
    num = int(input())
    if num >= 4 and num <= 20:
        return num
    else:
        print('Кол-во должно быть от 4 до 20')
        get_num_hexagons()


if __name__ == '__main__':
    width, height = 200, 200
    turtle.screensize(canvwidth=width, canvheight=height)

    # num = get_num_hexagons()
    num = 5
    tr = turtle.Turtle()
    tr.speed(100)
    tr.penup()
    # tr.goto(-width, height)
    tr.pendown()
    # x, y = -width, height
    x, y = 0, 0
    size = (width // num) // 2
    for i in range(num):
        for j in range(num):
            if j % 2 == 0:
                color = 'green'
            else:
                color = 'red'
            draw_hexagon(tr, size, x, y, color=color)
            tr.right(150)
            x+= size*3**(1/2)
        y -= 2*size - size/2
        if i % 2 == 0:
            x = size*3**(1/2)/2
        else:
            x = 0



    turtle.mainloop()
