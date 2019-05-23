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
    
    def read_excel_cadastro_parametro(self):
        arquivo = excel('./data/data.xlsx', 'CadastroParametrosResseguro')
        values = dict(zip(arquivo['campo de input'], arquivo['valor']))
        return values
    
    '''******************* Enviar Apolice e Endosso RE21 ************************'''

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
    
    '''******************* Cadastra Parametro Resseguro ************************'''

    def cobertura(self):
        return str(self.read_excel_cadastro_parametro().get('Cobertura', ''))
    
    def modalidade(self):
        return str(self.read_excel_cadastro_parametro().get('Modalidade', ''))
    
    def imp_segurada(self):
        return str(self.read_excel_cadastro_parametro().get('Imp segurada', ''))

    
