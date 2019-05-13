from Pyautomators.desk import Desk
from Pyautomators.mouse_teclado import Teclado
from Pyautomators.mouse_teclado import Mouse

class ConsultaParametro():

    def __init__(self, app):
        self.app = app
        self.mouse = Mouse()
        self.teclado = Teclado()


    def consulta_parametro_reasseguro(self):
        self.mouse.clica_imagem(r'data\images\campo_busca.png',similar=70)
        self.teclado.escrever_direto('re21')
        self.teclado.digitos('enter')
        self.mouse.clica_imagem(r'data\images\parametrizacao_envio.png',similar=70, cliques=2)
        # self.mouse.clica_imagem(r'data\images\mais.png',similar=70)
        # self.mouse.clica_imagem(r'data\images\emissao.PNG',cliques=2, similar=70)
        # self.mouse.clica_imagem(r'data\images\menu_atualizacoes.PNG',cliques=2, similar=70)

        
        
