#!/usr/bin/env python2

from random import shuffle, randrange
from math import floor, ceil
from collections import defaultdict
from subprocess import call
import string
import random

flagg = ""
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

#Build tree from adjacency matrix
def adjMat_Tree(matrix, cell = 0):
    tree = {cell: {}}
    for conn in range(len(matrix[cell])):
        if matrix[cell][conn]:
            matrix[conn][cell] = 0 # Block backtracing
            if cell in tree:
                tree[cell] = {**tree[cell], **adjMat_Tree(matrix, conn)}
            else:
                tree[cell] = adjMat_Tree(matrix, conn)
            matrix[cell][conn] = 0 # Block remapping
    return tree

# Solve maze
def Dijkstra(Graph, source):
   # Graph[u][v] is the weight from u to v (however 0 means infinity)
   infinity = float('infinity')
   n = len(Graph)
   dist = [infinity]*n   # Unknown distance function from source to v
   previous = [infinity]*n # Previous node in optimal path from source
   dist[source] = 0        # Distance from source to source
   Q = list(range(n)) # All nodes in the graph are unoptimized - thus are in Q
   while Q:           # The main loop
       u = min(Q, key=lambda n:dist[n])                 # vertex in Q with smallest dist[]
       Q.remove(u)
       if dist[u] == infinity:
           break # all remaining vertices are inaccessible from source
       for v in range(n):               # each neighbor v of u
           if Graph[u][v] and (v in Q): # where v has not yet been visited
               alt = dist[u] + Graph[u][v]
               if alt < dist[v]:       # Relax (u,v,a)
                   dist[v] = alt
                   previous[v] = u
   return dist,previous

def getSolution(Graph):
    predecessor = Dijkstra(Graph, 0)[1]
    cell = len(predecessor)-1
    solution = []
    while cell:
        solution = [cell] + solution
        cell = predecessor[cell]
    return [0] + solution

maze, adjMap = make_maze(mazeWidth, mazeHeight)
solution = getSolution(adjMap)
tree = adjMat_Tree(adjMap)

# print(maze)
# print(tree)
# print(solution)

# Actually build chall and save it to the disk
# call("mkdir Enter/", shell=True) # Make Folder
def buildDir(dirTree, lastPath = 0, currPath = 'Enter/'):
    for path in dirTree:
        direction = ""
        if path == lastPath+1: currPath += "Right/"
        elif path == lastPath-1: currPath += "Left/"
        elif path == lastPath-mazeWidth: currPath += "Up/"
        elif path == lastPath+mazeWidth: currPath += "Down/"

        call("mkdir " + currPath, shell=True) # Make Folder

        if path == 0:
            f = open(currPath + "map.mp4", 'w')
            f.write(maze)
            f.close()
            if len(dirTree[path]) == 1:
                call("echo And so you begin your great journey... Only on way ahead, straight ahead!!\\\\n\\(You\\'re in the top left, get to the bottom right\\) > " + currPath + "readme.txt", shell=True)
            else:
                call("echo And so your epic quest begins, with a choice.  You don\\'t have a good feeling about this.\\\\n\\(You\\'re in the top left, get to the bottom right\\) > " + currPath + "readme.txt", shell=True)
        elif path == 23:
            scramble = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(8))
            call("echo flag{" + flagg + scramble + "} >" + currPath + "flag", shell=True)
        else:
            # print(path, len(dirTree[path]), '', end='')
            if len(dirTree[path]) == 1:
                call("echo And the path, to you, remains clear. > " + currPath + "readme.txt", shell=True)
            else:
                call("echo You reach a crossroads.  You feel crushed under the pressure of having to make yet another choice in this endless monotony of the infinite. > " + currPath + "readme.txt", shell=True)
                # There's a fork in the road.  You consider picking it up, but you don't have any clue where its been and decide it's probably better to look up and decide which path you're going to take.

        buildDir(dirTree[path], path, currPath)
        currPath = "/".join(currPath.split("/")[:-2]) + '/'

    if not len(dirTree):
        call("echo And yet again, you find yourself faced with a wall.  You feel that you might have strayed from the path. > " + currPath + "readme.txt", shell=True)


buildDir(tree)
