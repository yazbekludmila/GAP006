
from Pyautomators.desk import Desk
from Pyautomators.mouse_teclado import Teclado
from Pyautomators.mouse_teclado import Mouse
from pages.pages.PageLogin import PageLogin
from time import sleep

class PageConsultaRegrasApf():

    def __init__(self,app):
        self.app = app
            
    # digitar promotores na caixa de menus para abrir menu promotores 
    #  

    def selecionar_menu_regras_Alerta(self):
        self.app.clica_imagem(r'data\images\procuramenu.png', similar=70)
        self.app.escrever_direto('regras de alerta')
        self.app.digitos('enter')      
        sleep(5)         
    ##duplo clique munu promotoress = abrir janela promotores
    def selecionar_menu_regras_Alerta02(self):
        self.app.clica_imagem(r'data\images\menu_regras_alerta.png',similar=80, cliques =2 )
        sleep(5)  


    def pesquisar_todos_alertas_cadastrados(self, id_chave, status_chave):
        
        if(id_chave == '0' and status_chave == ' '):   # pesquisa geral 
            self.app.clica_imagem(r'data\images\pesquisarpromotor.png',similar=80)
            sleep(5)   
            
        else:    ### faz pesqauisa de acordo com parametros passados 
            self.app.clica_imagem(r'data\images\ID_PESQ_REGRAS.png', similar=50)
            self.app.escrever_direto(id_chave)
            self.app.digitos('tab')    
            self.app.escrever_direto(status_chave)
            self.app.clica_imagem(r'data\images\pesquisarpromotor.png',similar=80)
            sleep(5)
        
    def fechar_tela_alertas(self):
        #fechar tela pesquisa regras alerta 
        self.app.clica_imagem(r'data\images\X_fechar_tela_alertas.png', similar=50)
        #sleep(2)
        # 
        #self.app.combo_digitos('alt','f4') 
        sleep(2)
        
    #def encerra_tw(self):
        #fechar menu tw 
        ##self.app.clica_imagem(r'data\images\x_fecharmenutw.png', similar=70)
    #    self.app.combo_digitos('alt','f4')
    #    sleep(3)
        # fechar tw botao terminar 
        #self.app.combo_digitos('alt','f4')
    #    self.app.clica_imagem(r'data\images\terminatw.png', similar=70)
    #    sleep(2)
    
    
