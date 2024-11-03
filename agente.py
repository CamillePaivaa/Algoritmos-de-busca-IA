from collections import deque

def posicionar_movimentar_agente(fronteira_largura, tabuleiro, posicao_x, posicao_y):
    
    agente = 2
    destino_x = 10
    destino_y = 0
    conjunto_explorado = set()
    fronteira_sem_repeticao = set()
    num_passos = 0
    tabuleiro[posicao_x][posicao_y] = agente  # Colocando o agente na posição inicial


    while (posicao_x, posicao_y) != (destino_x, destino_y):

        print('Fronteira:', fronteira_largura)
        conjunto_explorado.add((posicao_x, posicao_y))
       
        
        if fronteira_largura:
            posicao_x, posicao_y = fronteira_largura.popleft()  
            tabuleiro[posicao_x][posicao_y] = agente  
            num_passos += 1

            for linha in tabuleiro:
             print(linha)

        # Verificar as direções: cima, esquerda, direita, baixo
        posicao_acima = posicao_x - 1 
        posicao_esquerda = posicao_y - 1  
        posicao_direita = posicao_y + 1  
        posicao_baixo = posicao_x + 1  

        if posicao_acima >= 0 and tabuleiro[posicao_acima][posicao_y] == 1 and (posicao_acima, posicao_y) not in fronteira_sem_repeticao:
            fronteira_largura.append((posicao_acima, posicao_y))
            fronteira_sem_repeticao.add((posicao_acima, posicao_y))
           
        if posicao_esquerda >= 0 and tabuleiro[posicao_x][posicao_esquerda] == 1 and (posicao_x, posicao_esquerda) not in fronteira_sem_repeticao:
            fronteira_largura.append((posicao_x, posicao_esquerda))
            fronteira_sem_repeticao.add((posicao_x, posicao_esquerda))
           
        if posicao_direita < len(tabuleiro[0]) and tabuleiro[posicao_x][posicao_direita] == 1 and (posicao_x, posicao_direita) not in fronteira_sem_repeticao:
            fronteira_largura.append((posicao_x, posicao_direita)) 
            fronteira_sem_repeticao.add((posicao_x, posicao_direita))
           
        if posicao_baixo < len(tabuleiro) and tabuleiro[posicao_baixo][posicao_y] == 1 and (posicao_baixo, posicao_y) not in fronteira_sem_repeticao:
            fronteira_largura.append((posicao_baixo, posicao_y))
            fronteira_sem_repeticao.add((posicao_baixo, posicao_y))
            
        print('Fronteira após explorar:', fronteira_largura)
        print('Conjunto explorado:', conjunto_explorado)
        

    print('Número de passos:', num_passos)
    print("\n\n Parabéns Você chegou no destino final")
    
   