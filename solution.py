"""
Case_3
Group:
Uchanov Igor        70%
Fishchukova Sofia   45%
Tsvykh Viktoria     50%
"""
import turtle

def get_color_choice():
    dict_color = {'красный': '#ec2e51', 'зеленый': '#59ea41', 'синий': '#211cf2',
                  'голубой': '#14dcf3', 'жёлтый': '#fffc00', 'розовый': '#f01de4'}

    while True:
        color_1, color_2 = map(str, input('Введите два цвета для заливки (Например: КрАсНыЙ жёлтый): ').lower().split())

        if color_1 in dict_color and color_2 in dict_color:
            color_1 = dict_color[color_1]
            color_2 = dict_color[color_2]
            break
        else:
            print('Неверно введен цвет Повторите еще раз!')

    return color_1, color_2


def draw_hexagon(tr, size, x, y, color_1):
    '''function, that draw a single hexagon by size'''

    my_turtle = tr
    my_turtle.goto(x, y)
    my_turtle.pendown()
    my_turtle.fillcolor(color_1)
    my_turtle.begin_fill()
    my_turtle.left(150)
    for _ in range(6):
        my_turtle.forward(size)
        my_turtle.right(60)
    my_turtle.penup()
    my_turtle.end_fill()


def get_num_hexagons():
    '''function, that ask and checks num of hexagons from user, then return that num'''
    num = int(input('Введите число шестиугольников в одной строке: '))
    if num >= 4 and num <= 20:
        return num
    else:
        print('Кол-во должно быть от 4 до 20')
        get_num_hexagons()


if __name__ == '__main__':
    width, height = 500, 500
    turtle.screensize(canvwidth=width, canvheight=height)

    num = get_num_hexagons()
    print('Доступные цвета для заливки:\n'
          '1. Красный\n'
          '2. Зелёный\n'
          '3. Синий\n'
          '4. Голубой\n'
          '5. Жёлтый\n'
          '6. Розовый\n')

    color_1, color_2 = get_color_choice()

    tr = turtle.Turtle()
    tr.speed(100)
    tr.penup()
    tr.pendown()
    
    x, y = 0, 0
    size = (width // num) // 2
    for i in range(num):
        for j in range(num):
            if j % 2 == 0:
                color = color_1
            else:
                color = color_2
            draw_hexagon(tr, size, x, y, color)
            tr.right(150)
            x += size * 3 ** (1 / 2)
        y -= 2 * size - size / 2
        if i % 2 == 0:
            x = size * 3 ** (1 / 2) / 2
        else:
            x = 0

    turtle.mainloop()
