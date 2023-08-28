from turtle import title, speed, bgcolor, colormode, fd, rt, pencolor

title("Turtle Spiral Helix")
speed(15)
bgcolor('#000')
r, g, b = 255, 0, 0

for i in range(255*2):
    colormode(255)

    if i < 255//3:
        g += 3
    elif i < (255*2)//3:
        r -= 3
    elif i < 255:
        b += 3
    elif i < (255*4)//3:
        g -= 3
    elif i < (255*5)//3:
        r += 3
    else:
        b -= 3

    fd(50+i)
    rt(91)
    pencolor(r, g, b)
