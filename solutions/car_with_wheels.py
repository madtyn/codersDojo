from turtle import Turtle

RECT_ANGLE = 90
FRONT_CAR_WIDTH = 20
BACK_CAR_WIDTH = 20
BODY_HEIGHT = 20
WINDOW_HEIGHT = 20
CEILING = 60
BASE = 100
WHEEL_RADIUS = 15
WHEEL_SEPARATION_DISTANCE = BASE - WHEEL_RADIUS * 4

t = Turtle()


def main_body():
    t.color(1,0,0)
    t.begin_fill()
    t.forward(BASE)
    t.left(RECT_ANGLE)
    t.forward(BODY_HEIGHT)
    t.left(RECT_ANGLE)
    t.forward(FRONT_CAR_WIDTH)
    t.right(RECT_ANGLE)
    t.forward(WINDOW_HEIGHT)
    t.left(RECT_ANGLE)
    t.forward(CEILING)
    t.left(RECT_ANGLE)
    t.forward(WINDOW_HEIGHT)
    t.right(RECT_ANGLE)
    t.forward(BACK_CAR_WIDTH)
    t.left(RECT_ANGLE)
    t.forward(BODY_HEIGHT)
    t.end_fill()


def wheel(radius):
    t.begin_fill()
    t.circle(radius)
    t.end_fill()


def goto_first_wheel():
    t.up()
    t.forward(WHEEL_RADIUS)
    t.down()


def goto_second_wheel():
    t.setheading(0)
    t.up()
    t.forward(WHEEL_SEPARATION_DISTANCE + WHEEL_RADIUS * 2)
    t.right(RECT_ANGLE)


t.reset()
t.speed(1)

main_body()

t.color(0, 0, 0)

goto_first_wheel()
wheel(WHEEL_RADIUS)
goto_second_wheel()
wheel(WHEEL_RADIUS)

t.hideturtle()
input()
