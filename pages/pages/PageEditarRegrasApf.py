
from Pyautomators.desk import Desk
from Pyautomators.mouse_teclado import Teclado
from Pyautomators.mouse_teclado import Mouse
from pages.pages.PageLogin import PageLogin
from pages.pages.PageConsultaGestoresApf import PageConsultaGestoresApf
from pages.pages.PageConsultaRegrasApf import PageConsultaRegrasApf

from time import sleep

class PageEditarRegrasApf():

    def __init__(self,app):
        self.app = app
                 
    
    def digitar_alerta(self,alerta):

        ## campo user tw
        sleep(3)
        #self.app.clica_imagem(r'data\images\alerta_regras.png',similar=70)
        self.app.escrever_direto(alerta)
        self.app.digitos('tab')    
        sleep(2)

    def digitar_status(self,status):
        #campo tipo 
        #self.app.digitos('tab') 
        #self.app.clica_imagem(r'data\images\status_regras.png',similar=80)
        self.app.escrever_direto(status)
        #self.app.escrever_direto(tipo)
        self.app.digitos('tab')
        sleep(4)

    def excluir_regra(self):
        
        self.app.clica_imagem(r'data\images\botaoXexcluirpromotor.png',similar=60)
        sleep(4)
    
    def confirma_alteracoes_alerta(self):
       #botao confirma alteracoes antes sair  
        sleep(2)
        self.app.clica_imagem(r'data\images\aceitar_regras.png',similar=80)
        sleep(2)
        ##self.app.combo_digitos('alt','f4')
    
    def fechar_tela_alertas(self):
       #botao confirma alteracoes antes sair  
    #    sleep(5)
        self.app.clica_imagem(r'data\images\X_fechar_tela_alertas.png',similar=80)
        sleep(2)
        ##self.app.combo_digitos('alt','f4')
    
    def confirma_sair(self):
       #botao confirma alteracoes antes sair  
    #    sleep(5)
        self.app.clica_imagem(r'data\images\sim_sair_regras.png',similar=80)
        sleep(2)
        ##self.app.combo_digitos('alt','f4')