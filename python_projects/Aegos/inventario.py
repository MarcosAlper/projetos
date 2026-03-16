from yardland import Yardland

class Inventario:
    def __init__(self, fazenda_instancia):
        self.fazenda = fazenda_instancia # Agora o inventário tem acesso à Yardland
        self.inventario = {}
        self.capacidade_carga = 20

    def _transferir_para_inventario(self):
        # Acessamos os recursos através da instância da fazenda
        itens_disponiveis = [k for k, v in self.fazenda.recursos.items() if isinstance(v, (int, float))]
        
        for i, item in enumerate(itens_disponiveis, 1):
            print(f"{i}. {item.title()} (Estoque: {self.fazenda.recursos[item]})")
        
        try:
            idx = int(input("Escolha o item: ")) - 1
            qtd = int(input("Quantidade: "))
            item_nome = itens_disponiveis[idx]
            
            espaco_livre = self.capacidade_carga - sum(self.inventario.values())
            
            if qtd <= self.fazenda.recursos[item_nome] and qtd <= espaco_livre:
                # Modifica o estoque da fazenda e o inventário pessoal
                self.fazenda.recursos[item_nome] -= qtd
                self.inventario[item_nome] = self.inventario.get(item_nome, 0) + qtd
                print(f"\n{qtd} {item_nome.title()} colocados na sacola.")
            else:
                print("\nErro: Estoque insuficiente ou sacola cheia!")
        except (ValueError, IndexError):
            print("\nEntrada inválida.")

    def _transferir_para_yardland(self):
        if not self.inventario:
            print("\nSua sacola está vazia.")
            return

        itens_na_sacola = list(self.inventario.keys())
        for i, item in enumerate(itens_na_sacola, 1):
            print(f"{i}. {item.title()} (Na sacola: {self.inventario[item]})")

        try:
            idx = int(input("Escolha o item para guardar: ")) - 1
            qtd = int(input("Quantidade: "))
            item_nome = itens_na_sacola[idx]

            if qtd <= self.inventario[item_nome]:
                self.inventario[item_nome] -= qtd
                self.fazenda.recursos[item_nome] += qtd
                
                # Limpa a chave se chegar a zero
                if self.inventario[item_nome] == 0:
                    del self.inventario[item_nome]
                print(f"\n{qtd} {item_nome.title()} guardados na Yardland.")
            else:
                print("\nErro: Você não tem essa quantidade na sacola.")
        except (ValueError, IndexError):
            print("\nEntrada inválida.")

inventario = Inventario(fazenda_instancia=Yardland())
inventario._transferir_para_inventario()
inventario._transferir_para_yardland()