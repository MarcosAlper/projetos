from soldados import *

def painelExercito():
    linha('=', 60)
    print("Painel do Exército")
    linha('-', 60)
    print(f"Moedas: {moedas} ({lucroMensal - gastosMensais})")
    print(f"Soldados: {numSoldados}")
    print(f"Milicianos: {len(milicianos)}")
    print(f"Espadachins: {len(espadachins)}")
    print(f"Dano Total: {danoTotal}")
    linha('-', 60)
    print("1. Contratar Soldados")
    linha('=', 60)
    escolha = input("    >>> ")
    linha('=', 60)
    print()
    return escolha

def contratarSoldados():
    while True:
        linha('=', 60)
        print("Soldados Disponíveis:")
        linha('-', 60)
        print("1. Miliciano | 1 Dano | 1 Moeda\n"
              "2. Espadachim | 5 Dano | 5 Moedas\n"
              '["0" para voltar]')
        linha('=', 60)
        escolha = int(input("    >>> "))
        linha('=', 60)
        print()
        if escolha == 0:
            break
        while True:
            if escolha == 1:
                linha('=', 60)
                print("Quantos Milicianos deseja contratar?\n"
                      '["0" para voltar]')
                linha('=', 60)
                quantidade = int(input("    >>> "))
                linha('=', 60)
                print()
                if quantidade == 0:
                    break
                elif quantidade < 0:
                    print("Quantidade inválida.\n")
                    continue
                else:
                    for miliciano_ in range(quantidade):
                        milicianos.append(Miliciano())
                    print(f"{quantidade} Miliciano(s) contratado(s) com sucesso!\n")
                    return 0
            elif escolha == 2:
                linha('=', 60)
                print("Quantos Milicianos deseja contratar?\n"
                      '["0" para voltar]')
                linha('=', 60)
                quantidade = int(input("    >>> "))
                linha('=', 60)
                print()
                if quantidade == 0:
                    break
                elif quantidade < 0:
                    print("Quantidade inválida.\n")
                    continue
                else:
                    for espadachim_ in range(quantidade):
                        espadachins.append(Espadachim())
                    print(f"{quantidade} Espadachim(ns) contratado(s) com sucesso!\n")
                    return 0

lucroMensal = 0
gastosMensais = 0
moedas = 100
milicianos = []
espadachins = []
numSoldados = 0
danoTotal = 0

while True:
    escolha = painelExercito()
    if escolha == '1':
        contratarSoldados()
        numSoldados = len(milicianos) + len(espadachins)
        gastosMensais = sum([soldado.soldo for soldado in milicianos + espadachins])
        danoTotal = sum([soldado.dano for soldado in milicianos + espadachins])
