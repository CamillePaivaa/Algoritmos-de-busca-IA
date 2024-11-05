import pygame
import sys
from tabuleiro import tabuleiro_inicial



# Cores
COR_CAMINHO = (255, 255, 255)     # Branco para o caminho
COR_OBSTACULO = (0, 0, 0)         # Preto para o obstáculo
COR_AGENTE = (0, 0, 255)          # Azul para o agente
TAMANHO_CELULA = 40
MARGEM = 2
LINHAS_TABULEIRO = 12 # Número de linhas no tabuleiro
COLUNAS_TABULEIRO = 12  # Número de colunas no tabuleiro



# Opções de busca para o menu
opcoes_busca = ["Busca em Profundidade", "Busca em Largura","Sair"]
tipo_busca_selecionado = None

def menu_selecao_busca():

    from busca_largura import busca_em_largura
    from busca_profundidade import busca_em_profundidade
    global tipo_busca_selecionado
    pygame.init()
    largura_tela = (TAMANHO_CELULA + MARGEM) * COLUNAS_TABULEIRO + MARGEM
    altura_tela = (TAMANHO_CELULA + MARGEM) * LINHAS_TABULEIRO + MARGEM

    tela = pygame.display.set_mode((largura_tela, altura_tela))
    pygame.display.set_caption("Menu de Seleção de Busca")

    font = pygame.font.Font(None, 36)
    selected_option = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(opcoes_busca)
                elif event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(opcoes_busca)
                elif event.key == pygame.K_RETURN:
                    tipo_busca_selecionado = opcoes_busca[selected_option]
                    print(f"Tipo de Busca Selecionado: {tipo_busca_selecionado}")

                    if tipo_busca_selecionado == "Busca em Profundidade":
                        busca_em_profundidade()
                    elif tipo_busca_selecionado == "Busca em Largura":
                        busca_em_largura()
                    elif tipo_busca_selecionado == "Sair":
                        pygame.quit()
                        sys.exit()

                    # Após a busca, resetar a seleção para a primeira opção
                    selected_option = 0

        tela.fill((0, 0, 0))  # Cor de fundo preta
        title_text = font.render("Selecione o Tipo de Busca", True, (255, 255, 255))
        tela.blit(title_text, (largura_tela // 2 - title_text.get_width() // 2, 50))

        # Desenha as opções
        for i, option in enumerate(opcoes_busca):
            color = (100, 100, 255) if i == selected_option else (255, 255, 255)
            option_text = font.render(option, True, color)
            tela.blit(option_text, (largura_tela // 2 - option_text.get_width() // 2, 150 + i * 50))
            

        pygame.display.flip()

def desenhar_tabuleiro(tela, agente_pos):
    tabuleiro = tabuleiro_inicial()
    for x in range(len(tabuleiro)):
        for y in range(len(tabuleiro[0])):
            cor = COR_CAMINHO if tabuleiro[x][y] == 1 else COR_OBSTACULO
            if (x, y) == agente_pos:
                cor = COR_AGENTE
            pygame.draw.rect(
                tela,
                cor,
                [(MARGEM + TAMANHO_CELULA) * y + MARGEM,
                 (MARGEM + TAMANHO_CELULA) * x + MARGEM,
                 TAMANHO_CELULA,
                 TAMANHO_CELULA]
            )

def animar_movimento(tabuleiro, caminho):
    pygame.init()
    largura_tela = len(tabuleiro[0]) * (TAMANHO_CELULA + MARGEM)
    altura_tela = len(tabuleiro) * (TAMANHO_CELULA + MARGEM)
    tela = pygame.display.set_mode((largura_tela, altura_tela))
    pygame.display.set_caption("Movimento do Agente")

    clock = pygame.time.Clock()
    for pos in caminho:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        
        tela.fill((0, 0, 0))  # Cor de fundo da tela
        desenhar_tabuleiro(tela, pos)
        pygame.display.flip()
        clock.tick(7)  # Controle de FPS para a velocidade de movimento

  

