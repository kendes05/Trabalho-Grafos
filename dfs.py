"""
  Execution:    python depth_first_search.py filename.txt s
  Data files:   https: // algs4.cs.princeton.edu / 41graph / tinyG.txt
                https: // algs4.cs.princeton.edu / 41graph / mediumG.txt

  Run depth first search on an undirected graph.
  Runs in O(E + V) time.

 % python depth_first_search.py tinyG.txt 0
  0 1 2 3 4 5 6
  NOT connected

 % python depth_first_search.py tinyG.txt 9
  9 10 11 12
  NOT connected

 """


class DepthFirstSearch:

    def __init__(self, G, s, newValue):
        self.sourceValue = G.value[s]
        self.marked = [False for _ in range(G.V)]
        self.dfs(G, s, newValue)

    def dfs(self, G, s, newValue):
        stack = [s]
        while stack:
            v = stack.pop() 

            if self.marked[v]: 
                continue

            if G.value[v] != self.sourceValue:
                continue

            G.value[v] = newValue 
            self.marked[v] = True 

            for w in G.adj[v]:
                if not self.marked[w]:
                    stack.append(w)

    @staticmethod
    def execute(G, s, newValue):
        DepthFirstSearch(G, s, newValue)
        return G

