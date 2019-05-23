
"""		Pyautomator Framework de teste 

			TRONWEB"""
# Pacotes Pyautomators
from Pyautomators.desk import Desk
from Pyautomators.mouse_teclado import Teclado
from Pyautomators.mouse_teclado import Mouse
from Pyautomators.Verifica import Valida
from Pyautomators import Ambiente
from pages.pages.TronWebPage import TronWeb
from pages.pages.ConsultaParametroPage import ConsultaParametro
from pages.pages.CadastroApolicesEnvioRe21Page import CadastroApolice
from pages.pages.IncluiParametroPage import IncluiParametro
from data.data import Data
import os
import getpass


# Modulos extras
from time import sleep

def before_all(context):
	pass

def before_feature(context,feature):
	pass

def before_scenario(context,scenario):
	if(getpass.getuser() == 'mconceicaos'):
		context.app = Desk('/home/JMenuTron.bat',Driver_Winium='/home/Winium.Desktop.Driver.exe')
	else:
		context.app = Desk('C:\JTron_Homolog\JMenuTron.bat',Driver_Winium='driver\Winium.Desktop.Driver.exe')
	
	# context.login = Login(context.app)
	context.consulta_parametro = ConsultaParametro(context.app)
#	context.menu = MenuPrincipal(context.app)
	context.tronweb = TronWeb(context.app)
	context.inclui_parametro = IncluiParametro(context.app, context.tronweb)
	context.dados = Data(context.app)
	context.cadastro_apolice = CadastroApolice(context.app)

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

