from calendario import Calendario
from menus import Menu
import pygame
import sys

# --- Pygame Setup ---
pygame.init()

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)

LARGURA_TELA, ALTURA_TELA = 800, 600
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Simulador de Calendário")

fonte = pygame.font.SysFont(None, 28)

# --- Calendário ---
tempo = Calendario()
# --- Menus ---
menu_inicial = Menu(LARGURA_TELA, ALTURA_TELA)
menu_jogo = Menu.MenuJogo(titulo="Simulador de Calendário",
                          opcoes=[
                              "0 - Pausar/Retomar",
                              "1 - Velocidade x1 (2s = 1 dia)",
                              "2 - Velocidade x2 (1s = 1 dia)",
                              "3 - Velocidade x3 (0.5s = 1 dia)",
                              "4 - Velocidade x4 (0.1s = 1 dia)"
                          ])

# -- Gerenciamento de tempo ---
relogio = pygame.time.Clock()
# Dicionário para selecionar velocidade de tempo
velocidades_tempo = {
    1: 2000, # 2 segundo real = 1 dia no jogo
    2: 1000, # 1 segundo real = 1 dias no jogo
    3: 500, # 0.5 segundo real = 1 dia no jogo
    4: 100 # 0.1 segundo real = 1 dia no jogo
}
# Velocidade inicial
velocidade_atual = 1
intervalo_dias = velocidades_tempo[velocidade_atual]
ultimo_avanco_tempo = pygame.time.get_ticks()

# Estado de pausa
pausado = True

# --- Loop Principal ---
rodando = True
while rodando:
    # Checa o tempo e avança o calendário
    if not pausado:
        tempo_atual = pygame.time.get_ticks()
        if tempo_atual - ultimo_avanco_tempo >= intervalo_dias:
            tempo.avancar_tempo(d=1)
            ultimo_avanco_tempo = tempo_atual

    # Processa eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        # Teclas para mudar a velocidade
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_0:
                pausado = not pausado
            elif evento.key == pygame.K_1:
                velocidade_atual = 1
            elif evento.key == pygame.K_2:
                velocidade_atual = 2
            elif evento.key == pygame.K_3:
                velocidade_atual = 3
            elif evento.key == pygame.K_4:
                velocidade_atual = 4
            if not pausado:
                intervalo_dias = velocidades_tempo[velocidade_atual]

    # Limpa a tela
    tela.fill(PRETO)

    # Desenha o menu
    menu_jogo.desenhar_menu(tela, fonte, PRETO, BRANCO)

    # Desenha na tela
    texto_data = fonte.render(tempo.hoje(), True, BRANCO)
    ret_texto = texto_data.get_rect(center=(LARGURA_TELA//2, 20))
    tela.blit(texto_data, ret_texto)
    
    # Atualiza a tela
    pygame.display.flip()

    # Controla a taxa de quadros
    relogio.tick(60)

pygame.quit()
sys.exit()
