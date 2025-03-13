from graph import Graph
from dfs import DepthFirstSearch

def read_matrix_from_file(filename):
    matrix = []
    
    with open(filename, 'r') as f:
        for line in f:
            row = list(map(int, line.split()))
            matrix.append(row)
            
    return matrix

def create_graph(matrix):
    linhas = len(matrix)
    colunas = len(matrix[0])
    vertices = linhas * colunas
    grafo = Graph(vertices)


    for i in range(linhas):
        for j in range(colunas):
            index = grafo.to_index(i, j, colunas)
            neighbors = grafo.get_neighbors(i, j, linhas, colunas)
            for neighbor in neighbors:
                grafo.add_edge(index, neighbor)
    
    return grafo


#matrix = read_matrix_from_file("UNIFOR_sample.txt")
matrix = [[1,2,3],[4,5,6],[7,8,9]]
g = create_graph(matrix)
print(g)

search = DepthFirstSearch(g,0)


