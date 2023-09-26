from turtle import Turtle

RECT_ANGLE = 90

# turtle at center (0, 0)
t = Turtle()

MARGIN = 5
HORIZONTAL_BORDER = (t.screen.window_width() / 2) - MARGIN
VERTICAL_BORDER = (t.screen.window_height() / 2) - MARGIN


def square(side_length, color):
    t.fillcolor(color)
    t.begin_fill()
    for __ in range(4):
        t.forward(side_length)
        t.right(RECT_ANGLE)
    t.end_fill()


def make_row(square_side_length, begin_with='black'):
    color_list = ['black', 'white']

    if begin_with == 'white':
        color_list.reverse()

    for __ in range(4):
        square(square_side_length, color_list[0])
        t.forward(square_side_length)
        square(square_side_length, color_list[1])
        t.forward(square_side_length)


def move_to_next_row(side_length):
    t.up()
    t.backward(side_length * 8)
    t.right(RECT_ANGLE)
    t.forward(side_length)
    t.left(RECT_ANGLE)
    t.down()


def make_board(square_side):
    for __ in range(4):
        make_row(square_side, 'white')
        move_to_next_row(square_side)
        make_row(square_side, 'black')
        move_to_next_row(square_side)


t.reset()
t.speed(0)
t.up()
t.goto(-HORIZONTAL_BORDER, VERTICAL_BORDER)
t.down()

make_board(90)

input()
