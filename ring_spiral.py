from turtle import title, speed, bgcolor, color, right, circle

title("Turtle Spiral Helix")
speed(15)
bgcolor('#000')

colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']


def drawCircles(size):
    for i in range(10):
        circle(size)
        size = size-4
        color(colors[i % 6])


def drawSpecial(size, repeat):
    for i in range(repeat):
        drawCircles(size)
        right(360/repeat)


drawSpecial(100, 10)
