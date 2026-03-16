from random import randint, choice

largura_tela = 11

pessoas = []
for c in range(0, 10):
    genero = ""
    genero_s = randint(0, 1)
    if genero_s == 0:
        genero = "homem"
    else:
        genero = "mulher"
    idade = randint(17, 24)

    pessoa = [genero, idade]
    pessoas.append(pessoa)
homens = 0
mulheres = 0
for c in pessoas:
    if c[0] == "homem":
        homens += 1
    elif c[0] == "mulher":
        mulheres += 1

mundo = {
    "floresta": ["galhos", "pedras", "folhas", "frutas", "animais", "árvores"],
    "rio": ["água", "pedras", "peixes"]
}
recursos_floresta = ["galhos", "pedras", "folhas", "frutas", "animais", "árvores"]
recursos_rio = ["água", "pedras", "peixes"]
lugar = ""

keys = []
for k in mundo.keys():
    keys.append(k)
print(keys, choice(keys))

print(f"{'='*largura_tela}\n"
      f"Local: {lugar}\n"
      f"Recursos: \n"
      f"{'-'*largura_tela}\n"
      f"Homens: {homens}\n"
      f"Mulheres: {mulheres}\n"
      f"{'='*largura_tela}")


input(">>> ")


