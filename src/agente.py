from collections import deque


def posicionar_movimentar_agente(codigo_busca, tabuleiro):
    agente = 2
    destino_x = 10
    destino_y = 0
    posicao_x = 4
    posicao_y = 11
    estado_inicial = (posicao_x, posicao_y) 
    conjunto_explorado = []
    fronteira = deque()
    fronteira_sem_repeticao = set()  
    tabuleiro[posicao_x][posicao_y] = agente  
    fronteira.append(estado_inicial)

    while (posicao_x, posicao_y) != (destino_x, destino_y):
       
      
        if fronteira:
            if codigo_busca == 'busca_hill_climbing':
                caminho, sucesso = busca_hill_climbing(
                    tabuleiro, estado_inicial, (destino_x, destino_y), distancia_manhattan
                )
                if not sucesso:
                    print("Busca falhou.")
                return caminho
            if codigo_busca == 'busca_largura':
                posicao_x, posicao_y = fronteira.popleft()  
           
            elif codigo_busca == 'busca_profundidade':
                 posicao_x, posicao_y = fronteira.pop()
        
            tabuleiro[posicao_x][posicao_y] = agente  

        posicao_acima = posicao_x - 1 
        posicao_esquerda = posicao_y - 1  
        posicao_direita = posicao_y + 1  
        posicao_baixo = posicao_x + 1  


        if posicao_acima >= 0 and tabuleiro[posicao_acima][posicao_y] == 1 and (posicao_acima, posicao_y) not in fronteira_sem_repeticao:
            fronteira.append((posicao_acima, posicao_y))
            fronteira_sem_repeticao.add((posicao_acima, posicao_y))
        
        if posicao_esquerda >= 0 and tabuleiro[posicao_x][posicao_esquerda] == 1 and (posicao_x, posicao_esquerda) not in fronteira_sem_repeticao:
            fronteira.append((posicao_x, posicao_esquerda))
            fronteira_sem_repeticao.add((posicao_x, posicao_esquerda))
        
        if posicao_direita < len(tabuleiro[0]) and tabuleiro[posicao_x][posicao_direita] == 1 and (posicao_x, posicao_direita) not in fronteira_sem_repeticao:
            fronteira.append((posicao_x, posicao_direita)) 
            fronteira_sem_repeticao.add((posicao_x, posicao_direita))
        
        if posicao_baixo < len(tabuleiro) and tabuleiro[posicao_baixo][posicao_y] == 1 and (posicao_baixo, posicao_y) not in fronteira_sem_repeticao:
            fronteira.append((posicao_baixo, posicao_y))
            fronteira_sem_repeticao.add((posicao_baixo, posicao_y))
    
        conjunto_explorado.append((posicao_x, posicao_y))

    if (destino_x, destino_y) not in conjunto_explorado:
     conjunto_explorado.append((destino_x, destino_y)) 

    print('Conjunto explorado: ', conjunto_explorado) 

    
    return conjunto_explorado


def busca_hill_climbing(tabuleiro, inicio, objetivo, heuristica):

    posicao_atual = inicio
    caminho = [posicao_atual]
    linhas = len(tabuleiro)
    colunas = len(tabuleiro[0])

    while posicao_atual != objetivo:
        linha, coluna = posicao_atual
        vizinhos = [
            (linha - 1, coluna),  
            (linha + 1, coluna),  
            (linha, coluna - 1), 
            (linha, coluna + 1)   
        ]

        vizinhos_validos = [
            (l, c) for l, c in vizinhos
            if 0 <= l < linhas and 0 <= c < colunas and tabuleiro[l][c] == 1
        ]

        
        proximo = None
        melhor_heuristica = float('inf')
        for vizinho in vizinhos_validos:
            h = heuristica(vizinho, objetivo)
            if h < melhor_heuristica:
                melhor_heuristica = h
                proximo = vizinho

        
        if proximo is None or melhor_heuristica >= heuristica(posicao_atual, objetivo):
            print("Busca falhou!")
            return caminho, False


        posicao_atual = proximo
        caminho.append(posicao_atual)

    return caminho, True


def distancia_manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
