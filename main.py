from graph import Graph
from dfs import DepthFirstSearch
from PIL import Image
import numpy as np

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

def matriz_para_imagem(matriz, mapa_cores):
    linhas, colunas = len(matriz), len(matriz[0])
    img = Image.new("RGB", (colunas, linhas))

    pixels = img.load()
    for i in range(linhas):
        for j in range(colunas):
            pixels[j, i] = mapa_cores.get(matriz[i][j], (0, 0, 0))

    img.show()

mapa_cores = {
    0: (0, 0, 255),
    255: (255, 255, 255),
    72: (128, 128, 128),        
}


matrix = read_matrix_from_file("UNIFOR_grayscale.txt")
#matrix = [[1,1,1],[0,0,0],[0,0,1]]
g = create_graph(matrix)

#matriz_para_imagem(matrix,mapa_cores)



g = DepthFirstSearch.execute(g,313100,0)
matrix = graph_to_matrix(g)


matriz_para_imagem(matrix,mapa_cores)


