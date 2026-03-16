class Calendario:
    MESES = ["janeiro", "fevereiro", "março", "abril", "maio", "junho",
             "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
    DIAS_MES = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(self, dia=1, mes=1, ano=0):
        if not (1 <= mes <= 12):
            raise ValueError("Mês deve estar entre 1 e 12.")
        if not (1 <= dia <= self.dias_no_mes(mes, ano)):
            raise ValueError(f"Dia inválido para o mês {mes} e ano {ano}.\n"
                             f"Use dias entre 1 e {self.dias_no_mes(mes, ano)}.")
        if ano < 0:
            raise ValueError("Ano deve ser maior ou igual a 0.")
        self.dia = dia
        self.mes = mes
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
    
    def hoje(self):
        return f"{self.dia:02d}/{self.mes:02d}/{self.ano:04d}"

    def avancar_tempo(self, d=0, m=0, a=0):
        self.ano += a
        self.mes += m
        while self.mes > 12:
            self.mes -= 12
            self.ano += 1
        
        self.dia += d
        while self.dia > self.dias_no_mes():
            self.dia -= self.dias_no_mes()
            self.mes += 1
            if self.mes > 12:
                self.mes = 1
                self.ano += 1

    def retroceder_tempo(self, d=1, m=0, a=0):
        self.ano -= a
        self.mes -= m
        while self.mes < 1:
            self.mes += 12
            self.ano -= 1

        self.dia -= d
        while self.dia < 1:
            self.mes -= 1
            if self.mes < 1:
                self.mes = 12
                self.ano -= 1
            self.dia += self.dias_no_mes(self.mes, self.ano)
            
    def ir_para_data(self, dia, mes, ano):
        if not (1 <= mes <= 12):
            raise ValueError("Mês deve estar entre 1 e 12.")
        if not (1 <= dia <= self.dias_no_mes(mes, ano)):
            raise ValueError(f"Dia inválido para o mês {mes} e ano {ano}.\n"
                                f"Use dias entre 1 e {self.dias_no_mes(mes, ano)}.")
        if ano < 0:
            raise ValueError("Ano deve ser maior ou igual a 0.")
        self.dia = dia
        self.mes = mes
        self.ano = ano
