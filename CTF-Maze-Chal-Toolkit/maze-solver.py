#!/usr/bin/env python3

def Dijkstra(Graph, source):
   # Graph[u][v] is the weight from u to v (however 0 means infinity)
   infinity = float('infinity')
   n = len(graph)
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


def display_solution(predecessor):
   cell = len(predecessor)-1
   while cell:
       print(cell,end='<')
       cell = predecessor[cell]
   print(0)

def solve(graph):
    display_solution(Dijkstra(graph, 0)[1])

def getSolution(graph):
    predecessor = Dijkstra(graph, 0)[1]
    cell = len(predecessor)-1
    solution = []
    while cell:
        solution = [cell] + solution
        cell = predecessor[cell]
    return [0] + solution

graph = (        # or ones on the diagonal
    (0,1,0,0,0,0),
    (1,0,1,0,1,0),
    (0,1,0,0,0,1),
    (0,0,0,0,1,0),
    (0,1,0,1,0,0),
    (0,0,1,0,0,0))


solve(graph)
print(getSolution(graph))
