from PIL import Image
import numpy as np

def matriz_para_imagem(matriz, mapa_cores):
    linhas, colunas = len(matriz), len(matriz[0])
    img = Image.new("RGB", (colunas, linhas))

    pixels = img.load()
    for i in range(linhas):
        for j in range(colunas):
            pixels[j, i] = mapa_cores.get(matriz[i][j], (0, 0, 0))

    img.show()

def read_matrix_from_file(filename):
    matrix = []
    
    with open(filename, 'r') as f:
        for line in f:
            row = list(map(int, line.split()))
            matrix.append(row)
            
    return matrix

matrix = read_matrix_from_file("UNIFOR_sample.txt")


mapa_cores = {
    0: (0, 0, 255), 
    1: (255, 255, 255), 
}

matriz_para_imagem(matrix, mapa_cores)