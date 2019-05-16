from Pyautomators.desk import Desk
from Pyautomators.mouse_teclado import Teclado
from Pyautomators.mouse_teclado import Mouse

class ConsultaParametro():

    def __init__(self, app):
        self.app = app
        self.mouse = Mouse()
        self.teclado = Teclado()


   def consulta_parametro_reasseguro(self, ramo='', produto=''):
        self.mouse.clica_imagem(r'data\images\campo_busca.png',similar=70)
        self.teclado.escrever_direto('re21')
        self.teclado.digitos('enter')
        self.mouse.clica_imagem(r'data\images\parametrizacao_envio.png',similar=70, cliques=2)
        self.mouse.clica_imagem(r'data\images\tela_parametrizacao_envio.png',similar=70)
        # self.mouse.clica_imagem(r'data\images\input_ramo.png',similar=70)
        self.teclado.escrever_direto(ramo)
        self.teclado.digitos('tab')
        # self.mouse.clica_imagem(r'data\images\input_produto.png',similar=70)
        self.teclado.escrever_direto(produto)
        self.teclado.digitos('enter')

