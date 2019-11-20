
from Pyautomators.desk import Desk
from Pyautomators.mouse_teclado import Teclado
from Pyautomators.mouse_teclado import Mouse
from pages.pages.PageLogin import PageLogin
from time import sleep

class PageConsultaGestoresApf():

    def __init__(self,app):
        self.app = app
            
    # digitar promotores na caixa de menus para abrir menu promotores 
    #  
    def selecionar_menu_promotor(self):
        self.app.clica_imagem(r'data\images\procuramenu.png', similar=70)
        self.app.escrever_direto('promotor')
        self.app.digitos('enter')      
        sleep(5)         
    ##duplo clique munu promotoress = abrir janela promotores
    def selecionar_menu01(self):
        self.app.clica_imagem(r'data\images\MENUPROMOTORESLCFO.png',similar=80, cliques =2 )
        sleep(5)  


    def pesquisar_todos_promotores_cadastrados(self, usertw, usercts):
        
        if(usertw == ' ' and usercts== '0'):   # pesquisa geral 
            self.app.clica_imagem(r'data\images\pesquisarpromotor.png',similar=80)
            sleep(5)   
            
        else:    ### faz pesqauisa de acordo com parametros passados 
            self.app.clica_imagem(r'data\images\usuariotw.png', similar=70)
            self.app.escrever_direto(usertw)
            self.app.digitos('tab')    
            self.app.escrever_direto(usercts)
            self.app.clica_imagem(r'data\images\pesquisarpromotor.png',similar=80)
            sleep(5)
        
    def fechar_tela_promotores(self):
        #fechar tela pesquisa promotor 
        self.app.clica_imagem(r'data\images\x_fechartelapromotores.png', similar=70)
        #sleep(2)
        # 
        #self.app.combo_digitos('alt','f4') 
        sleep(2)
        
    def encerra_tw(self):
        #fechar menu tw 
        ##self.app.clica_imagem(r'data\images\x_fecharmenutw.png', similar=70)
        self.app.combo_digitos('alt','f4')
        sleep(3)
        # fechar tw botao terminar 
        #self.app.combo_digitos('alt','f4')
        self.app.clica_imagem(r'data\images\terminatw.png', similar=70)
        sleep(2)
    
    
