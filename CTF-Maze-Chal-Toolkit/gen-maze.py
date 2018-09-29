#!/usr/bin/env python2

from random import shuffle, randrange
from math import floor, ceil

mazeWidth = 6
mazeHeight = 4

def make_maze(w = 6, h = 4):
    # Makes a square grid:
    vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]
    con = [[0] * w*h for _ in range(w*h)]
    ver = [["|  "] * w + ['|'] for _ in range(h)] + [[]]
    hor = [["+--"] * w + ['+'] for _ in range(h + 1)]

    # Carve Out Maze (break walls and build connections):
    def walk(x, y):
        vis[y][x] = 1

        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        shuffle(d)
        for (xx, yy) in d:
            if vis[yy][xx]: continue
            if xx == x:
                hor[max(y, yy)][x] = "+  "
                con[(max(y, yy)*w) + x][(max(y, yy)*w) + x - w] = 1
                con[(max(y, yy)*w) + x - w][(max(y, yy)*w) + x] = 1
            if yy == y:
                ver[y][max(x, xx)] = "   "
                con[(y*w) + max(x, xx)][(y*w) + max(x, xx) - 1] = 1
                con[(y*w) + max(x, xx) - 1][(y*w) + max(x, xx)] = 1
            walk(xx, yy)
    walk(randrange(w), randrange(h))

    # Turn Maze into string:
    s = ""
    for (a, b) in zip(hor, ver):
        s += ''.join(a + ['\n'] + b + ['\n'])
    return s, con

maze, connections = make_maze(mazeWidth, mazeHeight)
print(maze)
print(connections)