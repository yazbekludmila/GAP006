from Pyautomators.desk import Desk
from Pyautomators.mouse_teclado import Teclado
from Pyautomators.mouse_teclado import Mouse
from pages.pages.TronWebPage import TronWeb

class ConsultaParametro():

    def __init__(self, app):
        self.app = app
        self.mouse = Mouse()
        self.teclado = Teclado()
        self.TronWeb = TronWeb(self.app)


    def consulta_parametro_reasseguro(self, ramo='', produto=''):
        self.mouse.clica_imagem(r'data\images\campo_busca.png',similar=70)
        self.teclado.escrever_direto('re21')
        self.teclado.digitos('enter')
        # self.TronWeb.validacao_tela(imagem=r'data\images\tela_parametrizacao_envio.png')
        self.mouse.clica_imagem(r'data\images\parametrizacao_envio.png',similar=70, cliques=2)
        self.TronWeb.validacao_tela(imagem=r'data\images\tela_parametrizacao_envio.png')
        self.mouse.clica_imagem(r'data\images\tela_parametrizacao_envio.png',similar=70)
        # self.mouse.clica_imagem(r'data\images\input_ramo.png',similar=70)
        if(ramo != ''):
            self.teclado.escrever_direto(ramo)
            self.teclado.digitos('tab')
        else:
            return self.teclado.digitos('tab')
        # self.mouse.clica_imagem(r'data\images\input_produto.png',similar=70)
        self.teclado.escrever_direto(produto)
        self.teclado.digitos('enter')
    
    def verifica_msg_campo_obrigatorio(self):
        self.mouse.clica_imagem(r'data\images\campo_obrigatorio.png',similar=70)

