jogador1 = "X"
jogador2 = "O"
lugares = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
turn = 1

def desenharJogoDaVelha():
    print(
    f" {lugares[0]} | {lugares[1]} | {lugares[2]}\n"
    "---+---+---\n" \
    f" {lugares[3]} | {lugares[4]} | {lugares[5]}\n"
    "---+---+---\n" \
    f" {lugares[6]} | {lugares[7]} | {lugares[8]}\n"
    )

def mudar(valor, lugar):
    lugares[int(lugar) - 1] = valor

while True:
    desenharJogoDaVelha()
    if (turn % 2 == 1):
        lugar = input("Jogador 1 escolhe o lugar: ")
        if lugar.isnumeric():
            if int(lugar) > 0 and int(lugar) < 10:
                mudar("X", lugar)
                turn += 1
            else:
                print("Lugar inválido.")
        else:
            print("Digite um número.")
    else:
        lugar = input("Jogador 2 escolhe o lugar: ")
        if lugar.isnumeric():
            if int(lugar) > 0 and int(lugar) < 10:
                mudar("O", lugar)
                turn += 1
            else:
                print("Lugar inválido.")
        else:
            print("Digite um número.")

