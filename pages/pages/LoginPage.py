from Pyautomators.desk import Desk
from Pyautomators.mouse_teclado import Teclado
from Pyautomators.mouse_teclado import Mouse
from Pyautomators.Verifica import Valida
import pyautogui
# import ctypes
from time import sleep


class Login():

    def __init__(self, app):
        self.app = app
        self.mouse = Mouse()
        self.teclado = Teclado()
        self.asserts = Valida()
        
    def realiza_login(self):
        while(Valida.verifica_tela("data\images\senha.png", 80, similaridade=50) == None):
            if(Valida.verifica_tela("data\images\senha.png", 80, similaridade=50) != None):
                break
            else:
                pass
        self.mouse.clica_imagem(r'data\images\senha.PNG', similar=70)
        self.teclado.escrever_direto('Mapfre2019')
        self.teclado.digitos('enter')

    def valida_login(self):
        sleep(3)
        self.mouse.clica_imagem(r'data\images\tron.PNG', similar=70)
    



