import pygame
import sys

       
TAMANHO_CELULA = 40
LINHAS_TABULEIRO = 12 
COLUNAS_TABULEIRO = 12  
largura_tela = 800  
altura_tela = 600  



opcoes_busca = ["Busca em Profundidade", "Busca em Largura","Hill Climb","Sair"]
tipo_busca_selecionado = None

def menu_selecao_busca():
    import pygame
    import sys
    from src.hill_climb import busca_hill_climbing
    from src.busca_largura import busca_em_largura
    from src.busca_profundidade import busca_em_profundidade
    global tipo_busca_selecionado
    
    pygame.init()
    pygame.mixer.init()
   
    tela = pygame.display.set_mode((largura_tela, altura_tela))
    pygame.display.set_caption("Menu de Seleção de Busca")
    font = pygame.font.Font("./font/RockSalt-Regular.ttf", 25)  
    selected_option = 0

    
    pygame.mixer.music.load("./assets/music/Ori and the Blind Forest – Main Theme [Menu Music].mp3")
    pygame.mixer.music.play(-1)  

    imagem_fundo = pygame.image.load("./assets/img/fundo.jpg") 
    imagem_fundo = pygame.transform.scale(imagem_fundo, (largura_tela, altura_tela))  

    espaco_entre_botoes = 20  
    altura_total_botoes = (len(opcoes_busca) * (font.get_height() + espaco_entre_botoes)) - espaco_entre_botoes
    button_start_y = (altura_tela - altura_total_botoes) // 2  

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
                    elif tipo_busca_selecionado == "Hill Climb":
                        busca_hill_climbing()
                    elif tipo_busca_selecionado == "Sair":
                        pygame.mixer.music.stop()
                        pygame.quit()
                        sys.exit()
                        
                    
                    pygame.time.wait(2000) 
                    if tipo_busca_selecionado != "Hill Climb": mensagem_vitoria()
                    selected_option = 0

        tela.fill((0, 0, 0))  
        tela.blit(imagem_fundo, (0, 0))  

        title_text = font.render("Selecione o Tipo de Busca", True, (255, 255, 255))
        tela.blit(title_text, (largura_tela // 2 - title_text.get_width() // 2, 50))

        for i, option in enumerate(opcoes_busca):
            option_text = font.render(option, True, (255, 255, 255))
            button_width = option_text.get_width() + 20  
            button_height = option_text.get_height() + 10
            button_x = largura_tela // 2 - button_width // 2
            button_y = button_start_y + i * (button_height + espaco_entre_botoes)  

            button_color = (100, 100, 255) if i == selected_option else (50, 50, 50)
            pygame.draw.rect(tela, button_color, (button_x, button_y, button_width, button_height), border_radius=10)

            tela.blit(option_text, (button_x + (button_width - option_text.get_width()) // 2,
                                button_y + (button_height - option_text.get_height()) // 2))

        pygame.display.flip()



imagem_labirinto = pygame.image.load('./assets/img/map.png')  
imagem_labirinto = pygame.transform.scale(imagem_labirinto, (TAMANHO_CELULA * COLUNAS_TABULEIRO, TAMANHO_CELULA * LINHAS_TABULEIRO))

def desenhar_tabuleiro(tela, agente_pos,num_passos ):
    
    font = pygame.font.SysFont('arial', 24)
    texto_passos = font.render(f"    Número de Passos: {num_passos}", True, (0,0,0))
    agente_img = pygame.image.load('./assets/img/agente_maca.png')

    largura_tabuleiro = (TAMANHO_CELULA) * COLUNAS_TABULEIRO  
    altura_tabuleiro = (TAMANHO_CELULA) * LINHAS_TABULEIRO    

    pos_x_inicial = (800 - largura_tabuleiro) // 2  
    pos_y_inicial = (600 - altura_tabuleiro) // 2   

    tela.blit(imagem_labirinto, (pos_x_inicial, pos_y_inicial))
    tela.blit(texto_passos, (10, 10))  

    x, y = agente_pos
    pos_x_agente = pos_x_inicial + TAMANHO_CELULA * y
    pos_y_agente = pos_y_inicial + TAMANHO_CELULA * x

    agente_img = pygame.transform.scale(agente_img, (TAMANHO_CELULA, TAMANHO_CELULA))
    tela.blit(agente_img, (pos_x_agente, pos_y_agente))


def animar_movimento(caminho):
    pygame.init()
    tela = pygame.display.set_mode((largura_tela, altura_tela))
    pygame.display.set_caption("Movimento do Agente")
    num_passos = 0  
    clock = pygame.time.Clock()

    print(f"Passos após incremento: {num_passos}")  
    for pos in caminho:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        
        tela.fill((129,164,205)) 
        desenhar_tabuleiro(tela, pos, num_passos)  
        num_passos = num_passos + 1
        pygame.display.update()  
        clock.tick(4)  

def mensagem_vitoria():
    font = pygame.font.Font("./font/RockSalt-Regular.ttf", 30)
    vitoria_text = font.render("Parabéns, você venceu!", True, (255, 255, 255))
    tela = pygame.display.get_surface()
    tela.fill((0, 0, 0)) 
    tela.blit(vitoria_text, (largura_tela // 2 - vitoria_text.get_width() // 2, altura_tela // 2))
    pygame.display.flip()
    pygame.time.wait(2000)  
