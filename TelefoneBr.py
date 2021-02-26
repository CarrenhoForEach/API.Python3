import re

class TelefoneBr:

    def __init__(self, numero):
        if self.valida_telefone(numero):
            self.telefone = numero
        else:
            raise ValueError("Telefone não encontrado!!!")

    def valida_telefone(self, numero):
        padrao = "([0-9]{2})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.findall(padrao, numero)
        if resposta:
            return True
        else:
            return False
    
    def format(self):
        padrao = "([0-9]{2})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.search(padrao, self.telefone)
        numero_formatado = "+{} ({}) {}-{}".format(
            resposta.group(1), resposta.group(2), resposta.group(3), resposta.group(4)
        )
        print(numero_formatado)