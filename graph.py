"""
   Execution:    python graph.py input.txt
   Dependencies: Bag.java Stack.java In.java StdOut.java
   Data files:   https://algs4.cs.princeton.edu/41graph/tinyG.txt
                 https://algs4.cs.princeton.edu/41graph/mediumG.txt
                 https://algs4.cs.princeton.edu/41graph/largeG.txt
 
   A graph, implemented using an array of sets.
   Parallel edges and self-loops allowed.
 
   % python graph.py < tinyG.txt
   13 vertices, 13 edges 
   0: 6 2 1 5 
   1: 0 
   2: 0 
   3: 5 4 
   4: 5 6 3 
   5: 3 4 0 
   6: 0 4 
   7: 8 
   8: 7 
   9: 11 10 12 
   10: 9 
   11: 9 12 
   12: 11 9 
 
   % python graph.py < mediumG.txt
   250 vertices, 1273 edges 
   0: 225 222 211 209 204 202 191 176 163 160 149 114 97 80 68 59 58 49 44 24 15 
   1: 220 203 200 194 189 164 150 130 107 72 
   2: 141 110 108 86 79 51 42 18 14 
   ...
 """
from bag import Bag


class Graph:

    def __init__(self):
        self.E = 0
        self.adj = {}   


    def add_edge(self, v, w):
        if v not in self.adj:
            self.adj[v] = Bag()
        if w not in self.adj:
            self.adj[w] = Bag()

        self.adj[v].add(w)
        self.adj[w].add(v)
        self.E += 1

    def __str__(self):
        s = "%d arestas\n" % (self.E)
        for v in self.adj:
            s += "%s: %s\n" % (v, str(self.adj[v]))
        return s
    def get_neighbors(self, i, j, rows, cols):
        neighbors = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < rows and 0 <= nj < cols:
                neighbors.append(self.to_index(ni, nj, cols))
        return neighbors

    def to_index(self, i, j, cols):
        return i * cols + j        
