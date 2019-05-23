import getpass 

class IncluiParametro():

    def __init__(self, app, tron):
        self.app = app
        self.validacao = tron
    
    def abrir_criar_registro(self):
        self.validacao.validacao_tela(imagem=r'data\images\criar_registro.PNG')
        self.app.clica_imagem(r'data\images\criar_registro.PNG',similar=80)
        self.validacao.validacao_tela(imagem=r'data\images\cobertura.PNG')
    
    def digitar_cobertura(self,cobertura):
        self.app.clica_imagem(r'data\images\cobertura.PNG',similar=80)
        self.app.clica_imagem(r'data\images\input_cobertura.PNG',similar=80)
        self.app.escrever_direto(cobertura)
        self.app.digitos('tab')

    def digitar_ramo(self, ramo):
        self.app.clica_imagem(r'data\images\ramo.PNG',similar=80)
        self.app.clica_imagem(r'data\images\input_ramo.PNG',similar=80)
        self.app.escrever_direto(ramo)
        self.app.digitos('tab')

    def digitar_modalidade(self,modalidade):
        self.app.clica_imagem(r'data\images\campo_modalidade.PNG',similar=80)
        self.app.escrever_direto(modalidade)
        self.app.digitos('tab')

    def digitar_imp_segurada(self,imp):
        self.app.clica_imagem(r'data\images\campo_imp_segurada.PNG',similar=80)
        self.app.escrever_direto(imp)
        self.app.digitos('tab')

    def preencher_vigencia(self,data_atual,data_final):
        self.app.clica_imagem(r'data\images\campo_inicio_vigencia.PNG',similar=80)
        self.app.escrever_direto(data_atual)
        self.app.digitos('tab')
        self.app.escrever_direto(data_final)

    def validar_mensagem(self,mensagem=''):
        self.validacao.validacao_tela(imagem=mensagem)
        self.app.clica_imagem(mensagem,similar=80)

    def fechar_criacao_de_registro(self):
        user = getpass.getuser()
        if(user == 'gsilvan'):
            self.app.clica_imagem(r'data\images\botao_fechar_gsilvan.PNG',similar=80)
        elif(user == 'jvictorr'):
            self.app.clica_imagem(r'data\images\botao_fechar.PNG',similar=80)
        elif(user == 'mconceicaos'):
            pass
        else:
            print('Usuário não cadastrado.')

    def aceitar_criacao_registro(self):
        self.app.clica_imagem(r'data\images\aceitar3.PNG',similar=80)

   
