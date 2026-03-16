class Soldado:
    def __init__(self, soldo, dano):
        self.soldo = soldo
        self.dano = dano

class Miliciano(Soldado):
    def __init__(self):
        super().__init__(soldo=1, dano=1)

class Espadachim(Soldado):
    def __init__(self):
        super().__init__(soldo=5, dano=5)
