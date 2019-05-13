from Pyautomators.desk import Desk
from Pyautomators.mouse_teclado import Teclado
from Pyautomators.mouse_teclado import Mouse
import pyautogui
# import ctypes
from time import sleep


class Login():

    def __init__(self, app):
        self.app = app
        self.mouse = Mouse()
        self.teclado = Teclado()
        
    def realiza_login(self):
        sleep(2)
        self.mouse.clica_imagem(r'data\images\usuario.PNG', similar=70)
        self.mouse.clica_imagem(r'data\images\senha.PNG', similar=70)
        
        self.teclado.escrever_direto('@indra2018bb')
        self.teclado.digitos('enter')

    def valida_login(self):
        sleep(3)
        self.mouse.clica_imagem(r'data\images\tron.PNG', similar=70)
    



