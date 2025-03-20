# Ferramenta "Balde de Tinta"

## Descrição

Este projeto implementa a conversão de uma matriz em um grafo, onde cada célula da matriz é representada como um vértice do grafo. Além disso, foi implementado um algoritmo de busca em profundidade (dfs) que funciona como uma ferramenta "balde de tinta", alterando todos os vértices conectados que possuam o mesmo valor de origem.

## Instalação

No terminal, escreva o comando abaixo para instalar as bibliotecas necessárias para o funcionamento do projeto:

```sh
cd Trabalho-Grafos
pip install -r requirements.txt
```

## Estrutura do Projeto

O projeto contém as seguintes classes principais:

- **Graph**: Representa um grafo utilizando listas de adjacência onde cada posição dessa lista terá uma Bag.
- **Bag**: Estrutura auxiliar utilizada para armazenar listas de adjacência.
- **DepthFirstSearch**: Implementa o algoritmo de busca em profundidade (DFS) para modificar os vértices e retorna-lo modificado. Recebe em seu construtor 3 parâmetros: O grafo, o índice do vértice que eu pretendo aplicar o dfs e o novo valor que será aplicado aos vértices conectados.

## Classe `DepthFirstSearch`

A classe `DepthFirstSearch` executa a busca em profundidade a partir de um vértice inicial, alterando todos os vértices conectados que tem o mesmo valor de origem.

### Exemplo

```python
from graph import Graph
from dfs import DepthFirstSearch
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
```

## Para executar

Para rodar o código de teste, basta executar o arquivo main.py do projeto no terminal (Veja se você está na pasta que contém os arquivos main.py e trabalho.py):

```sh
python main.py
```

Para rodar o código do trabalho, basta executar o arquivo trabalho.py no terminal (Veja se você está na pasta que contém os arquivos main.py e trabalho.py):

```sh
python trabalho.py
```
