from validate_docbr import CPF, CNPJ

class Documento:
    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError("Quantidade de números errados!!!")

class DocCpf:
    def __init__(self, documento):
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError("Cpf inválido")
    
    def __str__(self):
        return self.format()

    def valida(self, documento):
        valido = CPF()
        return valido.validate(documento)
    def format(self):
        masc = CPF()
        return masc.mask(self.cpf)

class DocCnpj:
    def __init__(self, documento):
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError("Cnpj inválido")

    def __str__(self):
        return self.format()

    def valida(self, documento):
        meu_cnpj = CNPJ()
        return meu_cnpj.validate(documento)
    def format(self):
        meu_cnpj = CNPJ()
        return meu_cnpj.mask(self.cnpj)


'''class CpfCnpj:

    def __init__(self, documento, tipo_documento):
        self.documento = str(documento)
        self.tipo_documento = tipo_documento

        if self.tipo_documento == 'cpf':
            if self.valida_cpf(self.documento):
                self.cpf = self.documento
            else:
                raise ValueError("CPF inválido!!!")
        elif self.tipo_documento == 'cnpj':
            if self.valida_e_cnpj(self.documento):
                self.cnpj = self.documento
            else:
                raise ValueError("CPNJ inválido!!!")
        else:
            raise ValueError("Documento não aceito!!!")

    def valida_cpf(self, documento):
        if len(documento) == 11:
            valido = CPF()
            return valido.validate(documento)
        else:
            raise ValueError("CPF com quantidade de números errada ou CPF inválido.");
    
    def mascara(self):
        masc = CPF()
        return masc.mask(self.cpf)
    
    def format_cnpj(self):
        masca = CNPJ()
        return masca.mask(self.cnpj)
    
    def __str__(self):
        if self.tipo_documento == 'cpf':
            return self.mascara()
        elif self.tipo_documento == 'cnpj':
            return self.format_cnpj()
    
    def valida_e_cnpj(self, documento):
        if len(documento) == 14:
            valida_cnpj = CNPJ()
            return valida_cnpj.validate(documento)
        else:
            raise ValueError("Quantidade números erroneamente colocadas.")

        def format_cpf(self):
        fatia_um = self.cpf[:3]
        fatia_dois = self.cpf[3:6]
        fatia_tres = self.cpf[6:9]
        fatia_quatro = self.cpf[9:]

        return("{}.{}.{}-{}".format(

        fatia_um, fatia_dois, fatia_tres, fatia_quatro
            )
        )
    '''