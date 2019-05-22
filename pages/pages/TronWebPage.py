import getpass
from datetime import datetime
from dateutil.relativedelta import relativedelta

class TronWeb():

    def __init__(self, app):
        self.app = app

    def realizar_login(self):
        self.app.clica_imagem(r'data\images\senha.PNG', similar=70)
        if(getpass.getuser() == 'gsilvan'):
            self.app.escrever_direto('Mapfre2019')
        elif(getpass.getuser() == 'jvictorr'):
            self.app.escrever_direto('@indra2018bb')
        else:
            print('Usuario não reconhecido.')
        self.app.digitos('enter')
    
    def selecionar_menu_emissao(self,opcao):
        self.app.clica_imagem(r'data\images\opcao_tronweb.png', similar=70, cliques=2)
        self.app.verifica_tela(r'data\images\opcao_emissao.png', 80, similaridade=50)
        self.app.clica_imagem(r'data\images\opcao_emissao.png', similar=70, cliques=2)
        self.app.clica_imagem(r'data\images\botao_direita.png', similar=70, cliques=1)
        if(opcao == 'Menu de Atualizacoes'):
            self.app.clica_imagem(r'data\images\opcao_menu_de_atualizacoes.png', similar=70, cliques=2)
        else:
            print('Selecione uma opcao valida.')
    
    def selecionar_menu_atualizacoes(self,opcao):
        self.selecionar_menu_emissao('Menu de Atualizacoes')
        if(opcao == 'Cadastro Apolices Envio RE21'):
            self.app.clica_imagem(r'data\images\baixo.png', similar=70, cliques=4)
            self.app.clica_imagem(r'data\images\cadastro_apolice.png', similar=70, cliques=2)
        elif(opcao == 'Emissao de Apolices e Endosso'):
            self.app.clica_imagem(r'data\images\opcao_emissao_de_apolices.png', similar=70, cliques=2)
        elif(opcao == 'Parametrizacao do Envio Re21'):
            self.app.clica_imagem(r'data\images\baixo.png', similar=40, cliques=13)
            self.app.clica_imagem(r'data\images\botao_direita.png', similar=70, cliques=2)
            self.app.clica_imagem(r'data\images\parametrizacao_envio.png',similar=70, cliques=2)

    def validacao_tela(self,imagem):
        tentativas = 50
        for tentativa in range(tentativas):
            if(self.app.verifica_tela(imagem, 80, similaridade=50) != None):
                break
            else:
                pass

    def get_data_atual(self):
        data_atual = datetime.today().strftime('%d%m%Y')
        return data_atual

    def get_data_futura(self):
        data_futura = (datetime.today() + relativedelta(years=1)).strftime('%d%m%Y')
        return data_futura