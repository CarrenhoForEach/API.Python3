import requests

class EnderecoCep:

    def __init__(self, cep):
        cep = str(cep)
        if self.valido_cep(cep):
            self.cep = cep
        else:
            raise ValueError("Cep inválido!")

    def __str__(self):
        return self.format()

    def valido_cep(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def format(self):
        return "{}-{}".format(self.cep[:5], self.cep[5:])

    def acessando_cep(self):
        url = "https://viacep.com.br/ws/{}/json/".format(self.cep)
        r = requests.get(url)
        dados = r.json()
        bairro = dados.get('bairro')
        cidade = dados.get('localidade')
        uf = dados.get('uf')
        return bairro, cidade, uf
        '''return (
            dados['bairro'],
            dados['localidade'],
            dados['uf']
        )
        '''