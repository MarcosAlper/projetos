from mundo import *

class Interface():
    def __init__(self, local_id):
        self.local_id = local_id
        self.opcoes = []
        self.cabecalho()
    
    def linha(self, simbolo='-', tamanho=20):
        print(simbolo * tamanho)

    def cabecalho(self):
        self.linha("=")
        local_obj = mapa.nodes[self.local_id]['dados']
        print(f"{local_obj.nome_exibicao} ({self.local_id}), Ano 1")
        self.linha("=")

    def exibir_menu(self):
        for index, opcao in enumerate(self.opcoes):
            if opcao != "sair e salvar":
                print(f"   {index + 1}. {opcao.capitalize()}")
            else:
                print(f"   0. {opcao.capitalize()}")
        self.linha("=")
    
    def verificar_escolha(self):
        while True:
            escolha = input("   >>> ")
            if escolha.isnumeric():
                escolha = int(escolha)
                if escolha < 0 or escolha > (len(self.opcoes) - 1):
                    print("Escolha inválida.")
                else:
                    self.linha("=")
                    print("\n")
                    return escolha
            else:
                print("Escolha inválida.")

class InterfaceCampones(Interface):
    def __init__(self, local_id):
        super().__init__(local_id)
        self.opcoes = [
            "longhouse", # Lugar de administração
            "trabalhos", # Lista de trabalhos disponíveis
            "social", # Pessoas conhecidas e nível socialização
            "mapa", # Mostra lugares imediatos e macro
            "sair e salvar"
        ]
        
        self.exibir_menu()
        escolha = self.verificar_escolha()
        if escolha == 1:
            pass # Chama o menu da Longhouse (Recursos, Família, Construção)
        elif escolha == 2:
            pass # Chama o menu de Trabalhos (Nesse caso, trabalhos de camponês e homem livre)
        elif escolha == 3:
            pass # Chama o menu Social (Lista de todas as pessoas conhecidas e nível de vínculo)
        elif escolha == 4:
            pass # Chama o menu do Mapa (Lista de lugares acessíveis, ajdacentes ao lugar atual)
        elif escolha == 0:
            pass # Sai do jogo e salva

class InterfaceDonoDeTerra(Interface):
    def __init__(self, local_id):
        super().__init__(local_id)
        self.opcoes = []

class InterfaceSenhor(Interface):
    def __init__(self, local_id):
        super().__init__(local_id)
        self.opcoes = []

interface = InterfaceCampones("X")
