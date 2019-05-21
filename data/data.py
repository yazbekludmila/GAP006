from Pyautomators.Dados import pegarConteudoXLS as excel 

class Data():

    def __init__(self, app):
        self.app = app
        arquivo = excel('./data/data.xlsx', 'TronWeb')
        values = dict(zip(arquivo['campo de input'], arquivo['valor']))
    
    def numero_de_cobertura(self):
        return self.values.get('Número de cobertura', '')
    
    def numero_de_prod(self):
        return self.values.get('Número de prod', '')
    
    def tipo_de_emissao(self):
        return self.values.get('Tipo de emissao', '')

    def numero_do_canal(self):
        return self.values.get('Número canal', '')
    
    def numero_da_apolice(self):
        return self.values.get('Número da apolice', '')