class Menu:
    def __init__(self, largura_da_tela=800, altura_da_tela=600):
        self.altura_menu = altura_da_tela
        self.largura_menu = largura_da_tela

    class MenuJogo:
        def __init__(self, titulo="menu jogo", opcoes=None):
            self.titulo = titulo
            self.opcoes = opcoes if opcoes is not None else ["Adicione opções"]

        def desenhar_menu_jogo(self, tela, fonte, cor_fundo, cor_texto):
            tela.fill(cor_fundo)
            if self.titulo:
                titulo_renderizado = fonte.render(self.titulo, True, cor_texto)
                tela.blit(titulo_renderizado, ((self.largura_menu - titulo_renderizado.get_width()) // 2, 100))

            for i, opcao in enumerate(self.opcoes):
                opcao_renderizada = fonte.render(f"{i + 1}. {opcao}", True, cor_texto)
                tela.blit(opcao_renderizada, (50, 160 + i * 40))
