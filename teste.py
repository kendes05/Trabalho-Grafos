from graph import Graph
from dfs import DepthFirstSearch

g = Graph(6)

g.add_edge(0,10,1,4)
g.add_edge(1,4, 2,2)
g.add_edge(0,10,2, 2)
g.add_edge(3,10,0,10)
g.add_edge(3,10,1,4)
g.add_edge(4,0,5,100)


print(g)

