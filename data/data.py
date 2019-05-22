from Pyautomators.Dados import pegarConteudoXLS as excel 

class Data():

    arquivo = None
    values = None

    def __init__(self, app):
        self.app = app

    def read_excel(self):
        arquivo = excel('./data/data.xlsx', 'TronWeb')
        values = dict(zip(arquivo['campo de input'], arquivo['valor']))
        return values

    def numero_de_cobertura(self):
        return self.read_excel().get('Número de cobertura', '')

    def numero_de_prod(self):
        return self.read_excel().get('Número de prod', '')

    def tipo_de_emissao(self):
        return self.read_excel().get('Tipo de emissao', '')

    def numero_do_canal(self):
        return self.read_excel().get('Número canal', '')

    def numero_da_apolice(self):
        return self.read_excel().get('Número da apolice', '')

    def cobertura(self):
        return str(self.read_excel().get('Cobertura', ''))

    