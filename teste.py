from graph import Graph
from dfs import DepthFirstSearch

g = Graph(5)

g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(3, 4)

search = DepthFirstSearch(g,0)
for v in range(g.V):
    if search.marked[v]:
        print(str(v) + " ")

if search.count == g.V:
    print("connected")
else:
    print("not connected")

