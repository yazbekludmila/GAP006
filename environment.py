
"""		Pyautomator Framework de teste 

			TRONWEB"""
# Pacotes Pyautomators
from Pyautomators.desk import Desk
from Pyautomators.mouse_teclado import Teclado
from Pyautomators.mouse_teclado import Mouse
from Pyautomators.Verifica import Valida
from Pyautomators import Ambiente
from pages.pages.LoginPage import Login
from pages.pages.ConsultaParametroPage import ConsultaParametro
from pages.pages.MenuPrincipalPage import MenuPrincipal
from pages.pages.IncluiParametroPage import IncluiParametro
import os


# Modulos extras
from time import sleep

def before_all(context):
	pass

def before_feature(context,feature):
	pass

def before_scenario(context,scenario):
	context.app = Desk('C:\JTron_Homolog\JMenuTron.bat',Driver_Winium='driver\Winium.Desktop.Driver.exe')
	context.login = Login(context.app)
	context.consulta_parametro = ConsultaParametro(context.app)
	context.menu = MenuPrincipal(context.app)
	context.inclui_parametro = IncluiParametro(context.app)

def before_step(context,step):
	pass

def after_step(context,step):
	pass

def after_scenario(context,scenario):
	context.app.fechar_programa()

def after_feature(context,feature):
	pass

def after_all(context):
	pass

