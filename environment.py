
"""		Pyautomator Framework de teste 

			TRONWEB"""
# Pacotes Pyautomators
from Pyautomators.desk import Desk
from Pyautomators.mouse_teclado import Teclado
from Pyautomators.mouse_teclado import Mouse
from Pyautomators.Verifica import Valida
from Pyautomators import Ambiente
from data.data import Data
import getpass
import os
from pages.pages.PageLogin import PageLogin
from pages.pages.PageConsultaGestoresApf import PageConsultaGestoresApf
from pages.pages.PageEditarGestoresApf import PageEditarGestoresApf

from pages.pages.PageConsultaRegrasApf import PageConsultaRegrasApf
from pages.pages.PageEditarRegrasApf import PageEditarRegrasApf

from Pyautomators.Documentacao import printarTela



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
	context.loginmenu          = PageLogin(context.app)
	context.gestoresapf        = PageConsultaGestoresApf(context.app)
	context.editagestoresapf   = PageEditarGestoresApf(context.app)
	context.regrasapf          = PageConsultaRegrasApf(context.app)
	context.editaregrasapf     = PageEditarRegrasApf(context.app)


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