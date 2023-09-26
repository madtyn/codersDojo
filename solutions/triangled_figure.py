"""
Isto entre comillas triples é un comentario. Os comentarios son ignorados e Python non os interpreta. Serven pra explicar cousas
"""
import turtle

t = turtle.Pen()
"""
Isto de aquí abaixo é unha lista. Lembrade que as listas permiten ter dentro valores.

Podemos obter 
o primer elemento con: colors[0]
o segundo elemento con colors[1]
etc...
"""
colors = [
    'red', 'blue', 'green', 'orange', 'purple', 'black', 'cyan', 'dark blue',
    'pink', 'dark green', 'gray'
]
"""
As listas tamén permiten engadir elementos, por exemplo:

colors.append('yellow')

mete o amarelo no final da lista, en cambio:

del l[1]

borra o segundo elemento
"""


def calc_angle(num_sides):
    """
    Esta función calcula o angulo entre os lados dun polígono regular
    num_sides é o número de lados do polígono
    """
    return 360 / num_sides


def polygon(num_sides, side_length):
    """
    Esta función debuxa un polígono regular

    num_sides é o número de lados
    side_length é a lonxitude do lado
    """
    angle_per_iter = calc_angle(num_sides)
    for i in range(num_sides):
        t.forward(side_length)
        t.left(angle_per_iter)


def figure(num_sides, side_length):
    """
    Isto construe calquer polígono a base de triangulos

    IMPORTANTE: Lembrade que se queredes facer poligonos de maís lados, hai que meter máis colores. Se acabades os colores, vai dar un erro

    num_sides é o número de lados
    side_length é a lonxitude do lado
    """
    angle = calc_angle(num_sides)
    for i in range(num_sides):
        t.color(colors[i], colors[i])
        t.begin_fill()
        polygon(3, side_length)
        t.end_fill()
        t.forward(side_length)
        t.left(angle)


figure(10, 30)

t.hideturtle()

input()
