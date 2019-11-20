
from Pyautomators.desk import Desk
from Pyautomators.mouse_teclado import Teclado
from Pyautomators.mouse_teclado import Mouse
from pages.pages.PageLogin import PageLogin
from pages.pages.PageConsultaGestoresApf import PageConsultaGestoresApf

from time import sleep

class PageEditarGestoresApf():

    def __init__(self,app):
        self.app = app
                 
    
    def habilitar_edicao(self):

        ## clicar LAPIS

        self.app.clica_imagem(r'data\images\editarpromotor.png', similar=70)
        ##self.app.clica_imagem(r'data\images\adicionarpromotor.png', similar=70)    
        sleep(5) 
    
    def habilitar_inclusao(self):

        ## clicar LAPIS

        self.app.clica_imagem(r'data\images\incluir.png', similar=70)
        ##self.app.clica_imagem(r'data\images\adicionarpromotor.png', similar=70)    
        sleep(5) 

    def digitar_usertw(self,usertw):

        ## campo user tw 
        sleep(2)
        self.app.clica_imagem(r'data\images\USUARIOTW_INCLUSAOPROMOTOR.png', similar=70)
        self.app.escrever_direto(usertw)
        self.app.digitos('tab')    
        sleep(4)

    def digitar_tipo(self,tipo):
        #campo tipo 
        #self.app.digitos('tab') 
        #self.app.clica_imagem(r'data\images\tipo_inclusao_promotor.png',similar=80)
       
        self.app.escrever_direto(tipo)
        #self.app.escrever_direto(tipo)
        self.app.digitos('tab')
        sleep(4)

    def digitar_ativo(self,ativo):
        #campo ativo 
            
        #self.app.clica_imagem(r'data\images\ativoinclusaopromotor.png',similar=80)
        self.app.escrever_direto(ativo)
        self.app.digitos('tab')
        sleep(5)
    
    
    #def validar_mensagem(self,mensagem):
    #    sleep(5)
    #    ##self.validacao.validacao_tela(imagem=mensagem)
    #    print('ooooooooooooooooooooooooooooooooi teste')
    #    print(mensagem)
    #    self.app.clica_imagem(mensagem,similar=80)    

    def efetiva_alteracao(self):
        ## botao aceitar janela inclusao / alteracao 
        self.app.clica_imagem(r'data\images\botao_aceitar.png',similar=80)
        #self.app.clica_imagem(r'data\images\aceitar_janela_alter.png',similar=80)
        sleep(2)
        self.app.combo_digitos('alt','f4')
    
    def efetiva_inclusao(self):
        ## botao NOVA ENTRADA  janela inclusao / alteracao 
        ##self.app.clica_imagem(r'data\images\botao_aceitar.png',similar=80)
        #self.app.clica_imagem(r'data\images\novaentrada.png',similar=80)
        self.app.clica_imagem(r'data\images\botaonovaentrada.png',similar=50)    
        sleep(2)
        self.app.combo_digitos('alt','f4')


    def fechar_janela_edicao(self):
        #fechar tela pesquisa promotor 
        sleep(2)
        self.app.combo_digitos('alt','f4')
        sleep(3)
        #self.app.clica_imagem(r'data\images\X_janela_alterapromotor.png', similar=70)
        
        
    def confirma_alteracoes(self):
       #botao confirma alteracoes antes sair  
    #    sleep(5)
        self.app.clica_imagem(r'data\images\aceitartelapromotor.png',similar=80)
        sleep(2)
        ##self.app.combo_digitos('alt','f4')
    
    def confirma_sair(self):
       #botao confirma alteracoes antes sair  
    #    sleep(5)
        self.app.clica_imagem(r'data\images\botaosim_sair_regras.png.png',similar=80)
        sleep(2)
    
    
    