from datetime import datetime, timedelta

class DataBr:
    def __init__(self):
        self.momento = datetime.today()

    def __str__(self):
        return self.format()

    def mes_cadastro(self):
        meses_do_ano = [
            "janeiro", "fevereiro", "março",
            "abril", "maio", "junho", "julho",
            "agosto", "setembro", "outubro",
            "novembro", "dezembro"
        ]
        mes_cadastro = self.momento.month - 1
        return meses_do_ano[mes_cadastro]
    
    def dia_da_semana(self):
        dias_lista = ["segunda", "terça", "quarta", "quinta", "sexta", "sabado", "domingo"]
        dia = self.momento.weekday()
        return dias_lista[dia]

    def format(self):
        data_formatada = self.momento.strftime("%d/%m/%Y %H:%M")
        return data_formatada

    def tempo_cadastro(self):
        tempo = (datetime.today() + timedelta(days=30)) - self.momento
        return tempo