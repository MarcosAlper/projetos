import pygame
import sys

class TextLabel:
    def __init__(self, text, font, color, **kwargs):
        self._text = text
        self.font = font
        self.color = color
        self.kwargs = kwargs
        self.render()

    def render(self):
        # Cria a imagem e obtém o retângulo
        self.surface = self.font.render(self._text, True, self.color)
        self.rect = self.surface.get_rect(**self.kwargs)
    
    def set_text(self, new_text):
        if self._text != new_text:
            self._text = new_text
            self.render()
    
    def draw(self, screen):
        screen.blit(self.surface, self.rect)
