# Codigo feito por Júlio César ^_____^
# Aqui declaramos a lista de numeros que vai compor a piarmide.
caminho = [
    [75],
    [95,64],
    [17,47,82],
    [18,35,87,10],
    [20,4,82,47,65],
    [19,1,23,75,3,34],
    [88,2,77,73,7,63,67],
    [99,65,4,28,6,16,70,92],
    [41,41,26,56,83,80,70,33],
    [41,48,72,33,47,32,37,16,94,29],
    [53,71, 44,65,25,43,91,52,97,51,14],
    [70,11,33,28,77,73,17,78,39,68,17,57],
    [91,71,52,38,17,14,91,43,58,50,27,29,48],
    [63,66,4,68,89,53,67,30,73,16,69,87,40,31],
    [4,62,98,27,23,9,70,98,73,93,38,53,60,4,23]
]

# Delaramos a variavel que cria uma cópia da pirâmide original para exibição.
caminho_original = [row[:] for row in caminho]

# Delaramos a variavel que cria uma lista para armazenar o caminho máximo.
caminho_maximo = [[0] * len(row) for row in caminho]

# loop que faz o caminho de baixo para cima na pirâmide para calcular a soma máxima.
for linha in range(len(caminho) - 2, -1, -1):
    for coluna in range(len(caminho[linha])):
        # aqui temos a certeza de que o índice está dentro dos limites.
        if coluna < len(caminho[linha + 1]) and (coluna + 1) < len(caminho[linha + 1]):
            if caminho[linha + 1][coluna] > caminho[linha + 1][coluna + 1]:
                caminho[linha][coluna] += caminho[linha + 1][coluna]
                caminho_maximo[linha][coluna] = coluna  # Armazena o índice do caminho escolhido.
            else:
                caminho[linha][coluna] += caminho[linha + 1][coluna + 1]
                caminho_maximo[linha][coluna] = coluna + 1  # Armazena o índice do caminho escolhido.

# Declaramos a variavel que faz o elemento no topo da pirâmide guarda a soma máxima.
soma_maxima = caminho[0][0]
print("A soma máxima do melhor caminho é:", soma_maxima)
print("E o melhor caminho é:")
# Exibi a pirâmide com o caminho máximo em vermelho usando os valores originais.
linha_atual = 0
coluna_atual = 0

# Calcula o comprimento máximo da linha para centralizar a pirâmide.
max_len = len(caminho[-1])

for linha in range(len(caminho_original)):
    # Calcula o número de espaços à esquerda para centralizar a linha.
    num_espacos = max_len - len(caminho_original[linha])
    print(" " * num_espacos, end="")
    for coluna in range(len(caminho_original[linha])):
        if coluna == coluna_atual:
            # Imprimi o elemento em vermelho se ele fizer parte do caminho máximo
            print(f"\033[91m{caminho_original[linha][coluna]}\033[0m", end=" ")
        else:
            # Imprimi o elemento normalmente se ele não fizer parte do caminho máximo.
            print(caminho_original[linha][coluna], end=" ")
    print()  # Pula para a próxima linha.
    if linha < len(caminho_maximo) - 1:
        # Atualiza o índice da coluna atual para seguir o caminho máximo.
        coluna_atual = caminho_maximo[linha][coluna_atual]
