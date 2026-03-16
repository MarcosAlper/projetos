from random import randint

class Populacao:
    def __init__(self, tamanho_vila="pequena"):
        self.populacao = []
        if tamanho_vila == "pequena":
            self.tam_populacional = randint(40, 71)
        for _ in range(self.tam_populacional):
            self.populacao.append(Pessoa)
    
    def populacao_total(self):
        return len(self.populacao)

class Pessoa:
    def __init__(self, nome="nome", idade=20):
        self.nome = nome
        self.idade = idade
