from turtle import *
import time
bgcolor('#000')
title("Turtle Spiral Helix")
time.sleep(7)
speed(0)
ht()
size = 0
for i in range(2000):
    if i % 2 == 0:
        color('red')
    else:
        color('white')
    fd(size)
    rt(91)
    size += 1
