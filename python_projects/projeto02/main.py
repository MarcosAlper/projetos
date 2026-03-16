from random import randint, choice
from time import sleep

"""
1. Grupo de pessoas com gênero e idade aleatórios.
"""

listaNomes = {
    "masculino": ["João", "Pedro", "Lucas", "Mateus",
                  "Rafael", "Gustavo", "Thiago", "Bruno",
                  "Felipe", "André", "Carlos", "Eduardo",
                  "Ricardo", "Vinícius", "Gabriel", "Leonardo"],
    "feminino": ["Maria", "Ana", "Juliana", "Fernanda",
                "Carla", "Sofia", "Isabela", "Camila",
                "Larissa", "Beatriz", "Mariana", "Gabriela",
                "Letícia", "Amanda", "Natália", "Vitória"]
}

"""class Tempo:
    def __init__(self):
        self.dia = 1
        self.ano = 0
        self.data = [self.dia, self.mes, self.ano]
        self.hora = 0
        self.minuto = 0
        self.tempoCorrendo = False
    
    class Mes:
        def __init__(self):
            self.meses = ["janeiro", "fevereiro", "março", "abril",
                          "maio", "junho", "julho", "agosto",
                          "setembro", "outubro", "novembro", "dezembro"]

    def correrTempo(self):
        self.tempoCorrendo = True
        while self.tempoCorrendo:
            time.sleep(1)
            self.minuto += 1
            if self.minuto == 60:
                self.minuto = 0
                self.hora += 1
            if self.hora == 24:
                self.hora = 0
                self.dia += 1
"""

class Calendario:
    MESES = ["janeiro", "fevereiro", "março", "abril", "maio", "junho",
             "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
    DIAS_MES = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(self, dia=1, mes=1, ano=0):
        self.dia = dia
        self.mes = mes  # 1 a 12
        self.ano = ano

    def bissexto(self, ano=None):
        if ano is None:
            ano = self.ano
        return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

    def dias_no_mes(self, mes=None, ano=None):
        if mes is None:
            mes = self.mes
        if ano is None:
            ano = self.ano
        if mes == 2:
            return 29 if self.bissexto(ano) else 28
        return self.DIAS_MES[mes-1]

    def avancar_dia(self, n=1):
        for _ in range(n):
            self.dia += 1
            if self.dia > self.dias_no_mes():
                self.dia = 1
                self.mes += 1
                if self.mes > 12:
                    self.mes = 1
                    self.ano += 1

    def retroceder_dia(self, n=1):
        for _ in range(n):
            self.dia -= 1
            if self.dia < 1:
                self.mes -= 1
                if self.mes < 1:
                    self.mes = 12
                    self.ano -= 1
                self.dia = self.dias_no_mes(self.mes, self.ano)

class GrupoPessoas:
    class Primordial:
        def __init__(self):
            self.idade = randint(17, 24)
            self.nascimento = [tempo.retroceder_dia((365 * self.idade) + (self.idade // 4) - (self.idade // 100) + (self.idade // 400))]
            self.aniversario = [self.nascimento[0], self.nascimento[1]]
            self.genero = choice(["masculino", "feminino"])
            if self.genero == "masculino":
                self.nome = choice(listaNomes["masculino"])
            else:
                self.nome = choice(listaNomes["feminino"])

tempo = Calendario()
pessoa = GrupoPessoas.Primordial()
print(f"Nome: {pessoa.nome}\n"
      f"Gênero: {pessoa.genero}\n"
      f"Idade: {pessoa.idade}\n"
      f"Nascimento: {pessoa.nascimento[0]:02d}/{pessoa.nascimento[1]:02d}/{pessoa.nascimento[2]:04d}\n"
      f"Aniversário: {pessoa.aniversario[0]:02d}/{pessoa.aniversario[1]:02d}")
