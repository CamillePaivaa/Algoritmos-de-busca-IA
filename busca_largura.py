from collections import deque
from tabuleiro import tabuleiro_inicial
from agente import posicionar_movimentar_agente

def busca_em_largura():
    fronteira = deque()
    posicao_x = 4
    posicao_y = 11
    estado_inicial = (posicao_x, posicao_y)  

    tabuleiro = tabuleiro_inicial()  
    fronteira.append(estado_inicial)
    

   
    posicionar_movimentar_agente(fronteira, tabuleiro, posicao_x, posicao_y)
