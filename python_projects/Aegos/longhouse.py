class yardland():
    def __init__(self, ceorl=str):
        self.ceorl = f"Ceorl {ceorl.title()}" # Nome do Ceorl, detentor do yardland
        self.moradores = [self.ceorl] # Lista de moradores do yardland, iniciando com o ceorl
        self.longhouse = {
            "bois": {"atual": 1, "limite": 2},
            "vacas": {"atual": 2, "limite": 4},
            "despensa": {"atual": 2, "limite": 4},
            "ovelhas": {"atual": 5, "limite": 10},
            "galinhas": {"atual": 4, "limite": 6},
            "carne_salgada": {"atual": 3, "limite": 8},
            "forragem": {"atual": 6, "limite": 12},
            "arado_ard": {"atual": 1, "limite": 2},
            "arado_pesado": {"atual": 0, "limite":1},
            "nvl_atual": {"atual": 1, "limite": 3} # Representa o número de ampliações feitas
        }
        self.celeiro_elevado = {
            "espaco": {"atual": 0, "limite": 0},
            "graos": 0,
            "sementes": 0,
            "la": 0,
            "linho": 0,
            "nvl_atual": {"atual": 0, "limite": 2}
        }
        self.despensa = {
            "espaco": {"atual": 2, "limite": 4},
            "ovos": 1,
            "queijo": 1,
            "leite": 0,
            "nvl_atual": {"atual": 1, "limite": 3}
        }
        self.estruturas = {
            "longhouseNvl2": {
                "construido": False,
                "requisitos": {"madeira": 50, "palha": 20, "trabalhadores": 3},
                "limite_bois": 4,
                "limite_vacas": 6,
                "limite_despensa": 12,
                "limite_ovelhas": 15,
                "limite_galinhas": 10,
                "limite_carne_salgada": 16,
                "limite_forragem": 25,
                },
            "longhouseNvl3": {
                "construido": False,
                "requisitos": {"hide": 1, "madeira": 200, "pedras": 50, "construtores": True},
                "limite_bois": 12,
                "limite_vacas": 20,
                "limite_despensa": 25,
                "limite_ovelhas": 50,
                "limite_galinhas": 30,
                "limite_carne_salgada": 30,
                "limite_forragem": 40,
                },
            "hyrdel": {
                "construido": False,
                "requisitos": {"madeira": 80, "palha": 40, "trabalhadores": 10, "ferramentas_carpintaria": True},
                "limite_bois": 6,
                "limite_vacas": 10,
                "limite_ovelhas": 25,
                "limite_galinhas": 15,
                "limite_forragem": 20,
                },
            "celeiro_elevadoNvl1": {
                "construido": False,
                "requisitos": {"madeira": 40, "palha": 4, "trabalhadores": 4},
                "espaco": 30, # 1 saca tem valor 1, 1 lã tem valor 1
                },
            "celeiro_elevadoNvl2": {
                "construido": False,
                "requisitos": {"madeira": 80, "palha": 8, "trabalhadores": 8, "ferramentas_carpintaria": True},
                "espaco": 80, # 1 saca tem valor 1, 1 lã tem valor 1
                },
            "eira": {
                "construido": False,
                "requisitos": {"madeira": 0, "palha": 0, "trabalhadores": 0, "ferramentas_carpintaria": True},
                },
        }        
        self.recursos = {
            "madeira": 200,
            "pedras": 100,
            "ferramentas_carpintaria": False,
            "trabalhadores": len(self.moradores),
            "construtores": False,
        }
        self.criacoes = {
            "arado ard": {
                "requisitos": {
                    "madeira": 15, 
                    "trabalhadores": 1
                },
                "efeitos": -0.25
            },
            "arado pesado": {
                "requisitos": {
                    "madeira": 40, 
                    "ferro": 5,
                    "trabalhadores": 3,
                    "ferramentas_carpintaria": True
                }
            }
        }
        self.campo = {
            "status": "bruto", # Pode ser: bruto, arado, semeado, pronto_para_colher
            "fertilidade": 100,
            "area_total": 10 # Tamanho em yardlands/acres
        }

    def painelGeral(self):
        linha('=', 60)
        print("Yardland")
        linha('-', 60)
        print(f"Propriedade de {self.ceorl}")
        print(f"Moradores: ", end='')
        for morador in self.moradores:
            if len(self.moradores) - 1 == self.moradores.index(morador):
                print(f"{morador}")
            else:
                print(f"{morador}, ", end='')
        linha('-', 60)
        lista_opcoes = ["Trabalhos", "Construções", "Vizinhos", "Criações", "Longhouse", "Sair do Yardland"]
        if self.estruturas["celeiro_elevadoNvl1"]["construido"]:
            lista_opcoes.insert(5, f"Celeiro Elevado Nvl {self.celeiro_elevado['nvl_atual']['atual']}")
        else:
            lista_opcoes.insert(5, f"{'-- Construir --'.center(21)}")
        if self.estruturas["eira"]["construido"]:
            lista_opcoes.insert(6, f"{'Eira'.center(21)}")
        else:
            lista_opcoes.insert(6, f"{'-- Construir --'.center(21)}")
        if self.estruturas["hyrdel"]["construido"]:
            lista_opcoes.insert(7, f"{'Hyrdel'.center(21)}")
        else:
            lista_opcoes.insert(7, f"{'-- Construir --'.center(21)}")
        for opcao in range((len(lista_opcoes) - 1)//2):
            string1 = f"{str(opcao + 1)}. {lista_opcoes[opcao]}"
            string2 = f"{str(opcao + 5)}. {lista_opcoes[opcao + 4]}"
            print(f"{f'{string1.center(30)}{string2.center(30)}'.center(60)}")
        print(f"{(str(len(lista_opcoes)) + '. ' + lista_opcoes[-1]).center(60)}")
        linha('=', 60)
        while True:
            escolha = input("    >>> ")
            if escolha in ["1", "2", "3", "4", "5", "9"]:
                break
            elif escolha == "6" and not self.estruturas["celeiro_elevadoNvl1"]["construido"]:
                print("Você não possui um celeiro elevado.\n")
                continue
            elif escolha == "7" and not self.estruturas["eira"]["construido"]:
                print("Você não possui uma eira.\n")
                continue
            elif escolha == "8" and not self.estruturas["hyrdel"]["construido"]:
                print("Você não possui um hyrdel.\n")
                continue
            break
        linha('=', 60)
        print()
        return escolha

    def painelTrabalho(self):
        linha('=', 60)
        print("Trabalhos")
        linha('-', 60)
        lista_trabalhos = ["1. Arar", "2. Semear", "3. Colher", "4. Malhar Grãos",
                           "5. Pastorear", "6. Coletar Lã","7. Ordenhar Vacas",
                           "8. Produzir Queijo", "9. Abater Animal", "10. Forrar Animais"]
        for trabalho in range(len(lista_trabalhos)//2):
            print(f"{f'{lista_trabalhos[trabalho].center(30)}{lista_trabalhos[trabalho + 5].center(30)}'.center(60)}")
        linha('=', 60)
        while True:
            escolha = input("    >>> ")
            if escolha in [str(i) for i in range(1, 10)]:
                break
        linha('=', 60)
        print()
        return escolha
        
    def construcoes(self):
        linha('=', 60)
        print("Construir Estrutura")
        linha('-', 60)
        if self.longhouse['nvl_atual']['atual'] < self.longhouse['nvl_atual']['limite']:
            requisitos = self.estruturas[f"longhouseNvl{self.longhouse['nvl_atual']['atual'] + 1}"]["requisitos"]
            print(f"1. Longhouse Nível {self.longhouse['nvl_atual']['atual'] + 1} | Requisitos: ", end='')
            for chave, valor in requisitos.items():
                print(f"{valor} {chave.replace('_', ' ').title()}", end=', ' if list(requisitos.keys())[-1] != chave else '\n')
        else:
            print("1. Longhouse Nível Máximo Alcançado")
        if self.celeiro_elevado['nvl_atual']['atual'] < self.celeiro_elevado['nvl_atual']['limite']:
            requisitos = self.estruturas[f"celeiro_elevadoNvl{self.celeiro_elevado['nvl_atual']['atual'] + 1}"]["requisitos"]
            print(f"2. Celeiro Elevado Nível {self.celeiro_elevado['nvl_atual']['atual'] + 1} | Requisitos: ", end='')
            for chave, valor in requisitos.items():
                print(f"{valor} {chave.replace('_', ' ').title()}", end=', ' if list(requisitos.keys())[-1] != chave else '\n')
        else:
            print("2. Celeiro Elevado Nível Máximo Alcançado")
        if not self.estruturas["eira"]["construido"]:
            requisitos = self.estruturas["eira"]["requisitos"]
            print(f"3. Eira | Requisitos: ", end='')
            for chave, valor in requisitos.items():
                print(f"{valor} {chave.replace('_', ' ').title()}", end=', ' if list(requisitos.keys())[-1] != chave else '\n')
        else:
            print("3. Eira Já Construída")
        if not self.estruturas["hyrdel"]["construido"]:
            requisitos = self.estruturas["hyrdel"]["requisitos"]
            print(f"4. Hyrdel | Requisitos: ", end='')
            for chave, valor in requisitos.items():
                print(f"{valor} {chave.replace('_', ' ').title()}", end=', ' if list(requisitos.keys())[-1] != chave else '\n')
        else:
            print("4. Hyrdel Já Construído")
        print('["0" para voltar]')
        linha('=', 60)
        while True:
            escolha = input("    >>> ")
            if escolha == "1":
                self.comprar(self.estruturas[f"longhouseNvl{self.longhouse['nvl_atual']['atual'] + 1}"])
            if escolha == "2":
                self.comprar(self.estruturas[f"celeiro_elevadoNvl{self.celeiro_elevado['nvl_atual']['atual'] + 1}"])
            if escolha == "3":
                self.comprar(self.estruturas["eira"])
            if escolha == "4":
                self.comprar(self.estruturas["hyrdel"])
            if escolha == "0":
                break
        linha('=', 60)
        print()
        return escolha
    
    def admLonghouse(self):
        while True:
            linha('=', 60)
            print("ADMINISTRAÇÃO DA LONGHOUSE")
            linha('-', 60)
            
            # Criamos uma lista de chaves para acessar por índice
            lista_recursos = [k for k in self.longhouse.keys() if k != "nvl_atual"]
            
            for i, recurso in enumerate(lista_recursos, 1):
                dados = self.longhouse[recurso]
                print(f"{i}. {recurso.replace('_', ' ').title():<15}: {dados['atual']}/{dados['limite']}")
            
            linha('-', 60)
            print('["0" para voltar]')
            opcao = input("Selecione um recurso para remover/abater: ")
            
            if opcao == "0":
                break
                
            if opcao.isdigit() and 1 <= int(opcao) <= len(lista_recursos):
                chave_selecionada = lista_recursos[int(opcao) - 1]
                
                try:
                    qtd = int(input(f"Quantidade de '{chave_selecionada}' para remover: "))
                    
                    if 0 < qtd <= self.longhouse[chave_selecionada]['atual']:
                        self.longhouse[chave_selecionada]['atual'] -= qtd
                        print(f"\nSucesso: {qtd} removido(s).")
                    else:
                        print("\nErro: Quantidade inválida ou estoque insuficiente.")
                except ValueError:
                    print("\nErro: Digite um número inteiro.")
            else:
                print("\nOpção inválida.")

    def comprar(self, estrutura: dict):
        requisitos = estrutura["requisitos"]
        
        # 1. VERIFICAÇÃO
        for item, valor_necessario in requisitos.items():
            if item not in self.recursos:
                continue # Pula se o requisito não estiver no estoque global
                
            estoque_atual = self.recursos[item]
            
            if isinstance(valor_necessario, bool):
                if estoque_atual == False: # Jogador não tem a ferramenta/condição
                    print(f"\nFalta pré-requisito: {item.replace('_', ' ').title()}!\n")
                    return
            else:
                if estoque_atual < valor_necessario:
                    print(f"\nRecurso insuficiente: {item.replace('_', ' ').title()}!\n")
                    return

        # 2. CONSUMO (Subtrai dos recursos do Ceorl)
        for item, valor_necessario in requisitos.items():
            if item in self.recursos and not isinstance(self.recursos[item], bool):
                self.recursos[item] -= valor_necessario

        # 3. FINALIZAÇÃO E UPGRADE DE LIMITES
        estrutura["construido"] = True
        
        if "limite_despensa" in estrutura: # É uma Longhouse
            self.longhouse['nvl_atual']['atual'] += 1
            # Atualiza os limites reais da longhouse com os novos valores da estrutura
            for chave in self.longhouse:
                limite_key = f"limite_{chave}"
                if limite_key in estrutura:
                    self.longhouse[chave]["limite"] = estrutura[limite_key]
            print(f"\nLonghouse ampliada para o Nível {self.longhouse['nvl_atual']['atual']}!")
            
        elif "espaco" in estrutura and "requisitos" in estrutura: # É um Celeiro
            self.celeiro_elevado['nvl_atual']['atual'] += 1
            self.celeiro_elevado['espaco']['limite'] = estrutura['espaco']
            print(f"\nCeleiro ampliado para o Nível {self.celeiro_elevado['nvl_atual']['atual']}!")

        print("Obra concluída com sucesso!\n")

    def arar(self):
        # 1. Verificações iniciais de estado
        if self.campo["status"] != "bruto":
            print(f"A terra já está {self.campo['status']}. Não há necessidade de arar agora.")
            return

        tem_ard = self.longhouse["arado_ard"]["atual"] > 0
        tem_pesado = self.longhouse["arado_pesado"]["atual"] > 0
        bois_atuais = self.longhouse["bois"]["atual"]

        if not tem_ard and not tem_pesado:
            print("Erro: Você não possui nenhum arado no Yardland.")
            return

        # 2. Menu de Seleção de Arado
        linha("=", 60)
        print("PREPARAÇÃO DA TERRA".center(60))
        linha("-", 60)
        
        opcoes_validas = []
        if tem_ard:
            print(f"1. Arado Ard (Requer 2 bois) | Disponível")
            opcoes_validas.append("1")
        
        if tem_pesado:
            status_pesado = "Disponível" if bois_atuais >= 8 else f"Faltam {8 - bois_atuais} bois"
            print(f"2. Arado Pesado (Requer 8 bois) | {status_pesado}")
            if bois_atuais >= 8:
                opcoes_validas.append("2")

        print("0. Cancelar")
        
        while True:
            escolha = input("\nEscolha o equipamento para o trabalho >>> ")
            if escolha == "0": return
            if escolha in opcoes_validas:
                break
            print("Escolha inválida ou você não possui os requisitos necessários.")

        # 3. Definição de custos e efeitos baseado na escolha
        if escolha == "1":
            custo_forragem = 4 # Ard exige mais esforço/tempo
            bonus_produtividade = self.criacoes["arado ard"]["efeitos"]
            ferramenta = "Arado Ard"
        else:
            custo_forragem = 2 # Mais eficiente
            bonus_produtividade = 0.2 # Bônus positivo para o pesado
            ferramenta = "Arado Pesado"

        # 4. Execução final
        if self.longhouse["forragem"]["atual"] >= custo_forragem:
            self.longhouse["forragem"]["atual"] -= custo_forragem
            self.campo["status"] = "arado"
            print(f"\nSucesso: O campo foi trabalhado com o {ferramenta}!")
            print(f"Os bois consumiram {custo_forragem} de forragem. Solo pronto para semear.")
        else:
            print("\nErro: Seus bois estão fracos demais. Você precisa de mais forragem.")
          
    def semear(self):
        pass

    def colher(self):
        pass

    def malharGrãos(self):
        pass

    def pastorear(self):
        pass

    def coletarLã(self):
        pass

    def ordenharVacas(self):
        pass

    def produzirQueijo(self):
        pass

    def abaterAnimal(self):
        pass

    def forrar(self): # Automática e dependente de haver forragem para cada animal
        pass

fazenda = yardland(ceorl="markos alper")
while True:
    escolha = fazenda.painelGeral()
    if escolha == "1":
        escolha = fazenda.painelTrabalho()
        if escolha == "1":
            fazenda.arar()
        elif escolha == "2":
            fazenda.semear()
        elif escolha == "3":
            fazenda.colher()
        elif escolha == "4":
            fazenda.malharGrãos()
        elif escolha == "5":
            fazenda.pastorear()
        elif escolha == "6":
            fazenda.coletarLã()
        elif escolha == "7":
            fazenda.ordenharVacas()
        elif escolha == "8":
            fazenda.produzirQueijo()
        elif escolha == "9":
            fazenda.abaterAnimal()
        elif escolha == "10":
            fazenda.forrar()
    elif escolha == "2":
        escolha = fazenda.construcoes()
        if escolha == "1":
            pass
    elif escolha == "3":
        escolha = fazenda.vizinhos()
        if escolha == "1":
            pass
    elif escolha == "4":
        escolha = fazenda.criacoes()
        if escolha == "1":
            pass
    elif escolha == "5":
        fazenda.admLonghouse()
    elif escolha == "6":
        fazenda.admCeleiroElevado()
    elif escolha == "7":
        fazenda.admEira()
    elif escolha == "8":
        fazenda.admHyrdel()
    elif escolha == "9":
        pass
