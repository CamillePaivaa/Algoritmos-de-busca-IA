from src.tabuleiro import tabuleiro_inicial
from src.agente import posicionar_movimentar_agente
from src.interface_grafica import animar_movimento

def busca_hill_climbing():
    codigo_busca = 'busca_hill_climbing'
    tabuleiro = tabuleiro_inicial()

    caminho = posicionar_movimentar_agente(codigo_busca, tabuleiro)
    animar_movimento(caminho)
