from random import randint, choice
from time import sleep


def iniciar():
    global pc, jogador
    print("Partida iniciada.")
    sleep(0.5)
    dar_carta("pc")
    sleep(0.5)
    dar_carta("jogador")
    sleep(2)


def quem_joga():
    global turno, quemcomeca, encerrar_jogo
    if quemcomeca == "pc":
        if turno % 2 != 0:
            jogada_pc()
        else:
            print("Sua vez.")
            pegar_carta = input("Pegar carta: s/n? ").lower()
            if pegar_carta == "s":
                dar_carta("jogador")
            else:
                encerrar_jogo = True
    else:
        if turno % 2 != 0:
            print("Sua vez.")
            pegar_carta = input("Pegar carta: s/n? ").lower()
            if pegar_carta == "s":
                dar_carta("jogador")
            else:
                encerrar_jogo = True
        else:
            jogada_pc()


def verificar():
    global parar_jogo
    if sum(pc) > 21:
        print("A soma das cartas do computador\n"
              "passaram de 21.\n"
              "O Jogador Venceu!")
        parar_jogo = True
    elif sum(jogador) > 21:
        print("A soma das cartas do jogador\n"
              "passaram de 21.\n"
              "O Computador Venceu!")
        parar_jogo = True
    else:
        pass


def jogada_pc():
    global pc, cartas_pc, parar_jogo, encerrar_jogo
    for c in cartas_pc:
        if not sum(pc) + c <= 21:
            encerrar_jogo = True
    dar_carta("pc")


def dar_carta(quem):
    global turno
    carta = choice(cartas)
    cartas.remove(carta)
    if quem == "pc":
        pc.append(carta)
        cartas_pc.remove(carta)
        if turno == 0:
            print(f"O computador pegou uma carta.")
            print(f"O computador pegou a carta {carta}.")
    else:
        jogador.append(carta)
        print(f"Você pegou a carta {carta}")


parar_jogo = False
encerrar_jogo = False
BARALHO = (11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10)
cartas = []
cartas_pc = []
for c in BARALHO:
    cartas.append(c)
    cartas_pc.append(c)
pc = []
jogador = []
turno = 0
turno_final = 0

iniciar()
quemcomeca = randint(0, 1)
if quemcomeca == 0:
    quemcomeca = "pc"
    print("Computador começa.\n")
else:
    quemcomeca = "jogador"
    print("Jogador começa.\n")

while not parar_jogo:
    turno += 1
    print("=" * 32)
    print(f"Turno: {turno}\n"
          f"Suas cartas: ", end="")
    if len(jogador) > 1:
        for c in jogador:
            print(f"{c}", end="")
        print()
    else:
        print(jogador[0])
    print(f"Cartas do Computador: ", end="")
    if len(pc) > 1:
        for c in pc:
            print(f"{c}", end="")
        print()
    else:
        print(pc[0])
    print(f"Soma: {sum(jogador)}")
    print("=" * 32)
    quem_joga()

    verificar()

    if encerrar_jogo:
        if turno != turno_final:
            turno_final = turno + 1
        else:
            print(f"Jogador: {sum(jogador)}\n"
                  f"Computador: {sum(pc)}\n")
            if sum(pc) < sum(jogador):
                print("O Jogador obteve o resultado\n"
                      "mais próximo de 21.\n"
                      "O Jogador Venceu!")
            elif sum(jogador) < sum(pc):
                print("O Computador obteve o resultado\n"
                      "mais próximo de 21.\n"
                      "O Computador Venceu!")
            parar_jogo = True

