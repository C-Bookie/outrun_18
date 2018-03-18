
import numpy as np
import pygame, sys
from pygame.locals import *
import time
import math


def foo(n):
    return [int(d) for d in str(n)]

def bar(n):
    r=0
    for a in n:
        r+=a
    return r

if __name__ == '__main__':
    base = 10
    lj=250
    red=[[]]*lj
    l = 250
    n=0
    while n<lj:
        r = []
        i = 0
        while i<l:
            a=foo(n^i)
            while len(a)>1:
                a=foo(bar(a))
            r+=a
            i+=1
        print(str(n)+": "+str(r))
        red[n]=r
        n+=1


    green=[[]]*lj
    n=0
    while n<lj:
        r = []
        i = 0
        while i<l:
            a=foo(n&i)
            while len(a)>1:
                a=foo(bar(a))
            r+=a
            i+=1
        print(str(n)+": "+str(r))
        green[n]=r
        n+=1


    blue=[[]]*lj
    n=0
    while n<lj:
        r = []
        i = 0
        while i<l:
            a=foo(n|i)
            while len(a)>1:
                a=foo(bar(a))
            r+=a
            i+=1
        print(str(n)+": "+str(r))
        blue[n]=r
        n+=1

    size = 4

    pygame.init()
    global surface
    surface = pygame.display.set_mode((l*size, lj*size), 0, 32)

    cycle = 0

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        y = 0
        while y < lj:
            x = 0
            while x < l:
                d = math.floor(255 / base * red[y][x])
                f = math.floor(255 / base * green[y][x])
                g = math.floor(255 / base * blue[y][x])

                h=cycle%6
                if h==0:
                    c=d
                    v=f
                    b=g
                elif h==1:
                    c=f
                    v=g
                    b=d
                elif h==2:
                    c=g
                    v=d
                    b=f
                elif h==3:
                    c=g
                    v=f
                    b=d
                elif h==4:
                    c=d
                    v=g
                    b=f
                elif h==5:
                    c=f
                    v=d
                    b=g
                pygame.draw.rect(surface, (c, v, b), (size * x, size * y, size, size))
                x += 1
            y += 1

        pygame.display.update()
        time.sleep(0.1)
        cycle+=1


