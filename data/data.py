from Pyautomators.Dados import pegarConteudoXLS as excel 

class Data():

    
    def __init__(self, app):
        self.app = app

    ''' ******** LEITURA DOS DADOS - FUNCIONALIDADE ENVIO APOLICE E ENDOSSO PARA O RE21 ********* '''

    def read_excel_envio_apolice_endosso(self):
        arquivo = excel('./data/data.xlsx', 'EnvioApoliceEndossoRE21')
        values = dict(zip(arquivo['campo de input'], arquivo['valor']))
        return values

    def numero_de_cobertura(self):
        return self.read_excel_envio_apolice_endosso().get('Número de cobertura', '')
    
    def numero_de_prod(self):
        return self.read_excel_envio_apolice_endosso().get('Número de prod', '')
    
    def tipo_de_emissao(self):
        return self.read_excel_envio_apolice_endosso().get('Tipo de emissao', '')

    def numero_do_canal(self):
        return self.read_excel_envio_apolice_endosso().get('Número canal', '')
    
    def numero_da_apolice(self):
        return self.read_excel_envio_apolice_endosso().get('Número da apolice', '')

    ''' ******** LEITURA DOS DADOS - FUNCIONALIDADE ENVIO APOLICE E ENDOSSO PARA O RE21 ********* '''