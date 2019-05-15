from Pyautomators.desk import Desk
from Pyautomators.mouse_teclado import Teclado
from Pyautomators.mouse_teclado import Mouse
from time import sleep

class IncluiParametro():

    def __init__(self, app):
        self.app = app
        self.mouse = Mouse()
        self.teclado = Teclado()

    def inclui_parametro(self):
        self.mouse.clica_imagem(r'data\images\editar.PNG',similar=80)


