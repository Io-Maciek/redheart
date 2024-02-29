import math
from turtle import *


def print_write(text, x, y, pen_color=None):
    penup()
    pre = None
    if pen_color is not None:
        pre = color()
        color(pen_color)
    goto(x, y)
    write(text, font=("Arial", 50, "normal"))
    if pre is not None:
        color(pre[0])
    goto(0, 0)
    pendown()
    update()


def hearta(k):
    return 15 * math.sin(k) ** 3


def heartb(k):
    return 12 * math.cos(k) - 5 * \
        math.cos(2 * k) - 2 * \
        math.cos(3 * k) - \
        math.cos(4 * k)


try:
    with open("config.txt", 'r') as f:
        title(f.read())
except FileNotFoundError:
    pass


delay(0)
ht()
tracer(0, 0)

setup(620, 700)

speed(10000)
bgcolor("pink")
color("red")

print_write("I", 0, 250, "black")

width(4)
YOU_SEEN = False
RANGE = 777

for i in range(RANGE):
    delay(0)
    goto(0, 0)
    goto(hearta(i) * 20, heartb(i) * 20 + 40)
    if i % 5 == 0:
        update()
    if not YOU_SEEN and i > (RANGE // 2):
        YOU_SEEN = True
        print_write("YOU", -69, -350, "black")

update()
done()
