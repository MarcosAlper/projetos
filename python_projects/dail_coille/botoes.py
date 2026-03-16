import pygame

class Botao:
    def __init__(self, texto, fonte, cor_texto, cor_fundo, x, y, largura, altura):
        self.texto = texto
        self.fonte = fonte
        self.cor_texto = cor_texto
        self.cor_fundo = cor_fundo
        self.superficie = self.fonte.render(self.texto, True, self.cor_texto)
        self.rect_texto = self.superficie.get_rect()
        self.rect = pygame.Rect(x, y, largura, altura)
        self.rect_texto.center = self.rect.center
    
    def draw(self, tela):
        pygame.draw.rect(tela, self.cor_fundo, self.rect)
        tela.blit(self.superficie, self.rect_texto)

    def clicado(self, pos_mouse):
        return self.rect.collidepoint(pos_mouse)
