#from CpfCnpj import Documento
#import re
#from TelefoneBr import TelefoneBr
#cpf = 15616987913
#tamanho_cpf = len(cpf)
#
# 
# 
#  
from acesso_cep import EnderecoCep
#import requests

cep = '01001000' #""
objeto_cep = EnderecoCep(cep)
bairro, cidade, uf = objeto_cep.acessando_cep()
print(bairro, cidade, uf)

'''
from datas import DataBr
from datetime import datetime
cadastro = DataBr()
print(cadastro.dia_da_semana())
print(cadastro)

print(cadastro.tempo_cadastro())


hoje = datetime.today()
hoje_formatado = hoje.strftime("%d/%m/%Y %H:%M")
print(hoje_formatado)


numero = "5519993963014"
telefone = TelefoneBr(numero)

telefone.format()


meu_cpf = CpfCnpj(38410282844)
print(meu_cpf)'''


'''meu_cnpj = CNPJ()

print(meu_cnpj.validate('00360305000104'))'''
'''
cnpj = '00360305000104' 
cpf = "38410282844"
documento = Documento.cria_documento(cpf)
print(documento)
meu_documento = cpf
meu_cnpj = CpfCnpj(meu_documento, 'cpf')
print(meu_cnpj)

padrao = "[0-9][a-z]{2}[0-9]"

texto = "123 1cc 3th1 0a0"

resposta = re.search(padrao, texto)
print(resposta.group())

pd = "\w{5,50}@\w{5,10}.\w{2,3}.\w{2,3}"

texto1 = "aaaaaabbbccccc rodrigo123@gmail.com.br ajjdfdfjdjsjfkdjfj"

resposta1 = re.search(pd, texto1)
print(resposta1.group())

pdo = "[0-9]{2} [0-9]{4,5} [0-9]{4}"

texto2 = "Eu gosto do numero 19 3233 8878 e também do 19 99396 3014"

resposta2 = re.findall(pdo, texto2)

print(resposta2)

'''