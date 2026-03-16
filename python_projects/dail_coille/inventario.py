class Inventario:
    def __init__(self):
        self.recursos = {
            "naturais": {
                "madeira": 0,
                "pedra": 0,
                "ferro bruto": 0,
                "comida": 0
            },
            "fabricados": {
                "ferramentas": 0,
                "armas": 0,
                "armaduras": 0,
                "ferro fundido": 0
            }
        }

    def gastar_recurso(self, tipo, recurso, quantidade):
        if recurso in self.recursos[tipo]:
            if self.recursos[tipo][recurso] >= quantidade:
                self.recursos[tipo][recurso] -= quantidade
                return True
            else:
                print(f"Recursos insuficientes: {recurso}")
                return False
        else:
            print(f"Recurso inválido: {recurso}")
            return False
