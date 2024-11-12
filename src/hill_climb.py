from src.tabuleiro import tabuleiro_inicial
from src.interface_grafica import animar_movimento

def hill_climbing():
    x = 4
    y = 11
    destino = (10, 0)
    destino_x, destino_y = destino
    visitados = set()
    tabuleiro = tabuleiro_inicial()
    agente = 2
    caminho = []  # Lista para salvar o caminho percorrido pelo agente
    
    # Verifica se a posição inicial e o destino estão dentro dos limites
    if not (0 <= x < len(tabuleiro) and 0 <= y < len(tabuleiro[0])) or \
       not (0 <= destino_x < len(tabuleiro) and 0 <= destino_y < len(tabuleiro[0])):
        raise ValueError("Posição inicial ou destino fora dos limites do tabuleiro")
    
    while (x, y) != destino:
        visitados.add((x, y))
        caminho.append((x, y))  # Salva a posição atual no caminho
        
        # Calcule as distâncias para os vizinhos, com verificações de limite
        vizinhos = []
        if x - 1 >= 0:
            vizinhos.append(((x - 1, y), abs(destino_x - (x - 1)) + abs(destino_y - y)))  # Cima
        if x + 1 < len(tabuleiro):
            vizinhos.append(((x + 1, y), abs(destino_x - (x + 1)) + abs(destino_y - y)))  # Baixo
        if y - 1 >= 0:
            vizinhos.append(((x, y - 1), abs(destino_x - x) + abs(destino_y - (y - 1))))  # Esquerda
        if y + 1 < len(tabuleiro[0]):
            vizinhos.append(((x, y + 1), abs(destino_x - x) + abs(destino_y - (y + 1))))  # Direita
        
        # Filtra os vizinhos viáveis que não foram visitados e são acessíveis (tabuleiro[x][y] == 1)
        vizinhos = [(pos, dist) for pos, dist in vizinhos 
                    if pos not in visitados and 0 <= pos[0] < len(tabuleiro) 
                    and 0 <= pos[1] < len(tabuleiro[0]) and tabuleiro[pos[0]][pos[1]] == 1]
        
        if not vizinhos:
            return False  # Sem vizinhos viáveis, sem solução

        # Seleciona o vizinho com a menor distância heurística
        (x, y), _ = min(vizinhos, key=lambda item: item[1])
        
        # Marca a posição atual do agente no tabuleiro
        tabuleiro[x][y] = agente

    # Adiciona a posição final no caminho
    caminho.append(destino)
    
    # Chama a função de animação passando o caminho percorrido
    animar_movimento(tabuleiro, caminho)
