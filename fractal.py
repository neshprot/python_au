import turtle as tl


def draw_triangle(scale):
    tl.forward(scale / 3)
    tl.left(120)
    tl.forward(scale / 3)
    tl.left(120)
    tl.forward(scale / 3)
    tl.left(120)


def draw_fractal(scale):
    if scale >= SCALE/50:
        draw_triangle(scale)
        tl.forward(scale/6)
        tl.left(60)
        draw_fractal(scale / 2)


SCALE = 1000
tl.pensize(2)
for n in range(0, 4):
    tl.seth(0)
    tl.penup()
    tl.goto(-SCALE / 4, -SCALE / 4)
    tl.pendown()
    if n == 1:
        tl.forward(SCALE / 6)
    if n == 2:
        tl.left(60)
        tl.forward(SCALE / 6)
        tl.right(60)
    if n == 3:
        tl.left(60)
        tl.forward(SCALE / 6)
        tl.right(120)
    draw_fractal(SCALE / 2)


tl.done()
