from src.tabuleiro import tabuleiro_inicial
from src.agente import posicionar_movimentar_agente
from src.interface_grafica import animar_movimento

def busca_em_profundidade(): 
    tabuleiro = tabuleiro_inicial()  
    codigo_busca = 'busca_profundidade'
   
   
    caminho= posicionar_movimentar_agente(codigo_busca, tabuleiro)
    animar_movimento(caminho)
