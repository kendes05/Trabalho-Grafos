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
        self.sourceValue = G.value[s]  # Valor original do ponto inicial
        self.marked = [False for _ in range(G.V)]
        self.dfs(G, s, newValue)

    def dfs(self, G, v, newValue):
        if self.marked[v]:  # Se já foi visitado, retorna
            return
        
        if G.value[v] != self.sourceValue:  # Se o valor não for igual ao original, não pinta
            return
        
        G.value[v] = newValue  # Pinta com a nova cor
        self.marked[v] = True

        for w in G.adj[v]:  # Percorre os vizinhos
            self.dfs(G, w, newValue) 

    @staticmethod
    def execute(G, s, newValue):
        DepthFirstSearch(G, s, newValue)
        return G

