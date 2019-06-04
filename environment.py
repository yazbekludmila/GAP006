
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
from pages.pages.EmissaoDeApolicesEEndossoPage import EmissaoDeApolices
from data.data import Data
from Pyautomators.Documentacao import printarTela
import os
import getpass


# Modulos extras
from time import sleep
def name_image(feature,scenario,step):
	return str("{feature}-{scenario}-{step}.png".format(feature=feature,scenario=scenario,step=step)).replace('<',"").replace(">","").replace("'","").replace('"',"")

def before_all(context):
	pass

def before_feature(context,feature):
	pass

def before_scenario(context,scenario):
	context.app = Desk('C:\JTron_Homolog\JMenuTron.bat',Driver_Winium='driver\Winium.Desktop.Driver.exe')
	# context.login = Login(context.app)
	context.consulta_parametro = ConsultaParametro(context.app)
#	context.menu = MenuPrincipal(context.app)
	context.tronweb = TronWeb(context.app)
	context.inclui_parametro = IncluiParametro(context.app, context.tronweb)
	context.dados = Data(context.app)
	context.cadastro_apolice = CadastroApolice(context.app)
	context.emissao = EmissaoDeApolices(context.app)

def before_step(context,step):
	pass

def after_step(context,step):
	context.print = printarTela(NomeArquivo="docs/image/{image}".format(image=name_image(context.feature.name,context.scenario.name,step.name)))

def after_scenario(context,scenario):
	context.app.fechar_programa()

def after_feature(context,feature):
	pass

def after_all(context):
	pass

