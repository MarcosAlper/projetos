import pygame
import sys
import os
from TextLabel import TextLabel
from inventario import Inventario
from populacao import Populacao
from botoes import Botao

def criar_labels_inventario():
    recursos_labels.clear()
    current_y = START_Y

    for categoria, itens in inventario_gerenciador.recursos.items():
        categoria_label = TextLabel(categoria.capitalize(), FONTE_MEDIA2, BRANCO, centerx=LARGURA//8, top=current_y)
        recursos_labels.append(categoria_label)
        current_y += LINE_HEIGHT_MED2

        for index_item, (item, quantidade) in enumerate(itens.items()):
            item_label = TextLabel(f"{item.replace('_', ' ').title()}: {quantidade}", FONTE_PEQUENA, BRANCO, left=START_X, top=current_y)
            recursos_labels.append(item_label)
            if index_item != len(itens) - 1:
                current_y += LINE_HEIGHT_PEQ
            else:
                current_y += LINE_HEIGHT_MED2

# CONFIGS INICIAIS
# Largura e altura da janela
LARGURA, ALTURA = 800, 500
# Centro da tela
CENTRO_X, CENTRO_Y = LARGURA // 2, (ALTURA // 2)

# Cores (RGB)
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)

# Texto
GRANDE = 48
MEDIO1 = 32
MEDIO2 = 28
PEQUENO = 21

LINE_HEIGHT_GRA = 48
LINE_HEIGHT_MED1 = 32
LINE_HEIGHT_MED2 = 28
LINE_HEIGHT_PEQ = 21

# Botões
LARGURA_BOTAO = 150
ALTURA_BOTAO = 80
COR_BOTAO = (70, 130, 180)
COR_TEXTO = BRANCO

# INICIALIZAÇÃO E CRIAÇÃO DA JANELA
pygame.init()

# Instância da janela
tela = pygame.display.set_mode((LARGURA, ALTURA))

# Título da janela
pygame.display.set_caption("Dail Coille")

FONTE_GRANDE = pygame.font.Font(None, GRANDE)
FONTE_MEDIA1 = pygame.font.Font(None, MEDIO1)
FONTE_MEDIA2 = pygame.font.Font(None, MEDIO2)
FONTE_PEQUENA = pygame.font.Font(None, PEQUENO)

# obter o caminho completo para a pasta do script
IMG_VILA_VOTADINI = "dail_coille_village.png"
DIRETORIO_ATUAL = os.path.dirname(sys.argv[0])
CAMINHO_IMG_VILA_VOTADINI = os.path.join(DIRETORIO_ATUAL, IMG_VILA_VOTADINI)

# PREPARAÇÃO DO TEXTO
inventario_gerenciador = Inventario()
populacao = Populacao()

recursos_labels = []
START_X = 20
START_Y = 78

# PREPARAÇÃO DE BOTÕES
botao_recursos = Botao("Adicionar Pessoa", FONTE_PEQUENA, COR_TEXTO, COR_BOTAO, 10, 380, LARGURA_BOTAO, ALTURA_BOTAO)
botao_teste1 = Botao("Botão 1", FONTE_PEQUENA, COR_TEXTO, COR_BOTAO, 170, 380, LARGURA_BOTAO, ALTURA_BOTAO)
botao_teste2 = Botao("Botão 2", FONTE_PEQUENA, COR_TEXTO, COR_BOTAO, 330, 380, LARGURA_BOTAO, ALTURA_BOTAO)
botao_teste3 = Botao("Botão 3", FONTE_PEQUENA, COR_TEXTO, COR_BOTAO, 490, 380, LARGURA_BOTAO, ALTURA_BOTAO)
botao_teste4 = Botao("Botão 4", FONTE_PEQUENA, COR_TEXTO, COR_BOTAO, 650, 380, LARGURA_BOTAO, ALTURA_BOTAO)

# Instância do Gerenciador
criar_labels_inventario()

# Imagem central
img_vila_votadini = None
rect_img_vila_votadini = None

try:
    img_vila_votadini = pygame.image.load(CAMINHO_IMG_VILA_VOTADINI).convert()
    img_vila_votadini = pygame.transform.scale(img_vila_votadini, (400, 300))
    rect_img_vila_votadini = img_vila_votadini.get_rect()
    rect_img_vila_votadini.center = (CENTRO_X, CENTRO_Y - 50)
except pygame.error as e:
    print(f"Erro ao carregar imagem no caminho {CAMINHO_IMG_VILA_VOTADINI}")
    print("Pygame Error:", e)

# Preparação dos Labels Estáticos
titulo = TextLabel("Dail Coille", FONTE_GRANDE, BRANCO, centerx=LARGURA // 2, top=10)
recursos = TextLabel("Recursos", FONTE_MEDIA1, BRANCO, centerx=LARGURA // 8, top=48)
populacao = TextLabel("População", FONTE_MEDIA1, BRANCO, centerx=(LARGURA // 8) * 7, top=48)

# LOOP PRINCIPAL DO JOGO
running = True
while running:
    # Tratamento de eventos (Fechar a janela)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False
        
        # Verifica clique do mouse
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:  # Botão esquerdo do mouse
                pos_mouse = evento.pos
                # Se botão trabalhadores for clicado
                if botao_recursos.clicado(pos_mouse):
                    print("Botão 'Adicionar Pessoa' clicado!")
                    # Aqui você pode adicionar a lógica para o que acontece quando o botão Recursos é clicado
                if botao_teste1.clicado(pos_mouse):
                    print("Botão 'Botão 1' clicado!")
                if botao_teste2.clicado(pos_mouse):
                    print("Botão 'Botão 2' clicado!")
                if botao_teste3.clicado(pos_mouse):
                    print("Botão 'Botão 3' clicado!")
                if botao_teste4.clicado(pos_mouse):
                    print("Botão 'Botão 4' clicado!")
        # Adicione outros eventos aqui (teclado, mouse, etc.)

    # Preencher a tela com a cor preta
    tela.fill(PRETO)

    # Desenha a imagem central
    if img_vila_votadini:
        tela.blit(img_vila_votadini, rect_img_vila_votadini)
    
    # Desenha o objeto de texto na tela
    titulo.draw(tela)
    recursos.draw(tela)
    populacao.draw(tela)

    # Botões
    botao_recursos.draw(tela)
    botao_teste1.draw(tela)
    botao_teste2.draw(tela)
    botao_teste3.draw(tela)
    botao_teste4.draw(tela)

    for label in recursos_labels:
        label.draw(tela)

    # Atualizar a tela
    pygame.display.flip()

# Encerramento
pygame.quit()
sys.exit()
