from Pyautomators.Dados import pegarConteudoXLS as excel 

class Data():

    arquivo = None
    values = None

    def __init__(self, app):
        self.app = app

    def read_excel_envio_apolice(self):
        arquivo = excel('./data/data.xlsx', 'EnvioApoliceEndossoRE21')
        values = dict(zip(arquivo['campo de input'], arquivo['valor']))
        return values

    def numero_de_cobertura(self):
        return self.read_excel_envio_apolice().get('Número de cobertura', '')

    def numero_de_prod(self):
        return self.read_excel_envio_apolice().get('Número de prod', '')

    def tipo_de_emissao(self):
        return self.read_excel_envio_apolice().get('Tipo de emissao', '')

    def numero_do_canal(self):
        return self.read_excel_envio_apolice().get('Número canal', '')

    def numero_da_apolice(self):
        return self.read_excel_envio_apolice().get('Número da apolice', '')

    def cobertura(self):
        return str(self.read_excel_envio_apolice().get('Cobertura', ''))

    
