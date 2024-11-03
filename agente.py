from collections import deque

def posicionar_movimentar_agente(fronteira_largura, tabuleiro, posicao_x, posicao_y):
    
    agente = 'A'
    tabuleiro[posicao_x][posicao_y] = agente # Colocar o agente na posição inicial
    destino_x = 6
    destino_y = 10
    
    # Verificar para onde o agente pode se mover
    # Seguindo esta ordem: ↑ cima, ← esquerda, → direita e ↓ baixo.

    while (posicao_x, posicao_y) != (destino_x, destino_y):

        posicao_acima = posicao_x - 1 
        posicao_esquerda = posicao_y - 1  
        posicao_direita = posicao_y + 1  
        posicao_baixo = posicao_x + 1  

        if posicao_acima >= 0 and tabuleiro[posicao_acima][posicao_y] == 1:  
            print('Agente pode se mover para cima.')
            fronteira_largura.append((posicao_acima, posicao_y))
        
        if posicao_esquerda >= 0 and tabuleiro[posicao_x][posicao_esquerda] == 1:
            print('Agente pode se mover para a esquerda.')
            fronteira_largura.append((posicao_x, posicao_esquerda))

        if posicao_direita < len(tabuleiro[0]) and tabuleiro[posicao_x][posicao_direita] == 1:
            print('Agente pode se mover para a direita.')
            fronteira_largura.append((posicao_x, posicao_direita)) #adicionando na ultima posição da fila

        if posicao_baixo < len(tabuleiro) and tabuleiro[posicao_baixo][posicao_y] == 1:
            print('Agente pode se mover para baixo.')
            fronteira_largura.append((posicao_baixo, posicao_y))


        print('Fronteira atualizada:', fronteira_largura)

        #Andar com agente seguindo a primeira posição da fronteira
    
        if fronteira_largura:
            posicao_x, posicao_y = fronteira_largura.popleft()  # Obter a nova posição
            tabuleiro[posicao_x][posicao_y] = agente  # Atualizar posição do agente no tabuleiro
            print('Fronteira final: ', fronteira_largura)
            print('Tabuleiro com movimento do agente:')

            for linha in tabuleiro:
                print(linha)

    
    

    
