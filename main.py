from graph import Graph
from dfs import DepthFirstSearch


def create_graph(matrix):
    linhas = len(matrix)
    colunas = len(matrix[0])
    vertices = linhas * colunas
    grafo = Graph(vertices)

    for i in range(linhas):
        for j in range(colunas):
            index = grafo.to_index(i, j, colunas)
            value = matrix[i][j]
            neighbors = grafo.get_neighbors(i, j, linhas, colunas)
            for neighbor in neighbors:
                neighbor_i, neighbor_j = divmod(neighbor, colunas)
                neighbor_value = matrix[neighbor_i][neighbor_j]
                
                grafo.add_edge(index, value, neighbor, neighbor_value)

    return grafo

def graph_to_matrix(grafo):
    linhas = int(grafo.V ** 0.5)
    colunas = linhas
    matriz = [[None for _ in range(colunas)] for _ in range(linhas)]
    
    for index, value in grafo.value.items():
        i, j = divmod(index, colunas)
        matriz[i][j] = value
    
    return matriz

def print_matrix(matrix):
    for row in matrix:
        print(row)
    print()

matrix = [
    [1, 1, 1],
    [0, 0, 0],
    [0, 0, 1]
]

grafo = create_graph(matrix)

print("Grafo antes da DFS:")

print(grafo)

matrix = graph_to_matrix(grafo) # Transforma o grafo em uma matriz para melhor visualização

print("\nMatriz antes do DFS:")

print_matrix(matrix)

grafo = DepthFirstSearch.execute(grafo, 0, 2) #Aplicando dfs no vértice de index 0 com valor de origem 2

print("Grafo depois da DFS:")

print(grafo)

matrix = graph_to_matrix(grafo)

print("\nMatriz depois do DFS:")

print_matrix(matrix)

