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
    num_passos = 0

    tabuleiro[posicao_x][posicao_y] = agente  # Colocando o agente na posição inicial
    fronteira.append(estado_inicial)

    while (posicao_x, posicao_y) != (destino_x, destino_y):
       
      
        if fronteira:
            if codigo_busca == 'busca_largura':
                posicao_x, posicao_y = fronteira.popleft()  
           
            elif codigo_busca == 'busca_profundidade':
                 posicao_x, posicao_y = fronteira.pop()
        
            tabuleiro[posicao_x][posicao_y] = agente  
            num_passos += 1
 

        # Verificar as direções: cima, esquerda, direita, baixo
        posicao_acima = posicao_x - 1 
        posicao_esquerda = posicao_y - 1  
        posicao_direita = posicao_y + 1  
        posicao_baixo = posicao_x + 1  

        # Adiciona as novas posições à fronteira, se válidas
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

    conjunto_explorado.append((destino_x, destino_y)) #adicionando o destino no conjunto explorado 
    print('Número de Passos: ', num_passos)
    print('Conjunto explorado: ', conjunto_explorado) 
    return conjunto_explorado  # Retorna o caminho percorrido

